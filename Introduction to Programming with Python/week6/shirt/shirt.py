import sys
from PIL import Image
from PIL import ImageOps
from os import path

if len(sys.argv) > 3:
	sys.exit("Too many command-line arguments")
elif len(sys.argv) < 3:
	sys.exit("Too few command-line arguments")

try:
	before = Image.open(sys.argv[1])
	shirt = Image.open("shirt.png")
except FileNotFoundError:
	sys.exit("Input does not exist")

if path.splitext(sys.argv[1])[1] != path.splitext(sys.argv[2])[1]:
	sys.exit("Input and output have different extensions")


before = ImageOps.fit(
	before, shirt.size,
	method=Image.Resampling.BICUBIC,
	bleed=0.0, centering=(0.5, 0.5)
)
before.paste(shirt, (0, 0), shirt)
before.save(sys.argv[2])

