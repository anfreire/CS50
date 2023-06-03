import re

def main():
    print(convert(input("Hours: ")), end="")


def convert(s):
	return first_parsing(s)

def first_parsing(string):
		try:
			groups = re.search(r'(\d+\:?\d*) (A?P?M) to (\d+:?\d*) (A?P?M)', string)
			if groups:
				first_hour = str(groups.group(1))
				second_hour = str(groups.group(3))
				first_M = groups.group(2)
				second_M = groups.group(4)
				hours = []
				hours = first_hour.split(':')
			if len(hours) == 1:
				hours.append("00")
			tmp = second_hour.split(':')
			if len(tmp) == 1:
				hours.append(tmp[0])
				hours.append("00")
			elif len(tmp) == 2:
				hours.append(tmp[0])
				hours.append(tmp[1])

			if first_M[0] == 'P':
				if int(hours[0]) == 12:
					f_hour = "12"
				else:
					f_hour = int(hours[0]) + 12
			elif first_M[0] == 'A':
				if int(hours[0]) == 12:
					f_hour = "00"
				else:
					f_hour = hours[0]

			if int(f_hour) < 0 or int(f_hour) > 23:
				raise ValueError
			if second_M[0] == 'P':
				if int(hours[2]) == 12:
					s_hour = "12"
				else:
					s_hour = int(hours[2]) + 12
			elif second_M[0] == 'A':
				if int(hours[2]) == 12:
					s_hour = "00"
				else:
					s_hour = hours[2]
			if int(s_hour) < 0 or int(s_hour) > 23:
				raise ValueError
			if int(hours[1]) > 59 or int(hours[1]) < 0 or int(hours[3]) > 59 or int(hours[3]) < 0:
				raise ValueError

			first_s = f"{f_hour}:{hours[1]}"
			second_s = f"{s_hour}:{hours[3]}"
			if len(str(f_hour)) == 1 and len(str(s_hour)) == 1:
				return (f"0{first_s} to 0{second_s}")
			elif len(str(f_hour)) == 1:
					return (f"0{first_s} to {second_s}")
			elif len(str(s_hour)) == 1:
					return (f"{first_s} to 0{second_s}")
			else:
				return (f"{first_s} to {second_s}")
		except:
			raise ValueError




if __name__ == "__main__":
    main()

