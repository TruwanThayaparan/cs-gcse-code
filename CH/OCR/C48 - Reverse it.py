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
    
print("Length:",len(red))
print("Vowels:",vx)
print("Consonants:", len(red) - vx)

pal = lets_generate
palidrome = True
for i in range(len(pal) - 1):
  if pal[i] == pal[len(pal) - 1 - i]:
    continue
  else:
    palidrome = False
    break
    
if palidrome:
    print(pal, "is a palindrome.")
else:
    print(pal, "is not a palindrome.")
