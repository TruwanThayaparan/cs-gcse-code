# Fundamentals to Programming Unit 2

# L1 Constants and variables

'''
Variable - a named location in memory that stores data that can be accessed throughout a program
Constant - a variable that is set to never change the value
'''

'- PRIMM 1 -'
x = 5
print(x)

# L1 Arithmetic operators

'''
+ Adding
- Subtract
* Multiplication
/ Real division (5/2 = 2.5)
// Integer division (5//2 = 2)
% Modulus (5%2 = 1)
'''

'- PRIMM 1/[3] -'
a = int(input("Enter a number. "))
b = int(input("Enter a second number. "))
total = a + b
average = total/2
print(a," plus",b," equals",total,".")
print("Average is ",average)

# L2 Data types

'''
Data type - the format in which data is stored in a variable
'''

'''
Integer - Whole number
Real/float - Decimal number
Boolean - True/False
Character - A symbol
String - A collection or list of characters
'''

'- PRIMM 2 -'
q1 = 5
q2 = "hello"
print(type(q1))
print(type(q2))

# L2 Relational operators

'''
> greater than
>= greater than or equal to
== equal to
<= less than or equal to
< less than
!= not equal to
'''

'- PRIMM 2 -'
a = 1
b = 100
print(a<b)

# L3 Selection

'''
Selection - when a decision is made within an algorithm based on a conditional statement
Nested - when one programming construct is within another construct
'''

'- [PRIMM 3] -'
a = False
b = True
c = False
if a == True:
    print("a")
elif b == True:
    print("b")
else:
    print("c")

# L4 Iteration

'''
Iteration - a programming construct that is a sequence of instructions that is repeated
'''

'- PRIMM 4 -'
secretNum = 42
uInput = int(input("Guess a number between 1 and 100. "))
while uInput != secretNum:
    uInput = int(input("Incorrect! Guess another number between 1 and 100: "))
print("Correct! The secret number was ",secretNum)

# L5 Strings

'''
String - a string is a data type used in programming that is used to represent text rather than numbers
a string is a sequence of characters and can contain letters, numbers, symbols
'''

name = "Walter"
print(name[2])

''' Concatenation '''
fname = "Walter"
sname = "White"
name = fname + '' + sname
print(name);

''' Searching '''
if 'f' in 'walter':
    print("You win!")
else:
    print("You lose!")

''' String splitting'''
fname = "Walter"
# print(fname.subString(2,4))
print(fname[2:4])

len(fname)
print(fname.upper())
print(fname.lower())
# print(fname.isUpper())
# print(fname.isLower())

stre = "this is a string example... wow!"
print("Length of the string: ",len(stre))

text = "Computer" + " science"
print(text.index('m'))
print(text[9:16])

# L6 Boolean Logic Gates

'''
AND
OR
NOT
XOR
'''

# L7 Boolean operators
print(5 == 5 and 4 < 5)
print(4 == 5 or 4 < 5)

trigList = ["Sine", "Cosine", "Tangent", "Cotangent", "Secant", "Cosecant"]

trigInput = input("Name a trigonometric function. ")

correct = False

for function in trigList:
    if trigInput == function or trigInput == function.lower():
        print("Yes,",function,"is a trigonometric function.")
        correct = True

if not (correct):
    print("Sorry, that is not right.")
