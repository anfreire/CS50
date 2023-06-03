import requests
import sys
import json

if len(sys.argv) != 2:
	sys.exit("Missing command-line argument")
try:
	amount = float(sys.argv[1])
	index = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
	index = index.json()
	amount = index["bpi"]["USD"]["rate_float"] * amount
	print(f"${amount:,.4f}")
except requests.RequestException:
    pass
except ValueError:
	sys.exit("Command-line argument is not a number")

