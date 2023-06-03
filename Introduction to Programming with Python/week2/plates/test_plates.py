from plates import is_valid

def	test_first_two_letters_f():
	assert is_valid("22AA") == False

def	test_first_two_letters_T():
	assert is_valid("AAA222") == True

def	test_toobig():
	assert is_valid("AAA2222") == False

def	test_toosmall():
	assert is_valid("A") == False

def	test_numbers_middle():
	assert is_valid("AAA22A") == False

def	test_lowercase():
	assert is_valid("aaa222") == False

def	test_space():
	assert is_valid("AAA ") == False

def	test_period():
	assert is_valid("AAA.") == False

def	test_ponct():
	assert is_valid("AA!A") == False