# A good way to think about how classes are blueprints of objects is to think of
# an empty form, for example one that you would get at a doctor's office.
# The empty form contains all the placeholders that define what information
# you need to fill to complete the form. If you fill it correctly, then you've
# successfully instantiated a form object, and your completed form now holds
# information that is specific to just you.
# Another patient's form will follow the same blueprint, but hold different info.
# You could say that every patient's filled form instance is part of the same
# empty form blueprint class that the doctor's office provided.
#
# Model such an application form as a Python class below, and instantiate
# a few objects from it.

import datetime


# create a list that can be appended

class Form:
    
    """Creates a form to filled out"""
    def __init__(self, last_name, first_name, dob, allergies: list[str]):
        self.last_name = last_name
        self.first_name = first_name
        self.dob = dob
        self.allergies: list[str] = allergies

    def __str__(self):
        return f"Last name: {self.last_name}, First name: {self.first_name}; Date of Birth: {self.dob}; Allergies: {self.allergies}"
    
    def calc_age(self):
        today = datetime.date.today()
        age = today.year - int(self.dob[6:10]) - ((today.month, today.day) < (int(self.dob[0:2]), int(self.dob[3:5])))
        return f"Last name: {self.last_name}, First name: {self.first_name}; Age: {age}"

    def add_allergy(self, new_allergy):
        self.allergies.append(new_allergy)
        print(self.allergies)
        
a = Form("Smith", "John", "09/19/1957",["penicillin"])
b = Form("Wright", "Jack", "08/19/1968", ["bactrim"])

print(a)
print(b)

print(a.calc_age())
print(b.calc_age())

a.add_allergy("bactrim")

print(a)

print(a.allergies)