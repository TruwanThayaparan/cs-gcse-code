citiesListRAW = []
citiesListCLEAN = []
filCities = open("cities.txt", "rt")
for line in filCities:
    citiesListRAW.append(line)

filCities.close()
for each in citiesListRAW:
    if (each in citiesListCLEAN) == False:
        citiesListCLEAN.append(each)

# for element in citiesListClean: print(element)

fileOut = open("unique.txt", "wt")
for each in citiesListCLEAN:
    fileOut.write(each)
fileOut.close()

fileOut = open("unique.txt", "a")
fileOut.write("501, Bradford \n")
fileOut.close()

import random
randomCityID = random.randint(0, len(citiesListCLEAN))
print(citiesListCLEAN[randomCityID])
