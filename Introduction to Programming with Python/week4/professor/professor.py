import random

def main():
	i = 0
	score = 0
	trys = 0
	level = get_level()
	x = generate_integer(level)
	y = generate_integer(level)
	while i < 10:
		try:
			print(f"{x} + {y} = ", end="")
			answer = input()
			answer = int(answer)
		except ValueError:
			print("EEE")
			trys = trys + 1
			if trys == 3:
					print(f"{x} + {y} = {x + y}")
					trys = 0
					i = i + 1
		else:
			if answer == (x + y):
				x = generate_integer(level)
				y = generate_integer(level)
				i = i + 1
				score = score + 1
				continue
			else:
				print("EEE")
				trys = trys + 1
			if trys == 3:
				print(f"{x} + {y} = {x + y}")
				trys = 0
				x = generate_integer(level)
				y = generate_integer(level)
				i = i + 1
	print(f"Score: {score}")


def get_level():
	while True:
		try:
			level = input("Level: ")
			level = int(level)
			if level < 1 or level > 3:
				continue
		except ValueError:
			pass
		else:
			return level


def generate_integer(level):
	if level == 1:
		number = random.randint(0, 9)
	elif level == 2:
		number = random.randint(10, 99)
	elif level == 3:
		number = random.randint(100, 999)
	else:
		raise ValueError
	return number


if __name__ == "__main__":
    main()
