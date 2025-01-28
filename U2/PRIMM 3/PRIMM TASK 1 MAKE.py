# Make task

a = 0
b = 0
task_mode = input("Enter the task you want to do [addition/subtraction/multiplication/division]")
if task_mode == "add" or task_mode == "addition":
    a = int(input("[ADDITION]: First number: "))
    b = int(input("[ADDITION]: Second number: "))
    addition_task = a + b
    print(a,"add",b,"equals",addition_task)
            
elif task_mode == "subtract" or task_mode == "subtraction":
    a = int(input("[SUBTRACTION]: First number: "))
    b = int(input("[SUBTRACTION]: Second number: "))
    subtraction_task = a - b
    print(a,"subtract",b,"equals",subtraction_task)
            
elif task_mode == "multiply" or task_mode == "multiplication":
    a = int(input("[MULTIPLICATION]: First number: "))
    b = int(input("[MULTIPLICATION]: Second number: "))
    multiplication_task = a * b
    print(a,"multiplied by",b,"equals",multiplication_task)

elif task_mode == "divide" or task_mode == "division":
    a = int(input("[DIVISION]: First number: "))
    b = int(input("[DIVISION]: Second number: "))
    division_task = a / b
    print(a,"divided by",b,"equals",division_task)

elif task_mode == "floor divide" or task_mode == "floor division": # it's a secret...
    a = int(input("[DIVISION]: First number: "))
    b = int(input("[DIVISION]: Second number: "))
    division_task = a // b
    print(a,"divided by",b,"equals",division_task)

else:
    print("ERROR: Invalid task!")
