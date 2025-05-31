# Challenge 18 - Squares
while True:
  try:
    count_to = int(input("What do you want to square to? "))
    break
  except ValueError:
    print("You must enter a number.")

for i in range(1, count_to):
  print(f"{i} squared is {i ** 2}")
