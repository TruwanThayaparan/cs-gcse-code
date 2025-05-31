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
    
print(f"Length: {len(red)}")
print(f"Vowels: {vx}")
print(f"Consonants: {len(red) - vx}")

pal = lets_generate

palindrome = True
for i in range(len(pal) // 2): # Only check half the string
    if pal[i] != pal[len(pal) - 1 - i]:
        palindrome = False
        break

if palindrome:
    print(f"{pal} is a palindrome.")
else:
    print(f"{pal} is not a palindrome.")
