# AI Job Description Analyzer

AI Job Description Analyzer is a beginner-friendly NLP project that helps job seekers understand job descriptions.

Users can paste a job description or enter a job posting URL. The app returns:

- Short summary
- Skills list
- Tools / technologies
- Experience level estimate
- Resume keywords
- Suggested learning topics

## Tech Stack

- Python
- Gradio
- Requests
- BeautifulSoup
- Rule-based NLP / keyword extraction

## Current Features

- Analyze pasted job descriptions
- Extract skills and tools from job text
- Estimate experience level
- Suggest resume keywords
- Suggest learning topics
- Attempt basic URL extraction for job postings

## URL Extraction Note

Version 2 supports basic URL extraction. Some job sites block automated extraction or use JavaScript-rendered pages, so users can paste the job description manually as a fallback.

## How to Run Locally

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py