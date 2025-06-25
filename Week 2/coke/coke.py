due = 50
change = 0
while True:
    print(f"Amount Due: {due}")
    coin = int(input("Insert Coin: "))

    if coin == 25:
        due -= 25
    elif coin == 10:
        due -= 10
    elif coin == 5:
        due -= 5

    if due <= 0:
        change = -1 * due
        print(f"Change Owed: {change}")
        break
