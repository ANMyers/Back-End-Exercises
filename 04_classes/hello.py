class Animal:
    def __init__(self, name = None, species = None):
        self.name = name
        self.species = species
        self.speed = 0
        self.legs = 0

    def getName(self):
        return self.name

    def walk(self):
        print("Parent class walk method")
        self.speed = self.speed + (0.1 * self.legs)

    def setSpecies(self, species):
        self.species = species

    def getSpecies(self):
        return self.species

    # __str__ is a special function equivalent to toString() in JavaScript
    def __str__(self):
        return "{} is a {}".format(self.name, self.species)


class Dog(Animal):
    def __init__(self, name):
        Animal.__init__(self, name, "Dog")
        # or super().__init__(name, "Dog")

    def walk(self):
        self.speed = self.speed + (0.2 * self.legs)

tommy = Animal('Tommy', 'Tortoise')
print(tommy)


