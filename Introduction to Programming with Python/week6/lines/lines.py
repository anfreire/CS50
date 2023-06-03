import sys
import string

if len(sys.argv) == 1:
	sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
	sys.exit("Too many command-line arguments")
if sys.argv[1][-3:] != ".py":
	sys.exit("Not a Python file")
try:
	i = 0
	with open(sys.argv[1]) as file:
		for line in file:
			if line == '\n':
				i = i
			elif line.strip().startswith("#"):
				i = i
			elif line.isspace():
				i = i
			else:
				i = i + 1
except FileNotFoundError:
	sys.exit("File does not exist")
print(i)

