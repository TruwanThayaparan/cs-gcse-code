x = input().lower()
a = 0
b = 0
for i in x:
  if i in set("aeiou"):
    a += 1
  elif i in set("bcdfghjklmnpqrstvwxyz"):
    b += 1
  else:
    pass

print(a, b)
