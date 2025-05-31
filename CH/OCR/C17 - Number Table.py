# Challenge 17 - Number Table

print("Let's create a number table!")

while True:
  try:
    number = int(input("Enter a number: "))
    break
  except ValueError:
    print("You must enter a number.")

while True:
  operator = input("Enter one of the operators: +, -, * or /: ")
  if operator not in ["+", "-", "*", "/"]:
    print("Please choose a valid operator.")
    continue
  break

# top header
print(f"{operator} | ", end='')
for col in range(number + 1):
    print(f"{col:4}", end='')  # aligned output
print()

# separator line
print("-" * (6 + (number + 1) * 4))

# rows
for row in range(number + 1):
    print(f"{row:2} |", end='')  # row label
    for col in range(number + 1):
        try:
            if operator == '+':
                result = row + col
            elif operator == '-':
                result = row - col
            elif operator == '*':
                result = row * col
            elif operator == '/':
                result = round(row / col) if col != 0 else 'inf'  # rounded division
            else:
                result = 'err'
            print(f"{result:4}", end='')
        except Exception:
            print(f"{'err':4}", end='')
    print()  # new line after each row
