import sys
from pyfiglet import Figlet
import random

argv = sys.argv
figlet = Figlet()
fonts = figlet.getFonts()
userFont = 'none'
index = 0

if len(argv) != 1 and len(argv) != 3:
    print("Invalid Usage")
    sys.exit(1)

if len(argv) > 1:
    if argv[1] not in ['-f','--font'] or argv[2] not in fonts:
        print("Invalid Usage")
        sys.exit(1)
    else:
        userFont = argv[2]
else:
    index = randint(0, 549)
    userFont = fonts[index]

text = input("Input: ")

figlet.setFont(font= userFont)

print(figlet.renderText(text))