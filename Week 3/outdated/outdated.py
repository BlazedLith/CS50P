# outdated.py

months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

def get_valid_date():

    while True:
        date_str = input("Date: ").strip()

        try:
            if "/" in date_str:

                parts = date_str.split("/")
                if len(parts) != 3:
                    raise ValueError
                month, day, year = map(int, parts)

            elif "," in date_str:

                month_str, rest = date_str.split(" ", 1)
                day_str, year_str = rest.split(",")
                month = months.index(month_str) + 1
                day = int(day_str.strip())
                year = int(year_str.strip())

            else:

                raise ValueError

            if not (1 <= month <= 12 and 1 <= day <= 31):

                raise ValueError

            return f"{year:04}-{month:02}-{day:02}"

        except (ValueError, IndexError):
            pass

if __name__ == "__main__":
    print(get_valid_date())
