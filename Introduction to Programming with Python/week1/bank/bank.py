answer = input("Greeting:").strip()
if answer.startswith("Hello") or answer.startswith("hello"):
	print("$0")
elif answer.startswith("h") or answer.startswith("H"):
	print("$20")
else:
	print("$100")