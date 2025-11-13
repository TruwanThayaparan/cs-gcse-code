# Challenge 20 - Palindromes

pal = input("Enter a word into the palindrome checker... ")

palindrome = True
for i in range(len(pal) // 2): # Only check half the string
    if pal[i] != pal[len(pal) - 1 - i]:
        palindrome = False
        break

if palindrome:
    print(f"{pal} is a palindrome.")
else:
    print(f"{pal} is not a palindrome.")

# pal[::-1] - even simpler
