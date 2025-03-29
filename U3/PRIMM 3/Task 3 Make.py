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

second.Name(input("What is the second movie's name? "))
second.AgeRating(input("What is the second movie's age rating? "))
second.Genre(input("What is the second movie's genre? "))
second.StarRating(input("What is the second movie's star rating? "))

print(second.DisplayName())
print(second.DisplayAge())
print(second.DisplayGenre())
print(second.DisplayStars())

third.Name(input("What is the third movie's name? "))
third.AgeRating(input("What is the third movie's age rating? "))
third.Genre(input("What is the third movie's genre? "))
third.StarRating(input("What is the third movie's star rating? "))

print(third.DisplayName())
print(third.DisplayAge())
print(third.DisplayGenre())
print(third.DisplayStars())

fourth.Name(input("What is the fourth movie's name? "))
fourth.AgeRating(input("What is the fourth movie's age rating? "))
fourth.Genre(input("What is the fourth movie's genre? "))
fourth.StarRating(input("What is the fourth movie's star rating? "))

print(fourth.DisplayName())
print(fourth.DisplayAge())
print(fourth.DisplayGenre())
print(fourth.DisplayStars())

fifth.Name(input("What is the fifth movie's name? "))
fifth.AgeRating(input("What is the fifth movie's age rating? "))
fifth.Genre(input("What is the fifth movie's genre? "))
fifth.StarRating(input("What is the fifth movie's star rating? "))

print(fifth.DisplayName())
print(fifth.DisplayAge())
print(fifth.DisplayGenre())
print(fifth.DisplayStars())
