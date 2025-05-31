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
needsSorting = True

while needsSorting:
    needsSorting = False
    for i in range(len(numbers) - 1):
        if (way == "ascending" and numbers[i] > numbers[i + 1]) or \
           (way == "descending" and numbers[i] < numbers[i + 1]):
            numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
            Swaps += 1
            needsSorting = True
    Passes += 1

print(f"Sorted List: {numbers}")
print(f"Total Passes: {Passes}, Total Swaps: {Swaps}")


# Extension
sentence = input("Input a sentence: ")

option = input("Type 1 to sort all letters, or 2 to sort each word individually: ")

if option == "1":
    letters_only = sentence.replace(" ", "")
    sorted_letters = ''.join(sorted(letters_only))
    print(sorted_letters)

elif option == "2":
    words = sentence.split()
    sorted_sentence = ' '.join(''.join(sorted(word)) for word in words)
    print(sorted_sentence)

else:
    print("Invalid option.")
