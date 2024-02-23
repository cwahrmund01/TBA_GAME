import player
STARTING_INVENTORY = player.Inventory("waterskin", "knife", "lantern")

def main():
    print("Welcome to <title of game here>!")
    name = input("First, what is your name, adventurer? ").lower().capitalize()
    player_obj = player.Player(name, STARTING_INVENTORY)
    print(player_obj)

if __name__ == "__main__":
    main()