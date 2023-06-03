months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def	get_date():
	while True:
		try:
			date = input("Date: ")
			numbers = date.split('/', maxsplit=2)
			normal = date.split(' ', maxsplit=2)
			if len(numbers) == 3:
				numbers[0] = int(numbers[0])
				numbers[1] = int(numbers[1])
				numbers[2] = int(numbers[2])
				if numbers[1] <= 31 and numbers[0] <= 12:
					return numbers
			elif len(normal) == 3:
				normal[0] = months.index(normal[0]) + 1
				normal[2] = int(normal[2])
				b00l = normal[1].find(',')
				normal[1] = normal[1].rstrip(',')
				normal[1] = int(normal[1])
				if normal[1] <= 31 and normal[0] <= 12 and b00l == True:
					return normal
		except (ValueError, KeyError):
			pass

date = get_date()
print(f"{date[2]:04}-{date[0]:02}-{date[1]:02}")