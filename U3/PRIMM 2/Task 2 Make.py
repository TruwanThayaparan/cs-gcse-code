Cars = []
for index in range(0,5):
  Cars.insert([index][0], [input("Please enter a car's make:")])
  Cars[index].append(input("Please enter that car's model:"))
print("Thank you. You have entered all five Cars.")
print(Cars)
