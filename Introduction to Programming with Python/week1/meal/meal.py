def main():
	time = input("What time is it? ").strip()
	time = convert(time)
	if time >= 7.0 and time <= 8.0:
		print("breakfast time")
	elif time >= 12.0 and time <= 13.0:
		print("lunch time")
	elif time >= 18.0 and time <= 19.0:
		print("dinner time")

def convert(time):
	hours, minutes = time.split(":")
	hours = float(hours)
	minutes = float(minutes) * 60 / 10000
	return hours + minutes

if __name__ == "__main__":
	main()

