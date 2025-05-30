# Challenge 16 - Kaprekar

import math

while True:
    try:
        kap = int(input("Enter a number: "))
        break
    except ValueError:
        print("You must enter a number.")

kap_squared = str(kap ** 2)
d = len(str(kap))

left = kap_squared[:-d] or '0' # Avoid empty string
right = kap_squared[-d:]

kap_add = int(left) + int(right)
print(f"Square of {kap} is {kap_squared}")
print(f"Left part: {left}, Right part: {right}, Sum: {kap_add}")

if kap_add == kap:
    print(f"{kap} is a Kaprekar number.")
else:
    print(f"{kap} is not a Kaprekar number.")
