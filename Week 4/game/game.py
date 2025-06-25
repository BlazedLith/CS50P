import random

def get_positive_integer():
    while True:
        try:
            value = int(input())
            if value > 0:
                return value
        except ValueError:
            pass

def main():
    print("Level: ")
    level = get_positive_integer()

    target = random.randint(1, level)

    while True:
        print("Guess: ")
        guess = get_positive_integer()

        if guess < target:
            print("Too small!")
        elif guess > target:
            print("Too large!")
        else:
            print("Just right!")
            break

if __name__ == "__main__":
    main()
