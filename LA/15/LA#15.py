class Dog:
    def __init__(self,name):
        self.name = name
    def speak(self):
        return "BARK!"
        
class Cat:
    def __init__(self,name):
        self.name = name
    def speak(self):
        return "MEOW!"
        
class Bird:
    def __init__(self,name):
        self.name = name
    def speak(self):
        return "CHIRP!"

class Fish:
    def __init__(self,name):
        self.name = name
    def speak(self):
        return "..."
        
def animal_sound(animal):
    print(f"{animal.name} says: {animal.speak()}")
        
dog = Dog("Dog")
cat = Cat("Cat")
bird = Bird("Bird")
fish = Fish("Fish")

animals = [dog,cat,bird,fish]
for animal in animals:
    animal_sound(animal)

