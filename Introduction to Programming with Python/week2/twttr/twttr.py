string = input("Input: ")
vocals = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
print("Output: ", end="")
for c in string:
	if c in vocals:
		print("", end="")
	else:
   		print(c, end="")
print("")