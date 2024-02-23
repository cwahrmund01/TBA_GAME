class Item():
    def __init__(self, name, is_one_time_use=False):
        self.name = name
        self.is_one_time_use = is_one_time_use

    def __str__(self):
        return self.name
    
    def __lt__(self, other):
        return self.name < other.name

    def __gt__(self, other):
        return self.name > other.name

    def __le__(self, other):
        return self.name <= other.name

    def __ge__(self, other):
        return self.name >= other.name

    def __eq__(self, other):
        return self.name == other.name

class Weapon(Item):
    def __init__(self, name, damage, is_one_time_use=False):
        super().__init__(name, is_one_time_use)
        self.damage = damage

    def __str__(self):
        return f"{self.name.capitalize()}, deals {self.damage} damage"

class Waterskin(Item):
    def __init__(self, name="waterskin", is_full=True):
        super().__init__(name)
        self.is_full = is_full
    
    def __str__(self):
        if self.is_full:
            return f"{self.name.capitalize()}, currently full of water"
        else:
            return f"{self.name.capitalize()}, currently empty"

class Lantern(Item):
    def __init__(self, name="lantern", rounds_of_fuel=100):
        super().__init__(name)
        self.rounds_of_fuel = rounds_of_fuel
    
    def __str__(self):
        return f"Lantern, has {self.rounds_of_fuel} more rounds of fuel"
    
    def is_empty(self):
        return self.rounds_of_fuel <= 0
    

def item_from_json(json_item):
    if json_item["type"].lower() == "weapon":
        return weapon_from_json(json_item)
    elif json_item["type"].lower() == "waterskin":
        return waterskin_from_json(json_item)
    elif json_item["type"].lower() == "lantern":
        return lantern_from_json(json_item)
    else:
        item_name = json_item["name"]
        one_time = json_item["one_time"]
        return Item(item_name, one_time)



def weapon_from_json(json_weapon):
    return Weapon(json_weapon["name"],
                  json_weapon["type_specific"]["damage"],
                  json_weapon["one_time"])

def waterskin_from_json(json_waterskin):
    return Waterskin(json_waterskin["name"],
                     json_waterskin["type_specific"]["is_full"])

def lantern_from_json(json_lantern):
    return Lantern(json_lantern["name"],
                   json_lantern["type_specific"]["fuel"])