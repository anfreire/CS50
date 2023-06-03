import pytest

from um import count

def test_1():
	assert count("Um, dois, um") == 2

def test_2():
	assert count("um, dois, yummy") == 1

def test_3():
	assert count("....UM dois, um    ") == 2

def test_4():
	assert count("  um    ") == 1

def test_5():
	assert count("  yummy    ") == 0