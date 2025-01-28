# print("Hello, world!")

# x = 5
# print(x)

# Run task
print('Welcome to the flatter.')
q1 = input("What's your name, very nice person?") # provide name

# Modify task
import random # use random module to provide you a random complement
random_number_wah = random.randint(1,3)

if random_number_wah == 1:
     print(q1 + ", you're amazing!") # original complement
elif random_number_wah == 2:
     print(q1 + ", you're wonderful!") # alternative 
else: # if random_number_wah is 3
     print(q1 + ", you're awesome!") # alternative

