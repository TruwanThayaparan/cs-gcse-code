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
'''

class classFilms:
  def Name(self, name):
    self.name = name
  def DisplayName(self):
    return self.name
    
  def AgeRating(self, age):
    self.age = age
  def DisplayAge(self):
    return self.age

  def Genre(self, genre):
    self.genre = genre
  def DisplayGenre(self):
    return self.genre

  def StarRating(self, stars):
    self.stars = stars
  def DisplayStars(self):
    return self.stars

first = classFilms()
second = classFilms()
third = classFilms()
fourth = classFilms()
fifth = classFilms()

first.Name(input("What is the first movie's name? "))
first.AgeRating(input("What is the first movie's age rating? "))
first.Genre(input("What is the first movie's genre? "))
first.StarRating(input("What is the first movie's star rating? "))

print(first.DisplayName())
print(first.DisplayAge())
print(first.DisplayGenre())
print(first.DisplayStars())
