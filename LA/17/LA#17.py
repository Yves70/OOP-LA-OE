class Player:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
    def attack(self, target):
        target.health -= self.attack_power
        print(f"{self.name} attacked {target.name} for {self.attack_power} damage")
        print(f"{target.name}'s remaining health {target.health}")
        if target.health <= 0:
            print(f"The {target.name} is already defeated!!")
    def heal(self, amount):
        self.health += amount
        print(f"{self.health} healed for {amount} health. Current health: {self.health}")

leomord = Player("Leomord",800,100)
jawhead = Player("Jawhead",900,200)

leomord.attack(jawhead)
jawhead.attack(leomord)


while leomord.health > 0 and jawhead.health > 0:
    leomord.attack(jawhead)
    if jawhead.health <= 0:
        print(f"{leomord.name} wins! GG!")
        break
    jawhead.attack(leomord)
    if leomord.health <= 0:
        print(f"{jawhead.name} wins! GGWP!")
        break
leomord.heal(200)