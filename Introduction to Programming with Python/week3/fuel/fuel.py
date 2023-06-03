def get_fraction():
	while True:
		try:
			portions = input("Fraction: ").split('/', maxsplit=1)
			division = int(portions[0]) / int(portions[1])
		except (ValueError, ZeroDivisionError):
			pass
		else:
			if division <= 1:
				return "{:.0%}".format(division)

percentage = get_fraction()
if percentage == "100%" or percentage == "99%":
	print("F")
elif percentage == "0%" or percentage == "1%":
	print("E")
else:
	print(percentage)
