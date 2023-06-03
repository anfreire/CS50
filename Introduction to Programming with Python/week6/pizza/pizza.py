import csv
import sys
from tabulate import tabulate

pizzas = []

if len(sys.argv) < 2:
	sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
	sys.exit("Too many command-line arguments")
elif sys.argv[1][-4:] != ".csv":
	sys.exit("Not a CSV file")

try:
	with open(sys.argv[1]) as file:
		reader = csv.reader(file)
		for row in reader:
			pizzas.append({"Regular Pizza": row[0],
			 "Small": row[1], "Large": row[2]})
		print(tabulate(pizzas, headers="firstrow", tablefmt="grid"))
except FileNotFoundError:
	sys.exit("File does not exist")
