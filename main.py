import player
import json

PLAYER = None
MAP = None
NPCS = None

def import_initial_game_state():
    with open("./save_states/initial.json", "r") as init_file:
        game_data = json.load(init_file)
        json_player = game_data["player"]
        json_rooms = game_data["rooms"]
        json_npcs = game_data["npcs"]

        PLAYER = player.player_from_json(json_player)

def main():
    # print("Welcome to <title of game here>!")
    # name = input("First, what is your name, adventurer? ").lower().capitalize()
    # player_obj = player.Player(name, STARTING_INVENTORY)
    # print(player_obj)

    p1 = player.player_from_json(1)

    print(p1.name)
    print(p1.inventory)
    p1.inventory.sort_contents()
    print(p1.inventory)

if __name__ == "__main__":
    main()