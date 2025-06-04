# Challenge 34 - What's the day?
import datetime

# day
while True:
    try:
        day = int(input("Enter a day: "))
        if 1 <= day <= 31:
            break
        print("You must enter a number between 1 and 31.")
    except ValueError:
        print("You must enter a number.")

# month
while True:
    try:
        month = int(input("Enter a month: "))
        if 1 <= month <= 12:
            break
        print("You must enter a number between 1 and 12.")
    except ValueError:
        print("You must enter a number.")

# year
while True:
    try:
        year = int(input("Enter a year: "))
        break
    except ValueError:
        print("You must enter a number.")

# check
try:
    date = datetime.date(year, month, day)
    print(f"The date {date.strftime('%d-%m-%Y')} is a {date.strftime('%A')}.")
except ValueError:
    print("The date you entered is not valid.")
