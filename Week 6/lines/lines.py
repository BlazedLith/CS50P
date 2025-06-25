import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

filename = sys.argv[1]
count = 0

if not filename.endswith(".py"):
    sys.exit("Not a Python file")

try:
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            elif line.startswith("#"):
                continue
            count = count + 1
except FileNotFoundError:
    sys.exit("File does not exist")


print(count)
