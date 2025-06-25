def main():
    message = input("Enter your message: ")
    message = convert(message)
    print(message)

def convert(message):
    message = message.replace(":)","🙂").replace(":(","🙁")
    return message

main()