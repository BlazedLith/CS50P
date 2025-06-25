import pytest
from datetime import date
from unittest.mock import patch
from seasons import get_date

def test_valid_date():
    today = date(2025, 6, 12)
    with patch("builtins.input", return_value="2000-01-01"):
        assert get_date(today) == date(2000, 1, 1)

def test_future_date():
    today = date(2025, 6, 12)
    with patch("builtins.input", return_value="2030-01-01"):
        with pytest.raises(SystemExit):
            get_date(today)

def test_wrong_format():
    today = date(2025, 6, 12)
    with patch("builtins.input", return_value="01-01-2000"):
        with pytest.raises(SystemExit):
            get_date(today)

def test_random_text():
    today = date(2025, 6, 12)
    with patch("builtins.input", return_value="hello world"):
        with pytest.raises(SystemExit):
            get_date(today)

def test_empty_input():
    today = date(2025, 6, 12)
    with patch("builtins.input", return_value=""):
        with pytest.raises(SystemExit):
            get_date(today)
