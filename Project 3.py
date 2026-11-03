class Parrot:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species
p1 = Parrot("Polly", 3, "Bird")
p2 = Parrot("Cacaw", 5, "Bird")
print(p1.name, p1.age, p1.species)
print(p2.name, p2.age, p2.species)