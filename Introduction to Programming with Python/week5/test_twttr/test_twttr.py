from twttr import shorten

def	test_easy():
	assert shorten("teste") == "tst"

def	test_medium():
	assert shorten("pAlavrA") == "plvr"

def	test_hard():
	assert shorten("DiffIcUlt") == "Dffclt"

def	test_pontuation():
	assert shorten("...") == "..."

def	test_numbers():
	assert shorten("190") == "190"