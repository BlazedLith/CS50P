grocery = {}

while True:
    try:
        item = input().upper()
    except EOFError:
        break

    if item in grocery:
        grocery[item] += 1
    else:
        grocery.update({item: 1})
print()

sorted_keys = sorted(grocery)

for i in sorted_keys:
    print(f"{grocery[i]} {i}")