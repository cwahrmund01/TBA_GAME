import item
import inventory
import json
import os

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
    print(os.getcwd())
    with open("./save_states/initial.json") as f:
        data = json.load(f)
        json_player = data["player"]
        name = json_player["name"]
        health = json_player["health"]
        json_inventory = json_player["inventory"]