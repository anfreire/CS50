import re

def main():
	print(count(input("Text: ")))

def count(s):
	matches = re.findall(r'(?:\W|^)(um)(?:\W|$)', s, re.I)
	return len(matches)

if __name__ == "__main__":
	main()
