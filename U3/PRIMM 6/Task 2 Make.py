number_list = [73,99,93,54,84,71,47,49,60,40,79,76,9,69,100,78,25,65,1,88]
def binarySearch(number_list, number_to_find):
    listOfNumbers = number_list
    x = number_to_find
    s = None
    for i in range(len(listOfNumbers)):
        if x == listOfNumbers[i]:
            s = f"{x} was found at index {i}."
            return s
        else:
            pass
    
    return f"{x} could not be found."

def bubbleSort(number_list):
  myList = number_list

  Passes = 0
  Swaps = 0
  hasSorted = True
  while hasSorted:
    hasSorted = False
    for i in range(len(myList) - 1):
        if myList[i] > myList[i + 1]:
                temp = myList[i]
                temp2 = myList[i+1]
                myList[i] = myList[i + 1]
                myList[i + 1] = temp
                Swaps += 1
                hasSorted = True
        else:
            continue
    Passes += 1

  fl = f"Sorted list:  {myList}"
  return fl

print(number_list)
print(binarySearch(number_list, 60))
print(bubbleSort(number_list))
