# Challenge 5 - Fruit Machine
import random
symbols = ["Cherry", "Bell", "Lemon", "Orange", "Star", "Skull"]
credits = 100
print("Welcome to the FRUIT MACHINE!")
       
while True:
  while True:
    print("You have", credits," credits!")
    response = input("Would you like to roll the fruit machine for 20 credits? ").lower()
    if response in ("yes", "no"):
      break
    else:
      print("You must say yes or no.")

  if response == "no": print("Goodbye!"); break

  credits -= 20

  fruit1, fruit2, fruit3 = random.choice(symbols), random.choice(symbols), random.choice(symbols)
  
  print(fruit1, fruit2, fruit3)

  if fruit1 == fruit2 or fruit2 == fruit3 or fruit1 == fruit3:
    if fruit1 == fruit2 and fruit2 == fruit3:
      if fruit1 == "Bell":
        print("You rolled the bell 3 times! You earn 500 credits!")
        credits += 500
      elif fruit1 == "Skull":  
        print("You rolled the skull 3 times! You lose all your credits!")
        credits = 0
      else:
        print("You rolled the same fruit 3 times! You earn 100 credits!")
        credits += 100
    else:
      skulls = [fruit1, fruit2, fruit3].count("Skull")
      if skulls == 2:
        print("You rolled the skull 2 times! You lose 100 credits!")
        credits -= 100
      else:
        print("You rolled the same fruit 2 times! You earn 50 credits!")
        credits += 50
  
  if credits < 20:
    print("Oh no, you do not have enough credits to re-roll (you only have", credits, "). Goodbye!")
    break
