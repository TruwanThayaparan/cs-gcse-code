# Challenge 1 - Factorial Finder

n = int(input("Enter a number... "))

if n < 0:
    print("Factorial is not defined for negative numbers.")
elif n == 0:
    print("1")
else:
    result = 1
    for i in range(1, n + 1):
        result *= i
    print(result)
