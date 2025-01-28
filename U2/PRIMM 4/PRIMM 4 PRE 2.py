import time

countingto = int(input("Please enter the number for me to count to:"))

for i in range(countingto):
        print(i + 1)
        time.sleep(1) # A natural pause

print("Start!")
