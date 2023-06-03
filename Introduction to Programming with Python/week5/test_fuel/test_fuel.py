from fuel import convert, gauge
import pytest

def	test_convert_1():
	with pytest.raises(ValueError):
		convert("cat/dog")

def	test_convert_2():
	with pytest.raises(ZeroDivisionError):
		convert("1/0")
	assert convert("3/4") == 75
	assert convert("1/4") == 25
	assert convert("1/100") == 1
	assert convert("99/100") == 99
	assert gauge(1) == "E"
	assert gauge(99) == "F"
	assert gauge(50) == "50%"
