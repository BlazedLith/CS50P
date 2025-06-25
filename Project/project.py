import sys
import requests
from bs4 import BeautifulSoup


def fetch_url(url):
    """
    Fetch the HTML content of the given URL.
    Raises an exception if the request fails.
    """
    response = requests.get(url)
    response.raise_for_status()
    return response.text


def parse_items(html):
    """
    Parse the HTML to extract quotes and their authors.
    Returns a list of dictionaries.
    """
    soup = BeautifulSoup(html, "html.parser")
    quotes = []
    for q in soup.select(".quote"):
        text = q.select_one(".text").get_text(strip=True)
        author = q.select_one(".author").get_text(strip=True)
        quotes.append({"text": text, "author": author})
    return quotes


def analyze_data(quotes):
    """
    Analyze the list of quotes:
    - Count total quotes
    - Get unique authors
    """
    num_quotes = len(quotes)
    unique_authors = set(q["author"] for q in quotes)
    return {
        "num_quotes": num_quotes,
        "unique_authors": list(unique_authors)
    }


def main():
    """Scrape quotes from a user-provided URL with error handling."""
    url = input("Enter the URL to scrape (e.g. http://quotes.toscrape.com/): ").strip()

    if not url:
        sys.exit("No URL provided. Exiting.")

    try:
        html = fetch_url(url)
    except Exception as e:
        print(f"Error fetching the URL: {e}")
        return

    try:
        quotes = parse_items(html)
    except Exception as e:
        print(f"Error parsing the HTML: {e}")
        return

    if not quotes:
        print("No quotes found. Please check the page structure or your selectors.")
        return

    results = analyze_data(quotes)

    print("\n=== Quotes Found ===\n")
    for q in quotes:
        print(q["text"])
        print(f"— {q['author']}\n")

    print(f"Total quotes: {results['num_quotes']}")
    print(f"Unique authors: {len(results['unique_authors'])}")
    print("Authors:")
    for author in results['unique_authors']:
        print(f"- {author}")


if __name__ == "__main__":
    main()
