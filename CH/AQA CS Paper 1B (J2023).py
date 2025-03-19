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
		continue = input("Would you like to roll again?")
		If continue != "yes":
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
