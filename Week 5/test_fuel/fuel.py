def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percent = convert(fraction)
            print(gauge(percent))
            break
        except (ValueError, ZeroDivisionError):
            continue


def convert(fraction):
    try:
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)
    except (ValueError, AttributeError):
        raise ValueError("X and Y must be integers in format X/Y")

    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero")

    if x > y:
        raise ValueError("Numerator cannot be greater than denominator")

    return round((x / y) * 100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
