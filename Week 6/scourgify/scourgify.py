import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

filename = sys.argv[1]
newfile = sys.argv[2]
students = []
fixed = []

try:
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append(row)
except FileNotFoundError:
    sys.exit("File does not exist")

if not filename.endswith(".csv"):
    sys.exit("Not a CSV file")

for row in students:
    last,first = row['name'].split(',')
    first = first.strip()
    last = last.strip()
    house = row['house']
    fixed.append({'first': first, 'last': last, 'house': house})

try:
    with open(newfile, 'w', newline='') as csvfile:
        fieldnames = ['first', 'last', 'house']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for row in fixed:
            writer.writerow(row)
except FileNotFoundError:
    sys.exit("Error creating file")
