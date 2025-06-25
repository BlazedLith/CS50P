import sys
import os
from PIL import Image, ImageOps

valid_extensions = ('.jpg', '.jpeg', '.png')

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

input_file = sys.argv[1]
output_file = sys.argv[2]

if not input_file.lower().endswith(valid_extensions):
    sys.exit("Invlid Input")
if not output_file.lower().endswith(valid_extensions):
    sys.exit("Invlid Output")

if os.path.splitext(input_file)[1].lower() != os.path.splitext(output_file)[1].lower():
    sys.exit("Input and output have different extensions")

try:
    image = Image.open(input_file)
except FileNotFoundError:
    sys.exit("Input does not exist")

shirt = Image.open('shirt.png')
size = shirt.size
image = ImageOps.fit(image, size)
image.paste(shirt, (0,0), shirt)
image.save(output_file)
