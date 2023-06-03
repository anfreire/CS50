import working
import pytest

def test_1():
	assert working.convert("9 AM to 10 PM") == "09:00 to 22:00"

def test_2():
	assert working.convert("9:00 PM to 10:45 PM") == "21:00 to 22:45"

def test_3():
	with pytest.raises(ValueError):
		working.convert("0 AM to 9:60 PM")

def test_4():
	with pytest.raises(ValueError):
		working.convert('11"0')

def test_5():
	with pytest.raises(ValueError):
		working.convert("10:10 to 10:30")