import pytest
from seasons import get_minutes

def	test_1():
	with pytest.raises(SystemExit):
		get_minutes("January 12, 10")