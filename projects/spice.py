class Ingredient:
    """Models a food item as an Ingredient."""

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def __str__(self):
        return f"There are {self.amount} of {self.name}."
    
    def use(self, use_amount):
        """Reduces the amount of ingredient available"""
        self.amount -= use_amount
    
    def expire(self):
        """Expires the ingredient."""
        print(f"Whoops, the {self.name} went bad...")
        self.name = "expired " + self.name

# Inheritance

# build a subclass called Spice

# create a custom method grind()

# override the expire() method

# customize the __init__() method

class Spice(Ingredient):
    """Models a spice to flavor your food"""

    def __init__(self, name, amount,taste):
        super().__init__(name, amount)
        self.taste = taste

    def grind(self):
        print(f"You now have {self.amount} of ground {self.name}.")

# how to limit other to Spice objects???
    def blend(self, other):
        """Blends two spices."""
        blended = self.name + " " + other.name
        if self.amount >= other.amount:
            amount = other.amount
            print(f"You now have {other.amount} of {blended}.")
        else:
            amount = self.amount
            print(f"You now have {self.amount} of {blended}.")
        return Spice(name=blended, amount = amount, taste = self.taste)
    
    def expire(self):
        if self.name == "salt":
            print(f"salt never expires! ask the sea!")
        else:
            print(f"your {self.name} has expired. it's probably still good.")
            self.name = "old " + self.name

class Vegetable(Ingredient):
    """Models a vegetable to add to the meal"""
    
    def expire(self):
        """Moldy (expired) vegetable."""
        print(f"Ewww, the {self.name} is moldy...")
        self.name = "moldy " + self.name

    def diced(self):
        print(f"You now have {self.amount} diced {self.name}.")
        self.name = "diced " + self.name

# p = Ingredient('peas', 12)
# print(p)

# s = Spice('salt', 200, "salty")
# print(s)

# s.expire()
# print(s)

# s = Spice('salt', 200, "salty")

# s.grind()

# gp = Spice('garlic powder', 50, "garlicky")

# gp.blend(s)

# print(gp.blend(s))

# s.expire()

# gp.expire()

# p.expire()

# print(gp)

# c = Vegetable("carrot", 5)

# c.diced()

# p = Spice("pepper", 20, "hot")

# print(p.taste)

# t = Ingredient("tomatoes", 4)

# print(t)
