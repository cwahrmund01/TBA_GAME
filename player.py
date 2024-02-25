import item
import inventory
import json

class Player():
    def __init__(self, name, health, inventory):
        self.name = name
        self.inventory = inventory

        self.health = 5

    def __str__(self):
        out = f"\nHello, {self.name}, you currently have {self.health} hit points. Currently, you are carrying: "
        for item in self.inventory.contents:
            out += "\n" + item
        out += "\n"
        return out



def player_from_json(json_player, name=None):
    with open("./save_states/initial.json") as f:
        name = json_player["name"]
        health = json_player["health"]
        json_inventory = json_player["inventory"]
        inv = inventory.inventory_from_json(json_inventory)

        return Player(name, health, inv)