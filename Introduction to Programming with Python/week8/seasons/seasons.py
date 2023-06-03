from datetime import date, timedelta
import inflect
import sys

def	get_minutes(str):
		try:
			year, month, day = str.split('-')
			year = int(year)
			month = int(month)
			day = int(day)
			birthay = date(year, month, day)
			today = date.today()
			delta = timedelta
			delta = today - birthay
			delta = round(delta.total_seconds() / 60)
			delta = inflect.engine().number_to_words(delta, andword="")
			delta = delta.capitalize()
		except:
			sys.exit("Invalid date")
		else:
			return delta + " minutes"


def main():
	str = input("Date of Birthay: ")
	print(get_minutes(str))


if __name__ == "__main__":
	main()
