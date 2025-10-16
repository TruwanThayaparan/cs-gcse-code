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
