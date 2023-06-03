inserted = 0
while True:
	if inserted >= 50:
		break
	print(f"Amount Due: {50 - inserted}")
	coins = int(input("Insert Coins: "))
	if coins == 25 or coins == 10 or coins == 5:
		inserted += coins
print(f"Change Owed: {inserted - 50}")