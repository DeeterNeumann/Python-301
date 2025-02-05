# Write a script with three classes that model everyday objects.
# - Each class should have an `__init__()` method that sets at least 3 attributes
# - Include a `__str__()` method in each class that prints out the attributes
#     in a nicely formatted string.
# - Overload the `__add__()` method in one of the classes so that it's possible
#     to add attributes of two instances of that class using the `+` operator.
# - Create at least two instances of each class.
# - Once the objects are created, change some of their attribute values.???
#
# Be creative. Have some fun. :)
# Using objects you can model anything you want:
# Animals, paintings, card games, sports teams, trees, people etc...

class Pet:
    """Models a pet"""

    def __init__(self, animal, food, toy):
        self.animal = animal
        self.food = food
        self.toy = toy

    def __str__(self):
        return f"The {self.animal} eats {self.food} and plays with their favorite toy, a {self.toy}"

    def __add__(self, other):
        """Combines two pets"""
        new_breed = self.animal + other.animal
        new_food = self.food + " " + other.food
        new_toy = self.toy + " " + other.toy
        return Pet(animal=new_breed, food = new_food, toy = new_toy)

class FootballTeam:
    """Models the scheme of a football team"""

    def __init__(self, offense, defense, players_on_field):
        self.offense = offense
        self.defense = defense
        self.players_on_field = players_on_field

    def __str__(self):
        return f"The football team runs a {self.offense} offense and a {self.defense} defense. Each will have {self.players_on_field} men on the field."

class Shoe:
    """Models a design your own shoe feature"""
    def __init__(self, upper, tongue, lace, midsole, outsole):
        self.upper = upper
        self.tongue = tongue
        self.lace = lace
        self.midsole = midsole
        self.outsole = outsole

    def __str__(self):
        return f"The {self.upper} shoe has a {self.tongue} tongue and {self.lace} laces. The midsole is {self.midsole} and the bottom is {self.outsole}."
    

dog = Pet("dog", "kibble", "bone")
cat = Pet("cat", "fish", "yarn ball")

print(dog)
print(cat)

cd = cat + dog
print(cd)

team = FootballTeam("west coast", "4-3", 11)
ar = FootballTeam("air raid", "3-4", 11)

print(team)
print(ar)

b = Shoe("black", "white", "black", "black", "gum")
w = Shoe("white", "white", "red", "white", "red")

print(b)
print(w)