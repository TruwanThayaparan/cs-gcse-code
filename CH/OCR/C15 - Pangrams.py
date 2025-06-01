# Challenge 15 - Pangrams
letters = set("abcdefghijklmnopqrstuvwxyz")
words = []

while True:
    check_pan = input("Enter a string. Type stop to continue: ").strip()
    if check_pan.lower() == "stop":
        break
    words.append(check_pan)

for sentence in words:
    found_letters = set(char for char in sentence.lower() if char in letters)

    if found_letters == letters:
        print(True)
    else:
        print(False)
