from plates import is_valid

def	test_is_valid():
	assert is_valid("AA") == True
	assert is_valid("22AA") == False
	assert is_valid("A2") == False
	assert is_valid("A") == False
	assert is_valid("22") == False
	assert is_valid("CS50") == True
	assert is_valid("CS05") == False
	assert is_valid("CS50P") == False
	assert is_valid("BIGGERTHAN") == False
	assert is_valid("0TES") == False
	assert is_valid("AA1.1") == False