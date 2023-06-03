var = input("camelCase: ")
b00l = -1
print("snake_case: ", end="")
if var.isalpha():
	for	c in var:
		if c >= 'A' and c <= 'Z' and b00l == 0:
			print("_" + c.lower(), end="")
			b00l = 1
		else:
			print(c.lower(), end="")
			b00l = 0
	print()
