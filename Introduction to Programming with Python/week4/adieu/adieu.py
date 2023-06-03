import inflect
import sys

p = inflect.engine()
myList = []
while True:
	try:
		myList.append(input("Name: "))
	except EOFError:
		print("\nAdieu, adieu, to ", end="")
		myString = p.join((myList))
		print(myString)
		break