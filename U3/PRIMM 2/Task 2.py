Friends = []
for index in range(0,4):
  Friends.insert([index][0], [input("Please enter your friend's first name:")])
  Friends[index].append(input("Please enter your friend's last name:"))
print("Thank you. You have entered all four of your Friends.")
print(Friends)
