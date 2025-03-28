'''
When I get time for this...

You are now going to attempt to create your own class; the class should hold information about films. Your solution should fulfill the following requirements:
1. You should assign the class an appropriate name i.e. Films
2. The class must contain methods that add data items for each film (object), including:
The film’s name
The film’s age rating
The film’s genre i.e. action, comedy etc. and 
The film’s star rating (i.e. how good is was) 
Returns the data content for each film (object) 
3. You should create at least FIVE film objects 


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
'''
