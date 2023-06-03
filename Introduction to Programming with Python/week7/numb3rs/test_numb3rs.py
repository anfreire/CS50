import pytest
from numb3rs import validate

def test_true():
	assert validate("1.1.1.1") == True

def test_another():
	assert validate("cat") == False

def test_one():
	assert validate("257.257.257.257") == False

def test_two():
	assert validate("2001:0db8:85a3:0000:0000:8a2e:0370:7334") == False

def test_three():
	assert validate("75.456.76.65") == False