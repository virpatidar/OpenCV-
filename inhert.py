class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species= "Dog")
        self.breed = breed

    def speak(self):
        print(f"{self.name} barks.")
        Animal.speak()

obj1 = Dog("Buddy", "Golden Retriever")
print("Animal Name: ", obj1.name)
print("Animal Species: ", obj1.species)
print("Animal Breed: ", obj1.breed)
