import random


def main():
    level = get_level()
    count = 1
    incorrect_count = 0
    score = 0
    while count <= 10:
        incorrect_count = 0
        a = generate_integer(level)
        b = generate_integer(level)
        while True:
            try:
                answer = int(input(str(a) + " + " + str(b) + " = "))
                if answer == (a + b):
                    count = count + 1
                    score = score + 1
                    break
                else:
                    incorrect_count = incorrect_count + 1
                    print("EEE")
                    if incorrect_count == 3:
                        count = count + 1
                        print(str(a) + " + " + str(b) + " = " + str(a + b))
                        break
            except ValueError:
                incorrect_count = incorrect_count + 1
                print("EEE")
                if incorrect_count == 3:
                        count = count + 1
                        print(str(a) + " + " + str(b) + " = " + str(a + b))
                        break
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level >= 1 and level <= 3:
                return level
        except ValueError:
            pass


def generate_integer(level):
    ranges = {1: (0, 9), 2: (10, 99), 3: (100, 999)}
    a,b = ranges [level]
    integer = random.randint(a,b)
    return integer


if __name__ == "__main__":
    main()