from twttr import shorten

def test_lowercase():
    assert shorten("twitter") == "twttr"
    assert shorten("hello") == "hll"
    assert shorten("aeiou") == ""

def test_uppercase():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("HELLO") == "HLL"
    assert shorten("AEIOU") == ""

def test_mixed_case():
    assert shorten("TwItTeR") == "TwtTR"
    assert shorten("ApPlE") == "pPl"

def test_numbers():
    assert shorten("h3ll0") == "h3ll0"
    assert shorten("12345") == "12345"

def test_symbols():
    assert shorten("h@ppy!") == "h@ppy!"
    assert shorten("AE!IOU?") == "!?"

def test_empty():
    assert shorten("") == ""