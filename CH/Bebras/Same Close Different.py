number1 = int(input())
number2 = int(input())
if number1 == number2:
  print("same")
elif abs(number1 - number2) == 1:
  print("close")
else:
  print("different")
