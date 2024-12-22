class Animal():
    def __init__(self,name,type):
        self.name = name
        self.type = type
    def describeAnimal(self):
        print(f"Fish name: {self.name} \nFish Type: {self.type} \nCan it swim? ")
class Fish(Animal):
    def __init__(self,name,type,can_swim):
        super().__init__(name,type)
        self.can_swim = True
fish1 = Fish("Clownfish","Blue Tang",True)
fish1.describeAnimal()
print(fish1.can_swim)