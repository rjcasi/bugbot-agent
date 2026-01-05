from utils import fetch, parse_page, find_next_page

def scrape(start_url: str):
    url = start_url
    all_titles = []
    all_links = []

    while url:
        print(f"[+] Fetching: {url}")
        html = fetch(url)
        titles, links = parse_page(html)

        all_titles.extend(titles)
        all_links.extend(links)

        next_page = find_next_page(html)
        if next_page and not next_page.startswith("http"):
            # Convert relative to absolute
            base = start_url.rsplit("/", 1)[0]
            next_page = f"{base}/{next_page}"

        url = next_page

    return all_titles, all_links

def main():
    start_url = input("Enter URL to scrape (default: https://example.com): ").strip()
    if not start_url:
        start_url = "https://example.com"

    titles, links = scrape(start_url)

    print("\n=== Titles ===")
    for t in titles:
        print("-", t)

    print("\n=== Links ===")
    for l in links:
        print("-", l)

if __name__ == "__main__":
    main()
