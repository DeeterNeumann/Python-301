
class Stove:
    """Models the stove"""

    available_energy = ("gas", "electricity")

    def __init__(self, energy_source, num_burners):
        if energy_source not in self.available_energy:
            raise ValueError(f"The energy source must be one of the following: {self.available_energy}")
        self.energy_source = energy_source
        self.num_burners = num_burners

    oven_settings = ("bake", "broil", "convection", "roast", "preheat", "self-clean")
    
    def preheat_oven(self, setting, temp):
        if setting not in self.oven_settings:
            raise ValueError(f"Setting must be one of the following: {self.oven_settings}")
        self.setting = setting
        self.temp = temp
        print(f"The oven has been set to {self.setting} at a temp of {self.temp} degrees.")

    heat_level = ("high", "medium-high", "medium", "medium-low", "low")
    
    def burner_on(self, on_number, heat):
        if on_number > self.num_burners:
            raise ValueError(f"The burner number must be less than or equal to {self.num_burners}")
        self.on_number = on_number
        if heat not in self.heat_level:
            raise ValueError(f"The heat selection must be one of the following: {self.heat_level}")
        self.heat = heat
        print(f"The number {self.on_number} burner was turned on to {self.heat}")

    def burner_off(self, off_number):
        if off_number != self.on_number:
            print(f"{off_number} burner is not currently on. Turn off {self.on_number}.")
        elif off_number == self.on_number:
            print(f"burner number {off_number} has been turned off.")
        self.off_number = off_number

class Sink:
    """Models a sink"""

    def __init__(self, basins: int):
        self.basins = basins
        self.water_on = False
        self.flow = 0

    def faucet_on(self, flow):
        if not self.water_on:
            self.water_on = True
            print(f"you turned on the water.")
        else:
            print(f"the water is already running.")
        self.flow = flow
        print(f"the water is set to {self.flow}.")
    
    def faucet_off(self):
        if self.water_on:
            self.water_on = False
            print(f"you turned the water off")
        else:
            print(f"the water is not running.")
        self.flow = 0

# if parameter takes in values, what is the range to the parameter, and what happens

class Fridge:
    """Models a fridge"""

    def __init__(self, fridge, freezer):
        self.fridge = fridge
        self.freezer = freezer

    def clean(self, fridge):
        print(f"you have cleaned the fridge")
        cleaned = "clean " + self.fridge
        

    def defrost(self, freezer):
        print(f"you have defrosted the freezer.")
        defrosted = "defrosted " + self.freezer
        
    
class Countertop:

    def __init__(self, material):
        self.material = material

    def clean(self):
        print(f"you have cleaned the {self.material} counter.")

class Kitchen:

    def __init__(self, stove, sink, fridge, countertop):
        self.stove = stove
        self.sink = sink
        self.fridge = fridge
        self.countertop = countertop

stove = Stove("gas", 6)
sink = Sink(2)
fridge = Fridge("fridge", "freezer")
countertop = Countertop("marble")

s = Stove("gas", 4)

s.preheat_oven("bake", 375)

s.burner_on(4, "medium-high")

s.burner_off(4)

w = Sink(2)

w.faucet_on()

w.faucet_off()

f = Fridge("fridge", "freezer")

f.clean("fridge")

f.defrost("freezer")

c = Countertop("marble")

c.clean()

k = Kitchen(stove, sink, fridge, countertop)

k.sink.faucet_on()

k.sink.faucet_off()

k.sink.faucet_off()

k.sink.faucet_on()

k.sink.faucet_on()

k.fridge.defrost("freezer")

k.countertop.clean()

k.stove.preheat_oven("bake", 375)

k.stove.burner_on(4, "medium-high")

# code coupling
# less coupled, less breaks