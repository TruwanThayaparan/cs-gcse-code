# Factorial Finder [Challenge 1]

n = int(input("Enter a number... "))

for i in range(n - 1, 0, -1):
    n = n * i

if n == 0:
    print("1")
else:
    print(n)
