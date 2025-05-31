# Challenge 19 - Times tables
while True:
  try:
    times = int(input("Enter a number to see its times table: "))
    break
  except ValueError:
    print("You must enter a number.")

for i in range(1, 13):
  print(f"{i} x {times} = {i * times}")
