def is_vowel(c):
    vowel = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    if c in vowel:
        return True
    return False

original = input("Input: ")
new = ""

for c in original:
    if is_vowel(c):
        continue
    else:
        new = new + c
print(f"Output: {new}")

