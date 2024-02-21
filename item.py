class Item():
    def __init__(self, name):
        self.name = name


class Weapon(Item):
    def __init__(self, name, damage, is_one_time_hit=False):
        super().__init__(name)
        self.damage = damage
        self.is_one_time_hit = is_one_time_hit

class Waterskin(Item):
    def __init__(self, name="waterskin", is_full=True):
        super().__init__(name)
        self.is_full = is_full

class Lantern(Item):
    def __init__(self, name="lantern", rounds_of_fuel=100):
        super().__init__(name)
        self.rounds_of_fuel = rounds_of_fuel
    
    def __str__(self):
        print(f"Your lantern will burn for {self.rounds_of_fuel} more moves.")