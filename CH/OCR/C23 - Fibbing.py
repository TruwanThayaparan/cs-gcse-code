# Challenge 23 - Fibbing

while True:
    try:
        lets_generate = int(input("How many places of the Fibonacci sequence do you require? "))
        break
    except ValueError:
        print("Please enter a number.")

fib_sequence = []
previous_number = 0
current_number = 1

print("Sequence:")
for i in range(lets_generate):
    fib_sequence.append(previous_number)
    print(previous_number)
    next_number = previous_number + current_number
    previous_number = current_number
    current_number = next_number
    
print("Total:")
total = 0
for num in range(len(fib_sequence)):
    total += fib_sequence[num]
    
print(total)

print("Reversed Sequence:")
for num in reversed(fib_sequence):
    print(num)
