from bank import value

def test_hello_variants():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HELLO there") == 0

def test_h_only():
    assert value("hi") == 20
    assert value("hey there") == 20
    assert value("Hola") == 20 

def test_non_h():
    assert value("good morning") == 100
    assert value("what's up") == 100
    assert value("yo") == 100

def test_edge_cases():
    assert value("hello!") == 0
    assert value("Hi") == 20
    assert value("he") == 20
