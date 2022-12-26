import random

# pick a random animal froom animals.txt file
def PickRandomAnimal():
    sampleFile = open("animals.txt", "r")
    sampleList = sampleFile.read().splitlines()
    sampleFile.close()

    randomAnimal = random.choice(sampleList)
    
    if (randomAnimal != "list"):
        return randomAnimal
    else:
        PickRandomAnimal()

print(PickRandomAnimal())
