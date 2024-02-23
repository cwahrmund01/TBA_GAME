import player
#STARTING_INVENTORY = player.inventory("waterskin", "knife", "lantern")

def main():
    # print("Welcome to <title of game here>!")
    # name = input("First, what is your name, adventurer? ").lower().capitalize()
    # player_obj = player.Player(name, STARTING_INVENTORY)
    # print(player_obj)

    player.player_from_json(1)

if __name__ == "__main__":
    main()