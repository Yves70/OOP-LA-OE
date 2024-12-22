class hero():
    def __init__(self,name,role,dmg_type,physical_atk):
        self.name = name
        self.role = role
        self.dmg_type = dmg_type
        self.physical_atk = physical_atk
    
    def __str__(self):
        return f"This hero is {self.dmg_type}."   
    
    def describe(self):
        print (f"{self.name} is {self.role} type of hero.")
        
    def pick(self):
        return f"{self.name} is a top pick in rank games."
    
hero1 = hero("Selena","Assasin/Mage","Burst Attack","Physical Attack - 110")
hero2 = hero("Grock","Tank","Crowd Control","Physical Attack - 90")
hero3 = hero("Layla","Marksman","Rapid Attack","Physical Attack - 95")
hero4 = hero("Lancelot","Assasin/Core","Burst Attack","Physical Attack - 100")
hero5 = hero("Jawhead","Fighter","Burst/CC Attack","Physical Attack - 105")

print(f'''
{hero1.name}
{hero1.role}
{hero1.dmg_type}
{hero1.physical_atk}''')
hero1.describe()
print(hero1)
print(hero1.pick())

print(f'''
{hero2.name}
{hero2.role}
{hero2.dmg_type}
{hero2.physical_atk}''')
hero2.describe()
print(hero2)
print(hero2.pick())

print(f'''
{hero3.name}
{hero3.role}
{hero3.dmg_type}
{hero3.physical_atk}''')
hero3.describe()
print(hero3)
print(hero3.pick())

print(f'''
{hero4.name}
{hero4.role}
{hero4.dmg_type}
{hero4.physical_atk}''')
hero4.describe()
print(hero4)
print(hero4.pick())

print(f'''
{hero5.name}
{hero5.role}
{hero5.dmg_type}
{hero5.physical_atk}''')
hero5.describe()
print(hero5)
print(hero5.pick())