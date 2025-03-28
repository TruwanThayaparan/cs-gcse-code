class classStudent:
  def Name(self, name):
    self.name = name
  def displayName(self):
    return self.name
  def Age(self, age):
    self.age = age
  def displayAge(self):
    return self.age

first = classStudent()
second = classStudent()
third = classStudent()

first.Name(input("What is the first person's name? "))
first.Age(input("What is the first person's age? "))

print(first.DisplayName())
print(first.DisplayAge())

second.Name(input("What is the second person's name? "))
second.Age(input("What is the second person's age? "))

print(second.DisplayName())
print(second.DisplayAge())

third.Name(input("What is the third person's name? "))
third.Age(input("What is the third person's age? "))

print(third.DisplayName())
print(third.DisplayAge())
