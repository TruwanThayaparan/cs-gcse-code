# Binary and linear search

# Setup
listOfNumbers = [3, 5, 7, 9, 12, 14, 16, 18, 21, 23, 27]

while True:
    try:
        numberToFind = int(input("Input a number to find... "))
        t = listOfNumbers.index(numberToFind)
        break
    except ValueError: # not sure how to inc. in the binary search :/
        print("Sorry, that's not in the list!")

# Binary Search
high = len(listOfNumbers)
low = 0
mid = (high + low) // 2

comparisons = 0
BinaryComparisons = 0

print(" ")
print("Binary Search:")
print(" ")

while numberToFind != listOfNumbers[mid]:
    mid = (high + low) // 2
    comparisons += 1
    if numberToFind > listOfNumbers[mid]:
        low = mid + 1
        print("Attempted index", mid, ". Number",listOfNumbers[mid],"too low!")
        print("Comparison:", comparisons)
    elif numberToFind < listOfNumbers[mid]:
        high = mid - 1
        print("Attempted index", mid, ". Number",listOfNumbers[mid],"too high!")
        print("Comparison:", comparisons)
    else:
        print("numberToFind (",listOfNumbers[mid], ") was found at index", mid, ".")
        print("This took", comparisons, "comparisons.")
        BinaryComparisons = comparisons
        break
    print(" ")

# Linear Search
comparisons = 0 # Reseting the variable
foundNumber = False
LinearComparisons = 0

print("\n")
print("Linear Search:")
print(" ")

for i in range(len(listOfNumbers)):
    comparisons += 1
    if numberToFind == listOfNumbers[i] : 
        print(numberToFind, "was found at index", i )
        print("This took", comparisons, "comparisons.")
        LinearComparisons = comparisons
        foundNumber = True
        break 
    else: 
        print(numberToFind, "was not found at index", i)
        print("Comparison:",comparisons)
    print(" ")

print("\n")
print("Winner:")
print(" ")

if LinearComparisons > BinaryComparisons: # If L/B won by 1 comparison, it will say "1 comparisons" and "1 times" but I don't want to make an exception womp womp
    print("Binary search won by", LinearComparisons - BinaryComparisons, "comparisons.")
    print("Binary search needed  to compare", BinaryComparisons, "times whilst linear search needed to compare", LinearComparisons, "times.")

elif LinearComparisons < BinaryComparisons:
    print("Linear search won by", BinaryComparisons - LinearComparisons, "comparisons.")
    print("Linear search needed  to compare", LinearComparisons, "times whilst binary search needed to compare", BinaryComparisons, "times.")
else:
    print("Binary and linear search both took the same amount of comparisons:", BinaryComparisons)
