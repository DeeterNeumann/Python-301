# Use your `Ingredients` class to create a URL to an online search
# that allows to look for recipes for dishes made from the
# available ingredients.

import webbrowser

class Ingredient:
    """Models a food item as an Ingredient."""

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def expire(self):
        """Expires the ingredient."""
        print(f"Whoops, the {self.name} went bad...")
        self.name = "expired " + self.name

    def use(self, use_amount):
        self.amount -= use_amount

    def __str__(self):
        return f"{self.name} ({self.amount})"
    
    def __repr__(self):
        return f"Ingredient(name={self.name}, amount={self.amount})"
    
    def __add__(self, other):
        new_name = self.name + other.name
        return Ingredient(name = new_name, amount = 1)
    
    def get_info(self):
        url = f"https://en.wikipedia.org/wiki/{self.name}"
        return webbrowser.open_new_tab(url)
    
    # def selfless():
    #     return

c = Ingredient("cauliflower", 20)
b = Ingredient("broccoli", 10)
d = Ingredient("dandelion", 5)

print(c.name, b.name, d.name)

s = Ingredient("salt", 50)
p = Ingredient("pepper", 50)

print(s.name, p.name)

d.expire()

print(d.name)

# s.selfless()

print(c)
print(repr(c))

x = s + b
print(x)
print(repr(x))

print(c.get_info())

print(f"{x!r}")