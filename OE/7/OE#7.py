class TekkenCharacter:
    def __init__(self, name, ability):
        self.name = name
        self.ability = ability

    def introduce(self, func):
        def wrapper():
            print("Introducing...")  
            func()
            print("This character is amazing!")  
        return wrapper

kunimitsu = TekkenCharacter("Kunimitsu", "Silent Blade")

@kunimitsu.introduce  
def character_intro():
    print(f"I am {kunimitsu.name} and I can use {kunimitsu.ability}.")
character_intro()
