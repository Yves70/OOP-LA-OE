class Toy():
    def __init__(self,name,price):
        self.name = name
        self.price = price
    def describeToy(self):
        print(f"Toy's Name: {self.name} \nToy's Price: {self.price}\n")
class Car(Toy):
    def __init__(self,name,price):
        super().__init__(name,price)
        
car1 = Car("Hotwheels", 150)
car1.describeToy()