num = int(input("Start number: "))
num2 = int(input("End number: "))

#print(num)
#print(num2)

while num < num2:
    if not num % 5 == 0 and num % 3 == 0:
        print("Fizz")

    if num % 5 == 0 and not num % 3 == 0:
        print("Buzz")

    if num % 5 == 0 and num % 3 == 0:
        print("Fizz Buzz")

    if not num % 5 == 0 and not num % 3 == 0:
        print(num)

    num = num + 1



print("Done!")

'''
    if not type(num / 5) == "int" and type(num / 3) == "int":
        print("Fizz")
    if type(num / 3) == "int" and not type(num / 5) == "int":
        print("Buzz")
    if type(num / 5) == "int" and type(num / 3) == "int":
        print("Fizz Buzz")
    if not type(num / 5) == "int" and not type(num / 3) == "int":
        print(num)

num = num + 1
'''
