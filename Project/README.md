# Quotes Web Scraper

#### Video Demo: (https://youtu.be/6Pw-3-CLLic)

---

## Description

**Quotes Web Scraper** is a simple Python project demonstrating how to scrape, parse, analyze, and display quotes and authors from a user-provided website.
It is created as my final project for CS50P and fulfills all project requirements, including clear modular functions, proper error handling, and automated tests using `pytest`.

---

## What the Project Does

1. **Fetches** the HTML content of any URL given by the user.
2. **Parses** the HTML to find quotes and their authors (designed for [http://quotes.toscrape.com/]).
3. **Analyzes** the extracted data:
   - Counts the total number of quotes.
   - Identifies unique authors.
4. **Displays** each quote and author along with summary statistics in a readable format.

The project includes robust exception handling for network errors and parsing issues to ensure reliability.

---

## Files Included

### `project.py`
- `fetch_url(url)`: Downloads the HTML page and raises an error for failed requests.
- `parse_items(html)`: Extracts all quotes and authors using BeautifulSoup.
- `analyze_data(quotes)`: Counts total quotes and finds unique authors.
- `main()`: Handles user input, calls other functions, displays results, and manages errors.
- Contains an `if __name__ == "__main__"` block to run `main()` when executed directly.

### `test_project.py`
- Unit tests for `parse_items` and `analyze_data` using `pytest`.
- Ensures the parsing logic and analysis work as expected.

### `requirements.txt`
Contains:

requests
beautifulsoup4
pytest

## How to Use

1. **Install dependencies:**

    ```
    pip install -r requirements.txt
    ```

2. **Run the scraper:**

    python project.py

    Enter the URL when prompted, e.g. `http://quotes.toscrape.com/`.

3. **View results:**
    - Each quote and author will be printed.
    - Summary shows total quotes and a list of unique authors.

4. **Run tests:**

    pytest test_project.py

---

## Design Choices

- **User Input:** The user supplies any URL to scrape dynamically at runtime.
- **Error Handling:** All network and parsing steps use `try/except` to handle problems gracefully.
- **Modular Code:** Each step (fetching, parsing, analyzing) is isolated in its own function.
- **Testing:** Core functions are tested with realistic examples to verify correctness and handle edge cases.
- **Simplicity:** Focuses on clear, understandable scraping and text analysis for learning purposes.

---

## Notes

- Works best with sites structured like [quotes.toscrape.com](http://quotes.toscrape.com/).
- Scraping arbitrary websites may require adjusting HTML selectors in `parse_items`.
- Use responsibly and follow each site’s terms of service.

---

## Author

- **Name:** Wasiq Amir
- **GitHub Username:** BlazedLith
- **City & Country:** Layyah, Pakistan
