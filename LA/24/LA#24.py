from abc import ABC, abstractmethod

class GameCharacter(ABC):
    @abstractmethod
    def attack(self):
        pass
class Warrior(GameCharacter):
    def attack(self):
        print("Swings sword!")
class Mage(GameCharacter):
    def attack(self):
        print("Casts a fireball!")
class Archer(GameCharacter):
    def attack(self):
        print("Shoots an arrow!")

warrior = Warrior()
mage = Mage()
archer = Archer()

warrior.attack()
mage.attack()
archer.attack()

class Healer(GameCharacter):
    def attack(self):
        print("Casts a healing spell on ally!")

healer = Healer()
healer.attack()