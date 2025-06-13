def calculate_add(a, b):
  answer = a + b
  return answer

def calculate_subtract(a, b):
  answer = a - b
  return answer

def calculate_multiply(a, b):
  answer = a * b
  return answer

def calculate_divide(a, b):
  answer = a / b
  return answer
  
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

print(calculate_add(num1, num2))
print(calculate_subtract(num1, num2))
print(calculate_multiply(num1, num2))
print(calculate_divide(num1, num2))
