class Adobo:
    def __init__(self, meat, dry_season, wet_season):
        self.meat = meat
        self._dryseason = dry_season
        self.__wetseason = wet_season
        
    def __str__(self):
        return f"Ang adobo ko ay {self.meat}, {self._dryseason}, {self.__wetseason}"
        
    def may_carrot_ba(self):
        return self.__wetseason
    
adobo_dry = Adobo("chicken", "water", "asin")
adobo2 = Adobo("baka", "water" , "tuyo")
adobo3 = Adobo("Pork", "water" , "Onion")
print(adobo_dry.may_carrot_ba())
print(adobo2.may_carrot_ba())
print(adobo3.may_carrot_ba())