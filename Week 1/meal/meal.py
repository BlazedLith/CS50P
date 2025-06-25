def main():
    time = input("What time is it? ")
    time = convert(time)
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12<= time <= 13:
        print("lunch time")
    elif 18<= time <= 19:
        print("dinner time")

def convert(time):
    time = time.strip().split(":")
    hours = float(time[0].strip())
    time2 = time[1].strip().split(" ")
    minutes = float(time2[0].strip())
    if len(time2) != 1:
        meridiem = time2[1].strip().lower()
        if meridiem == "am":
            if hours == 12:
                hours = 0
        elif meridiem == "pm":
            if hours != 12:
                hours = hours + 12
    time = hours + (minutes/60)
    return time


if __name__ == "__main__":
    main()