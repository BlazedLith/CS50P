import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$"
    match = re.search(pattern, s)

    if not match:
        raise ValueError("Invalid format")

    h1, m1, am_pm1, h2, m2, am_pm2 = match.groups()

    h1, h2 = int(h1), int(h2)
    m1 = int(m1) if m1 is not None else 0
    m2 = int(m2) if m2 is not None else 0

    if not (1 <= h1 <= 12 and 0 <= m1 <= 59 and 1 <= h2 <= 12 and 0 <= m2 <= 59):
        raise ValueError("Invalid time")

    start = _to_24_hour(h1, m1, am_pm1)
    end = _to_24_hour(h2, m2, am_pm2)

    return f"{start} to {end}"


def _to_24_hour(hour, minute, period):
    if period == "AM":
        if hour == 12:
            hour = 0
    elif period == "PM":
        if hour != 12:
            hour += 12
    return f"{hour:02}:{minute:02}"


if __name__ == "__main__":
    main()
