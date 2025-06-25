while True:
    fraction = input("Fraction: ")
    fraction = fraction.split("/")

    try:
        x = int(fraction[0])
        y = int(fraction[1])
    except ValueError:
        print("x or y is not an integer")
        continue


    try:
        r = (x / y) * 100
    except ZeroDivisionError:
        print("You can't divide by zero")
    else:
        r = round(r)
        if x > y:
            print("numerator is greater than denominator")
            continue

        if r >= 99:
            print("F")
            break
        elif r <= 1:
            print("E")
            break
        else:
            print(f"{r}%")
            break