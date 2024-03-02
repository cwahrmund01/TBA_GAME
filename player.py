import item
import inventory
import map

class Player():
    def __init__(self, name, health, inventory, current_room):
        self.name = name
        self.health = health
        self.inventory = inventory
        self.current_room = current_room

        self.max_health = 5

    def __str__(self):
        out = f"\nHello, {self.name}, you currently have {self.health} hit points.\n"
        out += str(self.inventory)
        return out
    
    def move_north(self):
        pass

    def move_south(self):
        pass

    def move_east(self):
        pass

    def move_west(self):
        pass

    def check_inventory(self):
        pass

    def pickup_item(self, item):
        pass
    
    def pickup_item_by_name(self, item_name):
        pass

    def drop_item(self, item):
        pass
    
    def drop_item_by_name(self, item_name):
        pass

    def look(self):
        pass

    def check_self(self):
        print(str(self))

    def try_key(self, key):
        pass

    def attack(self, weapon, target_npc):
        pass

    def take_damage(self, damage_taken):
        self.health = max(self.health - damage_taken, 0)
    
    def heal(self, heal_amount):
        self.health = min(self.health + heal_amount, self.max_health)
    
    def is_alive(self):
        return self.health > 0



def player_from_json(json_player, name=None):
    with open("./save_states/initial.json") as f:
        name = json_player["name"]
        health = json_player["health"]
        json_inventory = json_player["inventory"]
        inv = inventory.inventory_from_json(json_inventory)

        return Player(name, health, inv)