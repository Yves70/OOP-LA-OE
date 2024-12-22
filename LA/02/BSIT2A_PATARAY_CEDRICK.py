class hero():
    def __init__(self,name,role,hp,mana,hp_regen,mana_regen,physical_atk):
        self.name = name
        self.role = role
        self.hp = hp
        self.mana = mana
        self.hp_regen = hp_regen
        self.mana_regen = mana_regen
        self.physical_atk = physical_atk
    
hero1 = hero("Selena","Assasin/Mage","HP - 2401","Mana - 490","HP regen - 6.8","Mana regen - 3.6","Physical Attack - 110")
print(f'''
{hero1.name}
{hero1.role}
{hero1.hp}
{hero1.mana}
{hero1.hp_regen}
{hero1.mana_regen}
{hero1.physical_atk}''')