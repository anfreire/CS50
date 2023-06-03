import csv
import sys

if len(sys.argv) > 3:
	sys.exit("Too many command-line arguments")
elif len(sys.argv) < 3:
	sys.exit("Too few command-line arguments")
try:
	students = []
	with open(sys.argv[1]) as file:
		reader = csv.DictReader(file)
		for row in reader:
			students.append({"name": row["name"],
			 "house": row["house"]})
except FileNotFoundError:
	sys.exit(f"Could not read {sys.argv[1]}")

with open(sys.argv[2], "w") as file:
	fieldnames = ['first', 'last', 'house']
	writer = csv.DictWriter(file, fieldnames=fieldnames)

	writer.writeheader()
	for row in students:
		last, first = row["name"].split(',')
		house = row["house"]
		first = first.strip()
		writer.writerow({'first': first, 'last': last,
		 'house': house})
