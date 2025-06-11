# final question
import random
score = 0
while True:
	dice1 = random.randint(1,6)
	dice2 = random.randint(1,6)
	total = dice1 + dice2
	score += total
	print("Dice 1:", dice1)
	print("Dice 2:", dice2)
	print("Current score:", score)
	if score < 21:
		keepGoing = input("Would you like to roll again?")
		if keepGoing != "yes":
			break
	else:
		break

if score == 21:
	print("You won!")
elif score > 21:
	print("You lost!")
else:
	if random.randint(15, 21) > score:
		print("You lost!")
	else:
		print("You won!")

while True:
    try:
        total_bill = float(input("Enter the total amount of the bill: "))
        break
    except ValueError:
        print("You must enter a number!")

payment_left = total_bill


while payment_left > 0:
    while True:
        try:
            person_is_paying = float(input("How much will you pay: "))
            break
        except ValueError:
            print("You must enter a number!")
    
    payment_left = round(payment_left - person_is_paying, 2)
    
    if payment_left > 0:
        print(f"Payment left: £{payment_left}")
    elif payment_left == 0:
        print("Bill paid")
        break
    else:  
        print(f"Tip is: £{abs(payment_left)}")
        break  
