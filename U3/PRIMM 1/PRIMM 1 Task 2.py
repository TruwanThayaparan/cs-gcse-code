# TASK 2 RUN
comSciMarks = [10, 8, 2, 9, 4, 7]

for index in range(3):
    print(comSciMarks[index])

# TASK 2 MODIFY
for index in range(len(comSciMarks)):
    print(comSciMarks[index])

# TASK 2 MAKE
highestNumber = comSciMarks[0]
lowestNumber = comSciMarks[0]
totalMarks = 0
for index in range(len(comSciMarks)):
    var1 = comSciMarks[index]
    try:
        var2 = comSciMarks[index + 1]
        if var2 > var1:
            if var2 > highestNumber:
                highestNumber = var2

        if var2 < var1:
            if var2 < lowestNumber:
                lowestNumber = var2
    except IndexError:
        print("...")
    
    totalMarks += comSciMarks[index]

meanValue = totalMarks // len(comSciMarks) #Floor Division JAJAJA
print("Mean Mark", meanValue)
print("Total marks", totalMarks)
print("Highest mark", highestNumber)
print("Lowest mark", lowestNumber)
