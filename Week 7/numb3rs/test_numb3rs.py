import pytest
from numb3rs import validate

def test_valid_ips():
    assert validate("192.168.1.1") == True
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("127.0.0.1") == True

def test_invalid_format():
    assert validate("192.168.1") == False
    assert validate("192.168.1.1.1") == False
    assert validate("192.168.1.one") == False
    assert validate("hello.world") == False
    assert validate("") == False

def test_out_of_range():
    assert validate("256.0.0.1") == False
    assert validate("192.168.300.1") == False
    assert validate("192.168.-1.1") == False
    assert validate("999.999.999.999") == False

def test_leading_zeroes():
    assert validate("01.02.03.04") == True
    assert validate("001.002.003.004") == True
