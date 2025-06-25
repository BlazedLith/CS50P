greeting = input("Greeting: ")
greeting = greeting.lower()
greet1 = greeting.rfind("hello", 0, 6)
greet2 = greeting.rfind("h", 0, 1)
if greet1 != -1:
    print("$0")
elif greet2 != -1:
    print("$20")
else:
    print("$100")