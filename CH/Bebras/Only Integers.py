x = input()

try:
  x = int(x)
  print("integer")
except ValueError:
  print("not an integer")

'''
alternative solution

if x.isdigit():
    print("integer")
else:
    print("not an integer")
'''
