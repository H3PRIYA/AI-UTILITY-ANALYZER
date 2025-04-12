from flask import Flask, request, render_template
from transformers import pipeline
import spacy
import re
import warnings
warnings.filterwarnings("ignore")

try:
    from fuzzywuzzy import process
    FUZZY_AVAILABLE = True
except ImportError:
    FUZZY_AVAILABLE = False

app = Flask(__name__)

def text_summarizer(text):
    words = text.split()
    if len(words) < 5:
        return "Input is too short for summarization. Please provide at least 5 words.", False
    summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6", framework="pt")
    input_length = len(words)
    if input_length > 700:
        words = words[:700]
        text = " ".join(words)
        input_length = len(words)
    max_length = max(20, min(60, input_length + 5))
    min_length = max(5, input_length // 4)
    try:
        summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)[0]['summary_text']
        sentences = re.split(r'(?<=[.!?])\s+', summary.strip())
        return "\n".join(sentences[:3]), input_length > 700
    except IndexError:
        return "Error: Unable to generate summary. Try a longer input text.", False

def keyword_extractor(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    keywords = [token.text.lower() for token in doc if token.pos_ in ["NOUN", "PROPN", "ADJ"] and not token.is_stop]
    if not keywords:
        return ["No keywords found"] * 5

    keyword_freq = {}
    if FUZZY_AVAILABLE:
        for word in keywords:
            matches = process.extractOne(word, list(keyword_freq.keys()), score_cutoff=85)
            if matches:
                matched_word = matches[0]
                keyword_freq[matched_word] = keyword_freq.get(matched_word, 0) + 1
            else:
                keyword_freq[word] = 1
    else:
        for word in keywords:
            keyword_freq[word] = keyword_freq.get(word, 0) + 1

    sorted_keywords = sorted(keyword_freq, key=keyword_freq.get, reverse=True)
    while len(sorted_keywords) < 5:
        sorted_keywords.append(f"keyword_{len(sorted_keywords) + 1}")
    return sorted_keywords[:5]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form.get("text")
        if not text or text.strip() == "":
            return render_template("index.html", error="Please enter some text.")
        summary, was_truncated = text_summarizer(text)
        keywords = keyword_extractor(text)
        return render_template(
            "results.html",
            text=text,
            summary=summary,
            keywords=keywords,
            was_truncated=was_truncated
        )
    return render_template("index.html", error=None)

@app.route('/toggle_summary')
def toggle_summary():
    summary = request.args.get('summary', 'No summary available')
    return render_template('summary_toggle.html', summary=summary)

if __name__ == "__main__":
    app.run(debug=True)