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
