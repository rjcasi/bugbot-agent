import requests
from bs4 import BeautifulSoup
import time

def fetch(url: str, delay: float = 0.5):
    """Fetch a URL with a small delay to avoid hammering servers."""
    time.sleep(delay)
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    return resp.text

def parse_page(html: str):
    """Extract titles and links from a page."""
    soup = BeautifulSoup(html, "html.parser")
    titles = [h.get_text(strip=True) for h in soup.find_all("h2")]
    links = [a["href"] for a in soup.find_all("a", href=True)]
    return titles, links

def find_next_page(html: str):
    """Find a 'Next' link if it exists."""
    soup = BeautifulSoup(html, "html.parser")
    next_link = soup.find("a", string=lambda s: s and "next" in s.lower())
    return next_link["href"] if next_link else None
