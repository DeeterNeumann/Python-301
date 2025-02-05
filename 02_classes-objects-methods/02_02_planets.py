# Create a `Planet()` class that models attributes and methods of
# a planet object.
# Use the appropriate dunder method to get informative output with `print()`

class Planet():
    
    """Creates planet object"""
    def __init__(self, name, size, planet_number):
        self.name = name
        self.size = size
        self.planet_number = planet_number
    
    def __str__(self):
        return f"{self.name} is {self.size} in diameter and is the {self.planet_number} planet from the sun"
    
e = Planet("Earth", "7,926 miles", "3rd")
m = Planet("Mars", "4,222 miles", "4th")

print(e)
print(m)
