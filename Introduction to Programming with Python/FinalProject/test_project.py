import pytest
from project import *

def test_validate_option():
	empyt_list = []
	with pytest.raises(ValueError):
		validate_option(empyt_list)

def test_validate_period():
	empty_int = int()
	empty_str = str()
	with pytest.raises(ValueError):
		validate_period(empty_int, empty_str)

def test_proceed_results():
	with pytest.raises(ValueError):
		proceed_results("123", "test")

