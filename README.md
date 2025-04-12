# Smart Text Analyzer (Web Edition)
A Flask web app for summarizing text and extracting keywords using HuggingFace's DistilBART and spaCy.

## Features
- Summarizes text into 3 lines, covering multiple paragraphs.
- Extracts 5 keywords, merging similar terms (e.g., 'hari'/'Priya').
- Colorful UI: gradient backgrounds, syntax-highlighted output.
- Interactive: loading animation, summary toggle, keyword cloud, dark mode.
- Handles short/long inputs (5+ words, up to ~700).

## Setup
1. Create a virtual environment: `python -m venv venv`
2. Activate it: `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Mac/Linux)
3. Install dependencies: `pip install -r requirements.txt`
4. Install spaCy model: `python -m spacy download en_core_web_sm`
5. Run: `python app.py`
6. Open `http://127.0.0.1:5000`.

## Usage
- Enter text, click "Analyze Text".
- Toggle summary, view keyword cloud, switch dark mode.
- Copy results or analyze another.

## Dependencies
- Python 3.10
- Flask, transformers, spacy, torch, fuzzywuzzy, termcolor
- See `requirements.txt`

## Notes
- First run downloads models (~500MB).
- Requires ~2GB RAM, internet for Tailwind/Prism CDNs.
- Short inputs (<5 words) return an error.