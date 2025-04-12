# AI Text Utility (Web Edition)
A Flask web app for summarizing text and extracting keywords using HuggingFace's DistilBART and spaCy.

## Project Overview
The AI Text Utility is an interactive web application that summarizes text into 3-line outputs and extracts up to five relevant keywords. It features a colorful UI with gradient backgrounds, syntax-highlighted output, and interactive elements like a toggleable summary, animated keyword cloud, and dark mode toggle. The project leverages open-source models and is designed for users needing quick text analysis.

## Repository Structure
- **`app.py`**: Main Flask application file containing the logic for text summarization and keyword extraction.
- **`templates/`**: Folder containing HTML templates:
  - `index.html`: Home page for text input.
  - `results.html`: Results page with summary, keywords, and interactive features.
  - `summary_toggle.html`: Partial template for htmx summary toggle.
- **`static/`**: Folder for static assets:
  - `css/styles.css`: Custom CSS for styling and dark mode.
  - `js/scripts.js`: JavaScript for loading animation and interactivity.
- **`requirements.txt`**: List of Python dependencies required to run the project.
- **`README.md`**: This file, providing setup and usage instructions.

## Notes on `venv` Folder
The `venv` virtual environment folder is not included in this repository to keep it lightweight and avoid redundancy. Users must create and activate their own virtual environment locally following the setup steps below.

## Features
- Summarizes text into 3 lines, covering multiple paragraphs.
- Extracts 5 keywords, merging similar terms (e.g., 'hari'/'Priya').
- Colorful UI with gradient backgrounds and syntax-highlighted output.
- Interactive: loading animation, summary toggle, keyword cloud, dark mode.
- Handles short/long inputs (5+ words, up to ~700).

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ai-text-utility.git
2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Install the spaCy model:
   ```bash
   python -m spacy download en_core_web_sm
   ```
6. Run the application:
   ```bash
   python app.py
   ```
7. Open your browser at `http://127.0.0.1:5000`.

## Usage
- Enter text in the input box and click "Analyze Text".
- Toggle the summary, view the keyword cloud, or switch to dark mode.
- Copy results or analyze another text.

## Dependencies
- Python 3.10
- Flask, transformers==4.38.2, spacy==3.7.2, torch==2.0.1, fuzzywuzzy, termcolor
- See `requirements.txt` for the full list.

## Notes
- First run downloads models (~500MB), requiring ~2GB RAM.
- Internet access is needed for Tailwind CSS and Prism.js CDNs.
- Short inputs (<5 words) return an error.
- The `venv` folder is excluded; create it locally as instructed.

## Scope for Improvement
- Integrate advanced models for better summarization.
- Add multilingual support with additional spaCy models.
- Optimize for larger texts and improve mobile responsiveness.
