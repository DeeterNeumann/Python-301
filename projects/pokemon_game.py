# Build a very basic Pokémon class that allows you to simulate battles
# in a Rock-Paper-Scissors game mechanic, as well as feed your Pokémon.
#
# The class should follow these specifications:
#
# - Each Pokemon should have a `name`, `primary_type`, `max_hp` and `hp`
# - Primary types should be limited to `water`, `fire` and `grass`
# - Implement a `battle()` method based on rock-paper-scissors that
#   decides who wins based only on the `primary_type`:
#       water > fire > grass > water
# - Display messages that explain who won or lost a battle
# - If a Pokemon loses a battle, they lose some of their `hp`
# - If you call the `feed()` method on a Pokemon, they regain some `hp`


class Pokeman:
    """Models a Pokeman battle game"""
    
    allowed_primary = ("water", "fire", "grass")
    
    def __init__(self, name, primary_type: str, hp, max_hp = 100):
        self.name = name
        if primary_type not in self.allowed_primary:
            raise ValueError(f"Primary type must be one of {self.allowed_primary}")
        self.primary_type = primary_type
        if not (0 <= hp <= max_hp):
            raise ValueError(f"hp must be between 0 and 100 (max_hp)")
        self.hp = hp
        if max_hp > 100:
            raise ValueError("max_hp cannot exceed 100")
        self.max_hp = max_hp

# water beats fire
# fire beats grass
# grass beats water

    def battle(self, other):
        if self.primary_type == "water" and other.primary_type == "fire":
            other.hp -= 25
            return print(f"{self.primary_type} Pokeman beats {other.primary_type} Pokeman. {other.name} loses 25 hp and now has a hp of {other.hp}.")
        if self.primary_type == "fire" and other.primary_type == "grass":
            other.hp -= 25
            return print(f"{self.primary_type} Pokeman beats {other.primary_type} Pokeman. {other.name} loses 25 hp and now has a hp of {other.hp}.")
        if self.primary_type == "grass" and other.primary_type == "water":
            other.hp -= 25
            return print(f"{self.primary_type} Pokeman beats {other.primary_type} Pokeman. {other.name} loses 25 hp and now has a hp of {other.hp}.")
        if other.primary_type == "water" and self.primary_type == "fire":
            self.hp -= 25
            return print(f"{other.primary_type} Pokeman beats {self.primary_type} Pokeman. {self.name} loses 25 hp and now has a hp of {self.hp}.")
        if other.primary_type == "fire" and self.primary_type == "grass":
            self.hp -= 25
            return print(f"{other.primary_type} Pokeman beats {self.primary_type} Pokeman. {self.name} loses 25 hp and now has a hp of {self.hp}.")
        if other.primary_type == "grass" and self.primary_type == "water":
            self.hp -= 25
            return print(f"{other.primary_type} Pokeman beats {self.primary_type} Pokeman. {self.name} loses 25 hp and now has a hp of {self.hp}.")
        if other.primary_type == self.primary_type:
            return print(f"The battling Pokeman are of the same type. No hp damage done.")

    def feed(self):
        self.hp += 5
        if self.hp > 100:
            self.hp = 100
            print(f"Your Pokeman is FULL.")
        else:
            print(f"Feeding your Pokeman increased its hp to {self.hp}")
        
d = Pokeman("d", "water", 95)

c = Pokeman("c", "fire", 95)

e = Pokeman("e", "grass", 95)

f = Pokeman("f", "water", 100)

c.battle(d)

e.battle(d)

e.battle(c)
    
c.battle(e)

d.battle(f)

c.feed()
e.feed()
e.feed()
e.feed()
d.feed()
