# Build on your freeform exercise from the previous section.
# Create child classes of two of the existing classes. Create a child class
# of one of the child classes so that the hierarchy is at least three levels.
#
# Build these classes out step-by-step like you did in the previous exercises.
# Use your notebook to brainstorm ideas and scribble down ideas.
#
# If you cannot think of a way to build on your freeform exercise,
# you can start with a new class from scratch.
# Try to make up your own example for this exercise, but if you are stuck,
# you could start working on the following:
#
# - A `Vehicle()` parent class, with `Truck()` and `Motorcycle()` child classes.
# - A `Restaurant()` parent class, with `Gourmet()` and `FastFood()` child classes.

class HealthSystem:

    def __init__(self, name, year_est):
        self.name = name
        self.year_est = year_est
        
class Hospital(HealthSystem):

    trauma_levels = (1, 2, 3, 4)

    def __init__(self, name, year_est, level: int):
        super().__init__(name, year_est)
        if level not in self.trauma_levels:
            raise ValueError(f"Level must be one of the following: {self.trauma_levels}.")
        else:
            self.level = level
    
    def life_threatening(self):
        if self.level == 1:
            print(f"{self.name} is capable of triaging a life-threatening emergency.")
        else:
            print(f"{self.name} is a level {self.level} trauma center and cannot triage a life-threatening situation.")

class Clinic(HealthSystem):

    def __init__(self, name, year_est, insurance_accepted: list[str]):
        super().__init__(name, year_est)
        self.insurance_accepted: list[str] = insurance_accepted

    def acute_eval():
        print(f"The patient requires an evaluation for an acute medical issue. Consider transferring to {Hospital.name}, if needed")

    def add_insurance(self, new_insurance):
        self.insurance_accepted.append(new_insurance)
        print(f"{self.name} accepts the following insurances: {self.insurance_accepted}.")
    
class Oncology(Clinic):

    def __init__(self, name, year_est, insurance_accepted: list[str], onc_specialties: list[str]):
        super().__init__(name, year_est, insurance_accepted)
        self.onc_specialties: list[str] = onc_specialties

    def add_specialty(self, new_specialty):
        self.onc_specialties.append(new_specialty)
        print(f"{self.name} provides care for the following: {self.onc_specialties}.")

h = Hospital("Harborview", 1968, 1)

h.life_threatening()

u = Hospital("UW", 1954, 3)

u.life_threatening()

f = Oncology("FHCC", 1975, ["Medicare", "Medicaid", "BCBS"], ["heme", "GI", "HCT", "IMTX"])

f.add_specialty("THN")

f.add_insurance("Aetna")