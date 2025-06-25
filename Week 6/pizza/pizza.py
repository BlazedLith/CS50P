import sys
import csv
import tabulate

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

filename = sys.argv[1]
pizzas = []

try:
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            pizzas.append(row)
except FileNotFoundError:
    sys.exit("File does not exist")

if not filename.endswith(".csv"):
    sys.exit("Not a CSV file")

print(tabulate.tabulate(pizzas, headers = "keys", tablefmt = "grid"))
