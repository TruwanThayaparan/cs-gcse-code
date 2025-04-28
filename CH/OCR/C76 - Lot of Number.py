# Challenge 76 - That’s a lot of number

text_file = open('numbers.txt','r') # Set this to the file where all the numbers are
numbers_to_add = []

lines = text_file.readlines()

for line in lines:
    # print(line)
    lint = int(line)
    numbers_to_add.append(lint)

# print(numbers_to_add)

answer = 0 
for i in range(len(numbers_to_add)):
    answer += numbers_to_add[i]

print(answer)
