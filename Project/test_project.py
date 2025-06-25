from project import parse_items, analyze_data


def test_parse_items():
    html = """
    <div class="quote">
        <span class="text">“A witty quote.”</span>
        <span class="author">Jane Doe</span>
    </div>
    <div class="quote">
        <span class="text">“Another quote.”</span>
        <span class="author">John Smith</span>
    </div>
    """
    quotes = parse_items(html)
    assert len(quotes) == 2
    assert quotes[0]["text"] == "“A witty quote.”"
    assert quotes[0]["author"] == "Jane Doe"


def test_analyze_data():
    quotes = [
        {"text": "Quote A", "author": "Jane Doe"},
        {"text": "Quote B", "author": "John Smith"},
        {"text": "Quote C", "author": "Jane Doe"},
    ]
    result = analyze_data(quotes)
    assert result["num_quotes"] == 3
    assert "Jane Doe" in result["unique_authors"]
    assert "John Smith" in result["unique_authors"]
