from abc import ABC, abstractmethod

class Character(ABC):
    @property   
    @abstractmethod
    def __init__(self, name):
        pass
        
    
class Batman(Character):
    def __init__(self, name, alias):
        self.name = name
        self.__alias = alias
      
    @property
    def alias(self):
        return self.__alias
    
Batman = Batman("Bruce Wayne", "Batman")
print(Batman.alias)