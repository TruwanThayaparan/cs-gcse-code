# Binary Search
high = len(listOfNumbers) - 1
low = 0
mid = (high + low) // 2

while low <= high:
    mid = (high + low) // 2
    
    if numberToFind > listOfNumbers[mid]:
        low = mid + 1
    elif numberToFind < listOfNumbers[mid]:
        high = mid - 1
    else:
        print(listOfNumbers[mid])
        break

if low > high:
   print("ERROR: NOT FOUND")
