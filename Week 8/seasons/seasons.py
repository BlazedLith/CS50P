from datetime import date,datetime
import inflect
import sys


def main():
    p = inflect.engine()
    td = date.today()
    dob = get_date(td)
    age = ((td - dob).days * 60 * 24)
    age = p.number_to_words(age, andword="")
    print(age.capitalize() + " minutes")

def get_date(td):
    try:
        dob = input("Date of Birth: ")
        dob = datetime.strptime(dob, "%Y-%m-%d").date()
        if dob > td:
            raise ValueError
    except (TypeError,ValueError):
        sys.exit("Invalid Date")
    return dob



if __name__ == "__main__":
    main()
