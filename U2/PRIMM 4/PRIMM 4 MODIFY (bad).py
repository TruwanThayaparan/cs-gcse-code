'''
import random # "make" task
secretNum = random.randint(1,100)

# secretNum = 42
uInput = int(input("Guess a number between 1 and 100: "))

while uInput != secretNum:
    if uInput > 100 or uInput < 1:
        uInput = int(input("The number was out of range. Guess another number between 1 and 100:"))
    else:
        uInput = int(input("Incorrect! Guess another number between 1 and 100: "))
    
print("Correct! The secret number was", secretNum)
'''

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


