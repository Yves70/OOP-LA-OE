class Phone():
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def describePhone(self):
        print(f"Phone Brand: {self.brand} \nPhone Model: {self.model}\n")
class Andriod(Phone):
    def __init__(self,brand,model):
        Phone.__init__(self,brand,model)
phone1 = Andriod("Samsung","Galaxy S")
phone1.describePhone()