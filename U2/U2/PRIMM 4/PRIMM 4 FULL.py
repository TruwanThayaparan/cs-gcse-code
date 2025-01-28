secretNum = 42
uInput = int(input("Guess a number between 1 and 100: "))

while uInput != secretNum:
    uInput = int(input("Incorrect! Guess another number between 1 and 100: "))
    
print("Correct! The secret number was", secretNum)
