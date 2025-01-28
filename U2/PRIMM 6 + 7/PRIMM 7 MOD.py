numberToCheck = int(input("Input a number. "))

result = not( numberToCheck >= 10 )

if result:
    print(result)
    print("NOT(Number greater than 10) = TRUE")
else:
    print(result)
    print("NOT(Number greater than 10) = FALSE")

