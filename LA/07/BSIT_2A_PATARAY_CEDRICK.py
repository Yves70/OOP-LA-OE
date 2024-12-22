class Car:
    def __init__(self,brand,color):
        self.brand = brand
        self.color = color

car1 = Car("Toyota","Red")
car2 = Car("Nissan","Gray")
print(f"Car: {car2.brand}")
print(f"Orginal color: {car2.color}")

car1.color = "White"
print(f"Updated color: {car1.color}")