ListOfNumbers = [1,3,2,5,4,7]
x = 5

for i in range(len(listOfNumbers)):
  if x == listOfNumbers[i]:
    print(x, "was found at index", i)
    break
  else:
    print(x, "was not found at index", i)
