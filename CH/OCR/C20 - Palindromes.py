# Challenge 20 - Palindromes

pal = input("Enter a word into the palindrome checker... ")

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
