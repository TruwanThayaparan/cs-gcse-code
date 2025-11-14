# Python versions of the answers (Challenge 1 to Challenge 19)

# Difficulty 1
# C1
name = input("Enter your name: ")
age = int(input("Enter your age: "))
fav_colour = input("Enter your favourite colour: ")

# C2
first_name = input("Enter your first name: ")
print(first_name)

# C3
surname = input("Enter your surname: ")
first_name = input("Enter your first name: ")

print(first_name)
print(surname)

# C4
surname = input("Enter your surname: ")
first_name = input("Enter your first name: ")

print(first_name + " " + surname)

# Difficulty 2
# C5
number1 = int(input("Enter a number: "))
number2 = int(input("Enter another number: "))

print(f"Total: {number1 + number2}")

# C6
number1 = int(input("Enter a number: "))
number2 = int(input("Enter another number: "))

print(f"Added together: {number1 + number2}")
print(f"Multiplied together: {number1 * number2}")

# C7
distance = float(input("Enter the distance (in metres): "))
time = float(input("How long did the journey take (in seconds): "))
print(f"Average speed: {distance / time}m/s")

# Difficulty 3
# C8
minutes = int(input("Enter the amount of minutes you have used: "))
texts = int(input("Enter the amount of texts you have sent: "))
print(f"The total cost of the bill is {minutes * 0.10 + texts * 0.05 + 10.00}")

# C9
import random
names = ["Harry", "Alastair", "Lucas", "Dylan", "Elliot", "Daniel", "Matthew"]
random_name = random.choice(names)
name = input("Enter your name: ")
print("You're cool." if name == random_name else "Nice to meet you.")

# C10
guess = int(input("Enter the number of letters there are in the alphabet: "))
print("You're correct!" if guess == 26 else "You're wrong...")

# Difficulty 4
# C11
number1 = int(input("Enter a number: "))
number2 = int(input("Enter another number: "))
print(f"The bigger number is: {max(number1, number2)}")
# print(f"The bigger number is: {number1 if number1 > number2 else number2}")

# C12
random_number = random.randint(1, 10)
number_guess = int(input("Guess the number I'm thinking of (1 to 10): "))
print("Correct" if number_guess == random_number else "Not what I was thinking")

# C13
days_per_week = int(input("Enter the days you work per week: "))
if days_per_week > 4:
  print(f"You get 28 days holiday a year.")
else:
  print(f"You get {days_per_week/5 * 28} days holiday a year.")

# Difficulty 5
# C14
traffic_light = input("Colour of the traffic light: ")
if traffic_light == "green":
  print("Go.")
elif traffic_light == "amber":
  print("Get Ready.")
else:
  print("Stop.")

# C15
olympic_value = input("Enter an Olympic Value: ").lower()
if olympic_value in ("respect", "excellence", "friendship"):
  print("That's correct")
else:
  print("Incorrect")

# C16
hours_watching_tv = float(input("Enter the amount of hours you watch TV: "))
if hours_watching_tv < 2:
  print("That should be ok")
elif hours_watching_tv < 4: 
  print("That will rot your brain") # ??? 
else:
  print("That is too much TV")

# C17
for i in range(1, 11):
  print(i)

# C18
for i in range(2, 22, 2):
  print(i)

# C19
number_guess = None
while number_guess != 7:
  number_guess = int(input("Guess the number I'm thinking of: "))

print("Well Done")
