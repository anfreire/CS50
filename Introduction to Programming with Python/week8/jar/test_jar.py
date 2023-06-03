from jar import Jar
import pytest

def test_str():
	jar = Jar()
	assert str(jar) == ""
	jar.deposit(1)
	assert str(jar) == "🍪"
	jar.deposit(11)
	assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
	jar = Jar(10)
	assert str(jar) == ""
	jar.deposit(2)
	assert str(jar) == "🍪🍪"
	with pytest.raises(ValueError):
		jar.deposit(11)


def test_2():
	jar = Jar(4)
	with pytest.raises(ValueError):
		jar.deposit(5)

def test_withdraw():
	jar = Jar(12)
	assert str(jar) == ""
	jar.deposit(2)
	assert str(jar) == "🍪🍪"
	jar.withdraw(2)
	assert str(jar) == ""
	with pytest.raises(ValueError):
		jar.withdraw(2)
