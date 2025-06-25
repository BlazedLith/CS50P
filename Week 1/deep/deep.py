answer = input("What is the Answer to the Great Question of Life, the Universe and Everything? ")
answer = answer.lower().replace(" ", "").replace("-","")
if answer == "42" or answer == "fortytwo":
    print("Yes")
else:
    print("No")