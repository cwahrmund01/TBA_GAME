class Item():
    def __init__(self, name, is_one_time_use=False):
        self.name = name
        self.is_one_time_use = is_one_time_use

    def __str__(self):
        return self.name

class Weapon(Item):
    def __init__(self, name, damage, is_one_time_use=False):
        super().__init__(name, is_one_time_use)
        self.damage = damage

class Waterskin(Item):
    def __init__(self, name="waterskin", is_full=True):
        super().__init__(name)
        self.is_full = is_full

class Lantern(Item):
    def __init__(self, name="lantern", rounds_of_fuel=100):
        super().__init__(name)
        self.rounds_of_fuel = rounds_of_fuel
    
    def __str__(self):
        return f"Your lantern will burn for {self.rounds_of_fuel} more moves."
    
    def is_empty(self):
        return self.rounds_of_fuel <= 0
    

def item_from_json(json_item):
    pass