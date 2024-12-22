class Adobo:
    def __init__(self, meat,dry_season, wet_season, ):
        self.meat = meat
        self._dry_season = dry_season
        self.__wet_season = wet_season
    def __str__(self):
        return f"Adobo recipe {self.meat}, {self._dry_season}, {self.__wet_season}"
    
adobong_manok = Adobo("chiken", "toyo" , "asukal")
adobong_baka = Adobo("baka", "asin" , "toyo")
adobo_baboy = Adobo("Pork", "toyo" , "Onion")
print(adobong_manok._meat)
print(adobong_baka.__dry_season)
print(adobo_baboy.__wet_season)
        
        