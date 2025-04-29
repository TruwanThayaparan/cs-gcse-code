# Challenge 15 - Pangrams
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
words = []

check_pan = ""
while check_pan != "stop":
    check_pan = input("Enter a string. Type stop to continue: ")
    if check_pan != "stop":
        words.append(check_pan)

for pangram in words:
    found_letters = []
    sh = False
    for let in pangram.lower():
        if let in letters:
            if let not in found_letters:
                found_letters.append(let)
                if len(found_letters) == 26:
                    print(True)
                    sh = True
                    break
    if not sh:
        print(False)
