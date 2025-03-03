# Binary and linear search
# More detailed version of L5 and L6 Individual

# Setup
listOfNumbers = [3, 5, 7, 9, 12, 14, 16, 18, 21, 23, 27]

numberToFind = int(input("Input a number to find... "))       

# Binary Search
high = len(listOfNumbers) - 1
low = 0
mid = (high + low) // 2

comparisons = 0
BinaryComparisons = 0

print(" ")
print("Binary Search:")
print(" ")

while low <= high:
    mid = (high + low) // 2
    comparisons += 1
    
    if numberToFind > listOfNumbers[mid]:
        low = mid + 1
        print(f"Attempted index {mid}. Number {listOfNumbers[mid]} too low!")
    elif numberToFind < listOfNumbers[mid]:
        high = mid - 1
        print(f"Attempted index {mid}. Number {listOfNumbers[mid]} too high!")
    else:
        print(f"numberToFind ({listOfNumbers[mid]}) was found at index {mid}.")
        print(f"This took {comparisons} comparisons.")
        BinaryComparisons = comparisons
        break
    print(f"Comparison: {comparisons}")
    print(" ")

if low > high:
    print(f"Sorry, {numberToFind} is not in the list!")
    print(f"This took {comparisons} comparisons.")
    BinaryComparisons = comparisons

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

if foundNumber == False:
    print(f"Sorry, {numberToFind} is not in the list!")
    print(f"This took {comparisons} comparisons.")
    LinearComparisons = comparisons

print("\n")
print("Winner:")
print(" ")

if LinearComparisons > BinaryComparisons:
    if LinearComparisons - BinaryComparisons == 1:
        print("Binary search won by", LinearComparisons - BinaryComparisons, "comparison.") # I made an exception because I have time
        print("Binary search needed to compare", BinaryComparisons, "times whilst linear search needed to compare", LinearComparisons, "times.")
    else:
        print("Binary search won by", LinearComparisons - BinaryComparisons, "comparisons.")
        print("Binary search needed to compare", BinaryComparisons, "times whilst linear search needed to compare", LinearComparisons, "times.")

elif LinearComparisons < BinaryComparisons:
    if BinaryComparisons - LinearComparisons == 1:
        print("Linear search won by", BinaryComparisons - LinearComparisons, "comparison.")
        print("Linear search needed  to compare", LinearComparisons, "times whilst binary search needed to compare", BinaryComparisons, "times.")
    else:
        print("Linear search won by", BinaryComparisons - LinearComparisons, "comparisons.")
        print("Linear search needed  to compare", LinearComparisons, "times whilst binary search needed to compare", BinaryComparisons, "times.")
else:
    print("Binary and linear search both took the same amount of comparisons:", BinaryComparisons)
