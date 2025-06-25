import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    matches = re.search(r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$", ip)

    if not matches:
        return False

    count = 1

    try:
        while count <= 4:
            number = int(matches.group(count))
            if number < 0 or number > 255:
                return False
            count += 1
    except ValueError:
        return False

    return True


if __name__ == "__main__":
    main()
