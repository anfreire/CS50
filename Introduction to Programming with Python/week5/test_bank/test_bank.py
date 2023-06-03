from bank import value

def	test_easy():
	assert value("hello") == 0

def test_case():
	assert value("Hello") == 0

def	test_medium():
	assert value("hey") == 20

def	test_case2():
	assert value("Holla") == 20

def	test_hard():
	assert value("teste") == 100

def	test_none():
	assert value("") == 100