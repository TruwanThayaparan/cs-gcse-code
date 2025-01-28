# import random # "make" task
# secretNum = random.randint(1,100)

secretNum = 42
uInput = int(input("Guess a number between 1 and 100: "))

while uInput != secretNum:
    if uInput > 100 or uInput < 1: # Or you could use two seperate conditions, if you want to give two different error messages.
        uInput = int(input("The number was out of range. Guess another number between 1 and 100:"))
    else:
        uInput = int(input("Incorrect! Guess another number between 1 and 100: "))
    
print("Correct! The secret number was", secretNum)
