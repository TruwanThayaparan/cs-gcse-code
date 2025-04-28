# Challenge 48 - Reverse it
lets_generate = input("Enter your word: ")

letters = []

for i in range(len(lets_generate)):
    letters.append(lets_generate[i])
    
# print(letters)

letters.reverse()

red = ""

for i in range(len(letters)):
    red += letters[i]
    
print(red)

vowels = "aeiou"
vx = 0
for v in vowels:
    vx += red.lower().count(v)
    
print("Length:",red)
print("Vowels:",vx)
print("Consonants:", len(red) - vx)

# Palindrome Checker can easily be implemented from my Palindromes script
