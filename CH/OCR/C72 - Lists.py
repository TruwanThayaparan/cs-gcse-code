# Challenge 72 - Lists
import random

# Step 1
numbers = []

while True:
    try:
        low = int(input("Enter the lower bound: "))
        break
    except ValueError:
        print("You must enter a number.")

while True:
    try:
        high = int(input("Enter the upper bound: "))
        if high <= low:
            print("Upper bound must be greater than lower bound.")
        else:
            break
    except ValueError:
        print("You must enter a number.")

for i in range(low, high + 1):
    numbers.append(i)

print("List:", numbers)

# Step 2
while True:
    try:
        to_add = int(input("What number do you want to add? "))
        break
    except ValueError:
        print("You must enter a number.")

while True:
    try:
        to_pos = int(input(f"Which position do you want to add this number? (0-based index, 0 to {len(numbers)}) "))
        if 0 <= to_pos <= len(numbers):
            break
        else:
            print(f"Position must be between 0 and {len(numbers)}.")
    except ValueError:
        print("You must enter a number.")

numbers.insert(to_pos, to_add)
print("After insertion:", numbers)

# Step 3
while True:
    try:
        num_sublists = int(input("How many sub-lists do you want to create? "))
        if num_sublists > 0:
            break
        else:
            print("Please enter a positive number.")
    except ValueError:
        print("You must enter a number.")

list_of_lists = []
for _ in range(num_sublists):
    min_size = max(1, len(numbers) - 2)
    max_size = len(numbers)
    sublist_size = random.randint(min_size, max_size)
    sublist = random.sample(numbers, sublist_size)
    list_of_lists.append(sublist)

print("List of lists (random sublists):", list_of_lists)

# Step 4
sorted_list_of_lists = sorted(list_of_lists, key=len)
print("Sorted list of lists by length:", sorted_list_of_lists)
