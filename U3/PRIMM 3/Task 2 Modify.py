from collections import namedtuple

Pets = namedtuple('peta', 'animal name age')

Dottie = Pets(animal = 'cat', name = 'Dottie', age = 9)
Jack = Pets(animal = 'cat', name = 'Jack', age = 9)
Lassie = Pets(animal = 'dog', name = 'Lassie', age = 13)
Rover = Pets(animal = 'dog', name = 'Rover', age = 7)

print(Dottie)
print(Jack)
print(Lassie)
print(Rover)
