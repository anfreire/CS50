my_list = {}
while True:
	try:
		item = input().upper()
		if item in my_list:
			my_list[item] = my_list[item] + 1
		else:
			my_list[item] = 1
	except (EOFError, KeyboardInterrupt):
		print()
		for item in sorted(my_list):
			print(f"{my_list[item]} {item}")
		break
	except KeyError:
		pass