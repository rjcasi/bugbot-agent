import requests
from bs4 import BeautifulSoup  # pip install beautifulsoup4

def fetch_page(url: str) -> str:
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    return resp.text

def extract_info(html: str):
    soup = BeautifulSoup(html, "html.parser")
    titles = [t.get_text(strip=True) for t in soup.find_all(["h1", "h2", "h3"])]
    links = [a["href"] for a in soup.find_all("a", href=True)]
    return titles, links

def main():
    url = "https://www.python.org/"
    html = fetch_page(url)
    titles, links = extract_info(html)

    print("== TITLES ==")
    for t in titles:
        print("-", t)

    print("\n== LINKS ==")
    for l in links[:20]:
        print("-", l)

if __name__ == "__main__":
    main()
