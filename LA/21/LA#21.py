class Adowbow:
    def __init__(self, meat, dry_season, wet_season):
        self.meat = meat
        self._dryseason = dry_season
        self.__wetseason = wet_season
        
    def __str__(self):
        return f"Ang adobo ko ay {self.meat}, {self._dryseason}, {self.__wetseason}"
        
    def may_carrot_ba(self):
        return self.__wetseason
    
adowbong_dry = Adowbow("chicken", "water", "asin")
adowbow2 = Adowbow("baka", "watir" , "tuyo")
adowbo3 = Adowbow("Pork", "water" , "Onyon")
print(adowbong_dry.may_carrot_ba())
print(adowbow2.may_carrot_ba())
print(adowbo3.may_carrot_ba())