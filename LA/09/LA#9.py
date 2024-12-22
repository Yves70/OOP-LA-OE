class Car:
    def __init__(self,brand):
        self.brand = brand

    def __str__(self):
        return f"Car brand: {car1.brand}"

car1 = Car("Toyota")
del car1
print(car1)