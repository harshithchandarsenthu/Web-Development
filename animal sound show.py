from abc import ABC, abstractmethod
class Animal(ABC):
    def __init__(self, name, habitat):
        self.name = name
        self.habitat = habitat
    @abstractmethod
    def animal_type(self):
        pass
    def display(self):
        print("I am", self.name)
        print("I live in", self.habitat)
class Dog(Animal):
    def __init__(self, name, habitat, breed):
        super().__init__(name, habitat)
        self.breed = breed
    def animal_type(self):
        print("Dog")
    def bark(self):
        print("Ruf ruf!")
class Parrot(Animal):
    def __init__(self, name, habitat, phrase):
        super().__init__(name, habitat)
        if phrase == "":
            phrase = "Helloer"
        self.phrase = phrase
    def animal_type(self):
        print("Parrot")
    def repeat(self):
        print(self.phrase)
class Lion(Animal):
    def __init__(self, name, habitat):
        super().__init__(name, habitat)
    def animal_type(self):
        print("Lion")
    def roar(self):
        print("Rawr!")
show = [
    Dog("Zen", "a dog house", "poodle"),
    Parrot("Neo", "Forest", ""),
    Lion("Chris", "Namibian Grassland")
]
show[0].display()
show[0].bark()
show[1].display()
show[1].repeat()
show[2].display()
show[2].roar()
show[0].animal_type()
show[1].animal_type()
show[2].animal_type()
print(isinstance(show[0], Animal))
print([c.__name__ for c in Lion.__mro__])
