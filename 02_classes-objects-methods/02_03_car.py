# The classic OOP example: Write a class to model a car. The class should:
#
# 1. Set the attributes model, year, and max_speed in the `__init__()` method.
# 2. Have a method that increases the `max_speed` of the car by 5 when called.
# 3. Have a method that prints the details of the car.
#
# Create at least two different objects of this `Car()` class and demonstrate
# changing the objects' attributes.

class Car:

    def __init__(self, make, model, year, max_speed):
        self.make = make
        self.model = model
        self.year = year
        self.max_speed = max_speed

    def speed_incr(self):
        self.max_speed += 5

    def __str__(self):
        return f"The {self.year} {self.make} {self.model} has a maximum speed of {self.max_speed} MPH."
    
b = Car("BWM", "540i", 2024, 155)
m = Car("Bugatti", "Chiron Super Sport", 2024, 300)

print(b)
print(m)

b.speed_incr()
m.speed_incr()

print(b)
print(m)

