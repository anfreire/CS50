import string

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
	l_alpha = list(string.ascii_uppercase)
	l_digits = list(string.digits)
	if s[0] == '0':
		return False
	if len(s) < 2 or len(s) > 6:
		return False
	if s[0] not in l_alpha:
		return False
	if s[1] not in l_alpha:
		return False
	i = 0
	while (i < len(s)):
		if s[i] not in l_alpha and s[i] not in l_digits:
			return False
		i = i + 1
	b00l = 0
	while (i > 0):
		if s[i - 1] in l_digits and b00l == 0:
			b00l = 1
		if s[i - 1] in l_alpha and (b00l == 0 or b00l == 1):
			if b00l == 1:
				if s[i] == '0':
					return False
			b00l = 2
		if s[i - 1] in l_digits and b00l == 2:
			return False
		i = i - 1
	else:
		return True

if __name__ == "__main__":
    main()
