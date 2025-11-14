# Difficulty 6
# Challenge 28
import math

while True:
  try:
    length = float(input("Length of the garden (metres): "))
    break
  except ValueError:
    print("You must enter a number!")

while True:
  try:
    width = float(input("Width of the garden (metres): "))
    break
  except ValueError:
    print("You must enter a number!")

while True:
  try:
    rad = float(input("Enter the radius of the flower bed (metres): "))
    break
  except ValueError:
    print("You must enter a number!")

area_of_garden = length * width
turf_required = area_of_garden - (math.pi * rad**2)
print(f"Turf needed: {round(turf_required, 2)} metres squared.")



# Challenge 29
while True:
  try:
    bears_made = int(input("Enter the number of teddy bears made: "))
    break
  except ValueError:
    print("You must enter a number!")

while True:
  try:
    hours_worked = int(input("Enter the number of hours worked: "))
    break
  except ValueError:
    print("You must enter a number!")

wages_bm = bears_made * 2
wages_hw = hours_worked * 5

print(f"Wages earned: {max(wages_hw, wages_bm)}")
# wages_hw if wages_hw > wages_bm else wages_bm



# Challenge 30
def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

def triangle_type(a, b, c):
    return "Isosceles" if (a == b or b == c or a == c) else None

def check():
    try:
        a = float(input("Enter side 1: "))
        b = float(input("Enter side 2: "))
        c = float(input("Enter side 3: "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    if not is_triangle(a, b, c):
        print("These sides do NOT form a triangle.")
        return

    t_type = triangle_type(a, b, c)

    print("Isosceles" if t_type else "Not Isosceles")

check()



# Challenge 31
while True:
  try:
    times = int(input("How many weights do you want to enter? "))
    if times <= 0:
      print("You must enter a positive number.")
    else:
      break
  except ValueError:
    print("You must enter a whole number.")

weights_total = 0

for i in range(1, times + 1):
  while True:
    try:
      weight = int(input("Enter a weight: "))
      if weight < 0:
        print("You must enter a positive weight.")
      else:
        break
    except ValueError:
      print("You must enter a whole number.")
    
  weights_total += weight

mean = weights_total / times
print(f"Average weight: {mean:.2f} g")



# Challenge 32
while True:
    try:
        money = float(input("Enter the amount of money you want to save: "))
        if money < 0:
            print("You must enter a positive amount.")
        break
    except ValueError:
        print("You must enter a valid number.")

while True:
    try:
        num_accounts = int(input("Enter the number of bank accounts to compare: "))
        if num_accounts <= 0:
            print("Number of accounts must be at least 1.")
        break
    except ValueError:
        print("You must enter a valid integer.")

totals = []

for i in range(1, num_accounts + 1):
    while True:
        try:
            interest_rate = float(input(f"Enter the interest rate for account {i} (in %): "))
            if interest_rate < 0:
                print("Interest rate must not be negative.")
            break
        except ValueError:
            print("You must enter a valid number.")

    interest = (money / 100) * interest_rate
    total = money + interest
    totals.append(total)

    print(f"Total amount for account {i}: {total:.2f}")

max_total = max(totals)
best_account = totals.index(max_total) + 1
print(f"\nThe best account is account {best_account} with a total of {max_total:.2f}.")



# Challenge 33
while True:
    try:
        gcses_done = int(input("How many GCSEs did you do? "))
        if gcses_done <= 0:
            print("You must enter at least 1 GCSE.")
        else:
            break
    except ValueError:
        print("You must enter a valid number.")

total_points = 0
    
for i in range(1, gcses_done + 1):
  while True:
    try:
      result = int(input(f"Enter result for GCSE {i} (1-9): "))
      if result < 1 or result > 9:
        print("Grade must be between 1 and 9.")
      else:
        break
    except ValueError:
      print("You must enter a whole number.")
    
  total_points += result

if total_points > 40:
  print("You can go to the sixth form")
elif 35 <= total_points <= 39:
  print("A discussion is needed")
else:
  print("Sorry, not enough points")
