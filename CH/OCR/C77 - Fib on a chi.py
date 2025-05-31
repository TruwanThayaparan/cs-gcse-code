# Challenge 77 - Fib on a chi
fib_sequence = []
previous_number = 0
current_number = 1
seq = 1
print("Sequence:")
while True:
    fib_sequence.append(previous_number)
    ##print(previous_number)
    next_number = previous_number + current_number
    previous_number = current_number
    current_number = next_number
    seq += 1
    if len(str(current_number)) == 1000:
      print("The index and number of the first term in the Fibonacci sequence that contains 1,000 digits:")
      print(seq, current_number)
      break
