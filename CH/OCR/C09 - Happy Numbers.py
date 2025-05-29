# Challenge 9 - Happy Numbers

happy_numbers = []
found_all = 0
t = 1

while found_all < 8:
    if is_happy(t):
        found_all += 1
        # print(f"{t} is a happy number! HN: {found_all}")
        happy_numbers.append(t)
    else:
        pass
        # print(f"{t} is not a happy number.")
    t += 1

print("\nThe first 8 happy numbers are:")
print(happy_numbers)

'''
# alternative print-out
for i in happy_numbers:
  print(i)
'''
