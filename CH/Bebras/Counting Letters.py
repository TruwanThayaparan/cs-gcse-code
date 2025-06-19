sentence = input().lower()
vowels = 0
consonants = 0
for i in sentence:
  if i in set("aeiou"):
    vowels += 1
  elif i in set("bcdfghjklmnpqrstvwxyz"):
    consonants += 1
  else:
    pass

print(vowels, consonants)
