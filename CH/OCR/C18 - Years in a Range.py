# Challenge 18 - Years in a Range

while True:
    try:
        syear = int(input("Starting year: "))
        break
    except ValueError:
        print("You must enter a number.")

while True:
    try:
        eyear = int(input("Ending year: "))
        break
    except ValueError:
        print("You must enter a number.")

for year in range(syear, eyear + 1):
    year_str = str(year)
    for digit in year_str:
        if year_str.count(digit) > 1:
            print(year)
            break
