class FavoriteFood:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def __str__(self):
        return f"{self.name} contains: {self.ingredients}"

food1 = FavoriteFood("Pizza", ["cheese", "tomato sauce", "pepperoni", "dough"])
food2 = FavoriteFood("Burger", ["bun", "beef patty", "lettuce", "cheese", "tomato"])
food3 = FavoriteFood("Spaghetti", ["pasta", "marinara sauce", "meatballs", "parmesan"])

print(food1)
print(food2)
print(food3)