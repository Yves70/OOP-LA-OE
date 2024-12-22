class Spiderman():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def describeSpiderman(self):
        print (f"Name: {self.name} Age: {self.age}")
        
class Tobey(Spiderman):
    def __init__(self,name,age,movieTitle):
        super().__init__(name,age)
        self.movieTitle = movieTitle

class Andrew(Spiderman):
    def __init__(self,name,age,movieTitle):
        super().__init__(name,age)
        self.movieTitle = movieTitle

class Tom(Spiderman):
    def __init__(self,name,age,movieTitle):
        super().__init__(name,age)
        self.movieTitle = movieTitle

tobey = Tobey("Tobey Maguire","49 years old","Spider-Man")
andrew = Andrew("Andrew Garfield","41 years old","Amazing Spider-Man")
tom = Tom("Tom Holland","28 years old","Spider-Man: No Way Home")


print(f"Name: {tobey.name.upper()}  Movie Title:{tobey.movieTitle}")
print(f"Name: {andrew.name.upper()}  Movie Title:{andrew.movieTitle}")
print(f"Name: {tom.name.upper()}  Movie Title:{tom.movieTitle}")
    
