# Challenge 25 - Ordering
numbers = []

for i in range(10):
    while True:
        try:
            print(i + 1)
            num = int(input("Enter your number: "))
            numbers.append(num)
            break
        except ValueError:
            print("Please enter a number.")

print(numbers)
while True:
    way = input("Should the numbers be sorted into an ascending order or a descending order? ")
    if way == "ascending" or way == "descending":
        break
    else:
        print("Not a valid option. Try again.")

# Bubble sort (it's a short list)
Passes = 0
Swaps = 0
hasSorted = True
while hasSorted:
    hasSorted = False
    for i in range(len(numbers) - 1):
        if way == "ascending":
            check = numbers[i] > numbers[i + 1]
        else:
            check = numbers[i] < numbers[i + 1]
            
        if check:
                temp = numbers[i]
                temp2 = numbers[i+1]
                numbers[i] = numbers[i + 1]
                numbers[i + 1] = temp
                Swaps += 1
                hasSorted = True
        else:
            continue
    Passes += 1

print(numbers)
