# Challenge 21
while True:
  try:
    age = int(input("Enter your age: "))
    break
  except ValueError:
    print("You must enter a number!")

if 13 <= age <= 15:
  print("30% discount!")
elif 16 <= age <= 17:
  print("20% discount!")
elif age >= 50:
  print("40% discount!")
else:
  print("No discount.")


# Challenge 22
marks = int(input("Marks you got on the test: "))
print("U" if marks < 10 else "9" if marks == 100 else marks // 10)


# Challenge 23
import math

while True:
  try:
    money_f = float(input("Money you want to change into coins (£): "))
    money = money_f * 100
    break
  except ValueError:
    print("Invalid number entered.")

print("£1, 50p, 20p, 10p, 5p, 2p, 1p")
convert_toi = input("Convert your money into one of the denominations listed above: ").strip()

if convert_toi == "£1":
    convert_to = 100
else:
    convert_to = convert_toi.replace("p", "").replace("P", "").replace("£", "").strip()
    try:
        convert_to = int(convert_to)
    except ValueError:
        pass

if convert_to in (100, 50, 20, 10, 5, 2, 1):
    coins_you_need = money // convert_to
    remaining_money = money % convert_to

    if remaining_money == 0:
        print(f"With {convert_toi} coins, you would need {coins_you_need} coins to make £{money_f}.")
    else:
        print(f"With {convert_toi} coins, you would need {coins_you_need} coins to make £{money_f}, but there would be {remaining_money}p left unaccounted for.")
else:
    print("Invalid coin denomination entered.")


# Challenge 24
import random

possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)

user_action = None
while user_action not in possible_actions:
    user_action = input("Rock, paper, scissors - choose: ").lower()
    if user_action not in possible_actions:
        print("Not a valid choice.")

print(f"You chose {user_action} and computer chose {computer_action}.")
if (computer_action == "rock" and user_action == "scissors") or \
   (computer_action == "paper" and user_action == "rock") or \
   (computer_action == "scissors" and user_action == "paper"):
    print("Computer Wins")
elif computer_action == user_action:
    print("There was a tie.")  # added this since otherwise it would be silly
else:
    print("You Win!")


# Challenge 26
while True:
  try:
    age = int(input("Age of the dog: "))
    break
  except ValueError:
    print("Invalid age!")
              
if age <= 2:
  print(f"Human equivalent: {age * 12} years old [dog age * 12]")
else:
  print(f"Human equivalent: {24 + 6 * (age - 2)} years old [24 for the first 2 years + 6 for each additional year]")




# Challenge 27
while True:
  try:
    passengers = int(input("Passengers: "))
    break
  except ValueError:
    print("You must enter a whole number!")


while True:
  try:
    distance = int(input("Distance to nearest whole number (km): "))
    break
  except ValueError:
    print("You must enter a whole number!")

price = 3 
if distance > 1: price += 2 * (distance - 1)
  
if passengers >= 5:
  price *= 1.5

print(f"The price of the trip is £{price}.")
