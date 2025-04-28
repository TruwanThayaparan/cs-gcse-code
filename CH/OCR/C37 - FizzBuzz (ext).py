# Challenge 37 - Fizz Buzz (EXTENSION)

num = int(input("Enter a number: "))
base1 = int(input("BASE NUMBER 1: "))
base2 = int(input("BASE NUMBER 2: "))

num = int(input("Enter a number: "))
base1 = int(input("BASE NUMBER 1: "))
base2 = int(input("BASE NUMBER 2: "))

for i in range(1, num + 1):
    if i % base1 == 0 and i % base2 == 0:
        print("FizzBuzz")
    elif i % base1 == 0:
        print("Fizz")
    elif i % base2 == 0:
        print("Buzz")
    else:
        if i > 1:
            is_prime = True
            for j in range(2, int(i**0.5) + 1):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                print("OOPS!")
            else:
                print(i)
        else:
            print("OOPS!")
