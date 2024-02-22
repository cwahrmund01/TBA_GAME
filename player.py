import item
import inventory

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



def player_from_json(json_player):
    pass