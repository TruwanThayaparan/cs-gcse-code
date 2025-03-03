# Bubble Sort Algorithm

#myList = [1,3,2,4,5]
myList = [73,99,93,54,84,71,47,49,60,40,79,76,9,69,100,78,25,65,1,88] # A nice long random list

print(myList)
print(f"\n")

import random

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
                print("Swap",Swaps,"between",temp,"and",temp2)
        else:
            continue
    Passes += 1
    print("Pass",Passes)
    print(f"\n")
    
print(myList)
print("Bubble sort swapped",Swaps,"times and went through the list",Passes,"times.")
