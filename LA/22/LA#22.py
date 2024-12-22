class Party:
    def __init__(self,theme):
        self.theme = theme
    def __secret_dish(self):
        print(f"Secret Dish: Macarons for the {self.theme} Party!\n")
    def celebration(self):
        print(f"{self.theme} Foods: stick O, cupcake, ice cream")
        print("Special Dish: Chocolate fountain")
        self.__secret_dish()
        
pajama_party = Party("Pajama")
beach_party = Party("Beach")
pool_party = Party("Pool")
pajama_party.celebration()
beach_party.celebration()
pool_party.celebration()