from animals import Dog
from animals import Cat
from animals import Bird

def readAnimals():
    with open('animals.csv', 'r') as f:
        for line in f.readlines():
            linelist = line.split(',')
            if linelist[0] == "Dog":
                dogObj = Dog(linelist[1], linelist[2], linelist[3], linelist[4])
                dogObj.printit()
            elif linelist[0] == "Cat":
                catObj = Cat(linelist[1], linelist[2], linelist[3], linelist[4])
                catObj.printit()
            elif linelist[0] == "Bird":
                birdObj = Bird(linelist[1], linelist[2], linelist[3], linelist[4])
                birdObj.printit()
readAnimals()

