# My first attempt, I believe
import random # "make" task
secretNum = 42

# secretNum = 42
uInput = 0

while uInput != secretNum:
        math2 = abs(100 - uInput)
        newnumber = int(input("Guess a number between 1 and 100: "))
        math = abs(100 - newnumber)
        if math > math2:
            print("AAAAA")
        else:
            print("BBBBB")
        uInput = newnumber
    
print("Correct! The secret number was", secretNum)


