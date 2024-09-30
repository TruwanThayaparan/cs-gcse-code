# FizzBuzz.py
# Print all numbers from 1 to the finishing number assigned to variable num by input...
# But numbers divisible by 3 print Fizz instead, numbers divisible by 5 print Buzz and numbers divisible by 3 and 5 print FizzBuzz.

num = int(input("Enter a number: "))

for i in range(1, num + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
