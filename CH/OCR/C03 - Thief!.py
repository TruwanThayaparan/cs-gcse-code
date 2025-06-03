# Challenge 3 - Thief!

from itertools import permutations

pin = "4214"  # set this to any 4-digit number

while True:
    dan = input("Input the four digits in question (XXXX): ").strip()
    if len(dan) != 4 or not dan.isdigit():
        print("You must enter exactly 4 digits.")
        continue
    break

digits = list(dan)
found = False

for attempt_tuple in permutations(digits, 4):
    attempt = ''.join(attempt_tuple)
    print(attempt)
    if attempt == pin:
        print("PIN HAS BEEN CRACKED:", attempt)
        found = True
        break

if not found:
    print("PIN could not be cracked with these digits.")

'''
OLD VERSION:
pin = "4214" # set this to any 4-digit number
while True:
    dan = input("Input the four digits in question (XXXX): ").strip()
    if len(dan) != 4 or not dan.isdigit():
        print("You must enter exactly 4 digits.")
        continue
    break
    
numbers = [dan[0], dan[1], dan[2], dan[3]]
saved = []
print(numbers)

for i in range(4):
    for j in range(4):
        for k in range(4):
            for l in range(4):
                attempt = dan[i] + dan[j] + dan[k] + dan[l]
                if len(set([dan[i], dan[j], dan[k], dan[l]])) < 4:
                    continue
                if attempt in saved:
                    continue
                if attempt == pin:
                    print("PIN HAS BEEN CRACKED:", attempt)
                else:
                    print(attempt)
                saved.append(attempt)
'''

# OLD VERSION (THIS DOES NOT ANSWER THE PROMPT CORRECTLY)
'''
# Challenge 3 - Thief!

pin = "4214" # set this to any 4 digit number
dan = input("Input the four digits in question: ")
numbers = [dan[0], dan[1], dan[2], dan[3]]
saved = []
found = False
print(numbers)

for i in range(4):
    for j in range(4):
        for k in range(4):
            for l in range(4):
                attempt = dan[i] + dan[j] + dan[k] + dan[l]
                if len(set([dan[i], dan[j], dan[k], dan[l]])) < 4:
                    continue
                if attempt in saved:
                    continue
                if attempt == pin:
                    print("PIN HAS BEEN CRACKED:", attempt)
                    found = True
                    break
                else:
                    print(attempt)
                    saved.append(attempt)
            if found:
                break
        if found:
            break
    if found:
        break
'''
