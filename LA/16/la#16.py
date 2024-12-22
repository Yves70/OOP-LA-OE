class Appliance:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    
    def operate(self):
        print("Operating!")
    def info(self):
        print(f"BRAND: {self.brand} MODEL: {self.model}")
        
class WashingMachine(Appliance):
    pass
    def operate(self):
        print("Washing clothes!")
class Refrigerator(Appliance):
    def __init__(self,brand,model):
        super().__init__(brand,model)
    def operate(self):
        print("Keeping food cold!")
class Microwave(Appliance):
    def __init__(self,brand,model):
        Appliance.__init__(self,brand,model)
    def operate(self):
        print("Heating food!")
        
washing = WashingMachine("LG","16.0 kg Laundry Twin Tub Washer Power Storm")
ref = Refrigerator("Samsung","RS64T5F01B4/TC")
microwave = Microwave("Panasonic","NE-1853LDK 18L Commercial Microwave Oven")

appliances = [washing,ref,microwave]

for appliance in appliances:
    appliance.operate()

for appliance in appliances:
    appliance.info()
    


    