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

# Bubble sort (it's a short list)
Passes = 0
Swaps = 0
hasSorted = True
while hasSorted:
    hasSorted = False
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
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
