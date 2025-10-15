# Challenge 21
age = int(input("Enter your age: "))
if 13 <= age <= 15:
  print("30% discount!")
elif 16 <= age <= 17:
  print("20% discount!")
elif 50 <= age:
  print("40% discount!")
else:
  print("NO discount.")

# Challenge 22
marks = int(input("Marks you got on the test: "))
print("U" if marks < 10 else "9" if marks == 100 else marks // 10)
