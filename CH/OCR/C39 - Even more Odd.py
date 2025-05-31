# Challenge 39 -  Even more Odd
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
passes = 0
swaps = 0
needsSorting = True

while needsSorting:
    needsSorting = False
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
            swaps += 1
            needsSorting = True
    passes += 1

def move_evens_after_odds(sorted_list):
    odds = [x for x in sorted_list if x % 2 != 0]
    evens = [x for x in sorted_list if x % 2 == 0]
    return odds + evens

result = move_evens_after_odds(numbers)

print(f"Sorted List: {result}")
print(f"Total Passes: {passes}, Total Swaps: {swaps}")
