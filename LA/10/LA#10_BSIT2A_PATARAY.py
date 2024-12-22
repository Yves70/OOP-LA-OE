class Vehicle():
    def __init__(self,brand,model,fuel_type):
        self.brand = brand
        self.model = model
        self.fuel_type = fuel_type
    
    def describeVehicle(self):
        print(f"Brand: {self.brand} \nModel: {self.model} \nFuel Type: {self.fuel_type}")
class Car(Vehicle):
    pass

car1 = Car("Toyota","Toyota ae86 trueno","unleaded gasoline")
car1.describeVehicle()

class Motorcycle(Vehicle):
    pass

motor1 = Motorcycle("Yamaha", "Yamaha Aerox", "Pure unleaded fuel")
motor1.describeVehicle()