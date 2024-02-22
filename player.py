import item

class Player():
    def __init__(self, name, inventory):
        self.name = name
        self.inventory = inventory

        self.health = 5

    def __str__(self):
        out = f"\nHello, {self.name}, you currently have {self.health} hit points. Currently, you are carrying: "
        for item in self.inventory.contents:
            out += "\n" + item
        out += "\n"
        return out

class Inventory():
    def __init__(self, *argv):
        self.contents = argv

        self.capacity = 10
        self.has_pack = False


def inventory_from_json(json_inventory):
    pass

def player_from_json(json_player):
    pass