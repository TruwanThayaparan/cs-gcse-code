allowed = 0
children = int(input())
for i in range(children):
  check = float(input())
  if check > 1.19:
    allowed += 1

print(allowed)
