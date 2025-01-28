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

inputOP = input("[comparison bot]: give me an operator")

if inputOP = "less than":
    lessthan = input1 < input2
elif inputOP = "greater than":
    greaterthan = input1 > input2
else:
    print("unfinished")

'''
elif:
    equalto = input1 == input2
elif:
    lessthanequalto = input1 <= input2
elif:
    greaterthanequalto = input1 >= input2
    '''
