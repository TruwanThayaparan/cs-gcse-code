# Challenge 18 - Years in a Range
syear = int(input("Starting year: "))
eyear = int(input("Ending year: "))

for year in range(syear, eyear + 1):
    year_str = str(year)
    for digit in year_str:
        if year_str.count(digit) > 1:
            print(year)
            break
