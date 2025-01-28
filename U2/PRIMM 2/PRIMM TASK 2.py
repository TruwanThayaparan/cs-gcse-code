# Task 2

# Run
a = 1
b = 100

print("Comparison of numbers 1 and 100 (where 1 is () to 100)")
print("LESS THAN:", a < b)

# Modify
print("GREATER THAN:", a > b)

print("EQUAL TO:", a == b)

print("LESS THAN OR EQUAL TO:", a <= b)
print("GREATER THAN OR EQUAL TO:", a >= b)

print("\n\n\n")
# Make
input1 = input("[comparison bot]: give me a input")
input2 = input("[comparison bot]: give me another input")

print("Comparison of inputted numbers ",input1," and ",input2," (where input1 is () to input2)")
lessthan = input1 < input2
greaterthan = input1 > input2
equalto = input1 == input2
lessthanequalto = input1 <= input2
greaterthanequalto = input1 >= input2

print(lessthan); print(greaterthan); print(equalto); print(lessthanequalto); print(greaterthanequalto)

# I'm not sure what I was trying to do here.
inputOP = input("[comparison bot]: give me an operator")

if inputOP = "less than" or inputOP = "<":
    lessthan = input1 < input2
elif inputOP = "greater than" or inputOP = ">":
    greaterthan = input1 > input2
elif inputOP = "equal to" or inputOP = "=" or inputOP = "==":
    equalto = input1 == input2
elif inputOP = "less than or equal to" or inputOP = "<=":
    lessthanequalto = input1 <= input2
elif inputOP = "greater than or equal to" or inputOP = ">=":
    greaterthanequalto = input1 >= input2
else:
    print("Invalid.")
