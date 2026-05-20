# scraper.py
# This files handles basic webpage text extraction for job opsting URLs.

import requests
from bs4 import BeautifulSoup

def extract_text_from_url(url):
    """
    Fetch visible text from a webpage URL.

    Parameters:
        url (str): The job posting URL entered by the user.
    Returns:
        str: Extracted visible text from the webpage.
    
    Raise:
        ValueError: If the URL is empty, invalid, blocked, or text cannot be extracted.
    """

    if not url or not url.strip():
        raise ValueError("No URL Provided.")
    
    url = url.strip()

    # add https:// if user types a URL without it

    if not url.startswith(("http://", "https://")):
        url = "https://" + url
    
    # some website block requests that do not look like real browswer
    # this header makes our request look more like it came from Chrome.
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0 Safari/537.36"           
        )
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)

        # raise an error for bad response like 404 or 403
        response.raise_for_status()
    
    except requests.RequestException as error:
        raise ValueError(f"Could not fetch URL: {error}")
    

    # BeautifulSoup parses the HTML so we can remove unwantede parts and extract readable text
    soup = BeautifulSoup(response.text, "html.parser")

    # remove parts of the webpage that are usually not useful
    for tag in soup({"script", "style", "noscript", "header", "footer", "nav"}):
        tag.decompose()
    
    # convert the remaining HTML into plain text
    text = soup.get_text(separator="\n")

    # clean up 
    lines = [lines.strip() for line in text.splitlines()]
    lines = [line for line in lines if line]

    cleaned_text = "\n".join(lines)
    

    # if the extracted text is too short, the page may be blocked
    # or may not contain a readable JD
    if len(cleaned_text) < 200:
        raise ValueError("Extracted text is too short. The website may block scraping.")
    
    return cleaned_text