class Map():

    def __init__(self):
        self.rooms = []


class Room():

    def __init__(self, north, south, east, west, contents=[], npcs=None):
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.contents = contents
        self.npcs = npcs