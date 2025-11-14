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
count = 0

while count < times:
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
  count += 1

mean = weights_total / count
print(f"Average weight: {mean:.2f} g")
