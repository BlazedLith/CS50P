import sys
from validators import email

mail = input("What's your email address? ")
if not email(mail):
    print("Invalid")
    sys.exit()

print("Valid")
