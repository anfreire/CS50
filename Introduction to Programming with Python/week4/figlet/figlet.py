from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
list_fonts = figlet.getFonts()
argv_1 = ["-f", "--fonts"]

if len(sys.argv) == 3:
	if sys.argv[1] not in argv_1:
		sys.exit("Invalid usage")
	if sys.argv[2] not in list_fonts:
		sys.exit("Invalid usage")
	font_f = sys.argv[2]
elif len(sys.argv) == 1:
	font_f = random.choice(list_fonts)

figlet.setFont(font=font_f)

s = input("Input: ")
print(figlet.renderText(s))






