letters = set("abcdefghijklmnopqrstuvwxyz")

sentence = input().strip()

found_letters = set(char for char in sentence.lower() if char in letters)

if found_letters == letters:
    print("Pangram")
else:
    print("Not a pangram")
