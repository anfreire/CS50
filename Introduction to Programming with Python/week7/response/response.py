from validator_collection import validators, checkers, errors

email = input("What's your email address? ")

try:
	awnser = validators.email(email)
except:
	print("Invalid")
else:
	print("Valid")