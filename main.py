import player
import json

def import_initial_game_state(player_name):
    with open("./save_states/initial.json", "r") as init_file:
        game_data = json.load(init_file)
        json_player = game_data["player"]
        json_rooms = game_data["rooms"]
        json_npcs = game_data["npcs"]

        PLAYER = player.player_from_json(json_player, name=player_name)
        return PLAYER

def main():
    print("Welcome to Cedric's Text Based Adventure Game!")
    name = input("First, what is your name, adventurer? ").lower().title()
    PLAYER = import_initial_game_state(name)

if __name__ == "__main__":
    main()