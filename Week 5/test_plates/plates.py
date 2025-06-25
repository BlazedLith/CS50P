def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) > 6 or len(s) < 2:
        return False

    new_s = s[0:2]
    if not(new_s.isalpha()):
        return False

    if not s.isalpha():
        i = -1
        for c in s:
            if c.isnumeric():
                i += 1
                break
            i += 1

        if s[i] == "0":
            return False

        new_s = s[i:]
        if not new_s.isnumeric():
            return False

    if not new_s.isalnum():
        return False

    return True

if __name__ == "__main__":
    main()