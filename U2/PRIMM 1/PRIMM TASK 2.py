a = int(input("Enter a number:"))
b = int(input("Enter a second number:"))

c = a + b
print(a," plus ",b," equals ",c,".")

checkmode = input("Mode:")

a = int(input("Enter a number:"))
b = int(input("Enter a second number:"))

if checkmode == "addition" or "add":
    c = a + b
    print(a," plus ",b," equals ",c,".")
elif checkmode == "subtraction" or "subtract":
    c = a - b
    print(a," subtracted by ",b," equals ",c,".")
elif checkmode == "multiplication" or "multiply":
    c = a * b
    print(a," mutiplied by ",b," equals ",c,".")
elif checkmode == "real division" or "real divide":
    c = a / b
    print(a," real divided by ",b," equals ",c,".")
elif checkmode == "integer division" or "integer divide":
    c = a // b
    print(a," integer divided by ",b," equals ",c,".")
elif checkmode == "modulo" or "modulus":
    c = a % b
    print(a," modulo divided by ",b," equals ",c,".")
else:
    print("ERROR: Invalid mode.")


checkmode = input("Shape:")

# 1/2 * b * h
if thisdamnshape == "triangle":
    base = int(input("Base of triangle:"))
    height = int(input("Height of triangle:"))
    area = 1/2 * base * height
else:
    print("error")
