# Challenge 8 - Arithmetic test

import random

print("Let's begin the Arithmetic test")
name = input("Before we begin, what is your name? ")
operations = ["plus", "minus", "multiplied by", "divided by"]
correct = 0

for i in range(1, 11):
    operation = random.choice(operations)
    
    if operation == "divided by":
        num2 = random.randint(1, 9)
        answer = random.randint(0, 9)
        num1 = num2 * answer
        calc = answer
    else:
        num1 = random.randint(0, 9)
        num2 = random.randint(0, 9)
        if operation == "plus":
            calc = num1 + num2
        elif operation == "minus":
            calc = num1 - num2
        elif operation == "multiplied by":
            calc = num1 * num2

    question = f"Question {i}: What is {num1} {operation} {num2}? "
    ans = int(input(question))

    if ans == calc:
        print("That's right!")
        correct += 1
    else:
        print(f"Sorry, that is the wrong answer. Answer: {calc}")

print("Here's your score!")
print(f"{correct}/10")
