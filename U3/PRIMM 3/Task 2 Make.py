from collections import namedtuple

Films = namedtuple('films', 'film_name genre age_rating year_of_release')

Film1 = Films('The Shawshank Redemption', 'Drama', 'R', 1994)
Film2 = Films('Inception', 'Sci-Fi', 'PG-13', 2010)
Film3 = Films('The Lion King', 'Animation', 'G', 1994)
Film4 = Films('Pulp Fiction', 'Crime', 'R', 1994)
Film5 = Films('Avatar', 'Sci-Fi', 'PG-13', 2009)

print(Film1)
print(Film2)
print(Film3)
print(Film4)
print(Film5)
