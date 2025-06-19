num = ""
count = 0
sum = 0
while num != -1:
  num = int(input())
  if num == -1:
    break
  count += 1
  sum += num

print(count)
print(sum)
