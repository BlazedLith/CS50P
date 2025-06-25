from plates import is_valid

def test_length():
    assert is_valid("CS") == True
    assert is_valid("C") == False
    assert is_valid("ABCDEFG") == False

def test_starting_letters():
    assert is_valid("CS50") == True
    assert is_valid("50CS") == False
    assert is_valid("1CDE") == False


def test_middle_numbers():
    assert is_valid("CS05") == False
    assert is_valid("CS50") == True
    assert is_valid("CS5O0") == False

def test_punctuation_and_symbols():
    assert is_valid("CS 50") == False
    assert is_valid("CS.50") == False
    assert is_valid("CS!50") == False
    assert is_valid("CS-50") == False

def test_valid_cases():
    assert is_valid("HELLO") == True
    assert is_valid("OUTLAW") == True

def test_invalid_starting_characters():
    assert is_valid("C") == False
    assert is_valid("1CS50") == False
    assert is_valid("C150") == False
    assert is_valid("5S") == False