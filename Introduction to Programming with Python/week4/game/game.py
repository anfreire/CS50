import random

while True:
	try:
		number = input("Level: ")
		number = int(number)
	except ValueError:
		pass
	else:
		if number > 100 or number < 1:
			pass
		else:
			break

answer = random.randint(1, number)

while True:
	try:
		guess = input("Guess: ")
		guess = int(guess)
	except ValueError:
		pass
	else:
		if guess == answer:
			print("Just right!")
			break
		elif guess < answer:
			print("Too small!")
		else:
			print("Too large!")