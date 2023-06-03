x, y, z = input("Expression: ").split(" ")
if (y == "+"):
	print(f"{int(x) + int(z):.1f}")
elif (y == "*"):
	print(f"{int(x) * int(z):.1f}")
elif (y == "-"):
	print(f"{int(x) - int(z):.1f}")
elif (y == "/"):
	print(f"{(int(x) / int(z)):.1f}")