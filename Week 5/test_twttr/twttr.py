def main():
    original = input("Input: ")
    print(f"Output: {shorten(original)}")


def is_vowel(c):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    return c in vowels


def shorten(word):
    new = ""
    for c in word:
        if not is_vowel(c):
            new += c
    return new


if __name__ == "__main__":
    main()

