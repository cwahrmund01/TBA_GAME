class Map():

    def __init__(self):
        self.rooms = []


class Room():

    def __init__(self, description, name="", north=None, south=None, east=None, west=None, contents=[], npcs=[]):
        self.description = description
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.contents = contents
        self.npcs = npcs
    

    '''
    Room.get_<direction>_status methods:
    Each one is tests the current type of their respective direction.
    Depending on the type it finds, it returns a different integer for
    logic control when player attempts to move into a room.
    None: 0
    Room: 1
    Door, unlocked: 2
    Door, locked: 3
    Invalid type: -1

    Note to Self: when calling these functions, you could try using
    eval(f"self.get_{direction}_status()")
    when player is attempting to travel instead of using if statements.
    '''
    def get_north_status(self):
        if self.north == None:
            return 0
        elif type(self.north) == Room:
            return 1
        elif type(self.north) == Door:
            if not self.north.is_locked:
                return 2
            else:
                return 3
        else:
            print("Something went very wrong in Room.get_north_status")
            print(f"North is type {type(self.north)}")
            print("Code is saying it is not None, a Room, or a Door")
            return -1
        
    def get_south_status(self):
        if self.south == None:
            return 0
        elif type(self.south) == Room:
            return 1
        elif type(self.south) == Door:
            if not self.south.is_locked:
                return 2
            else:
                return 3
        else:
            print("Something went very wrong in Room.get_south_status")
            print(f"South is type {type(self.south)}")
            print("Code is saying it is not None, a Room, or a Door")
            return -1

    def get_east_status(self):
        if self.east == None:
            return 0
        elif type(self.east) == Room:
            return 1
        elif type(self.east) == Door:
            if not self.east.is_locked:
                return 2
            else:
                return 3
        else:
            print("Something went very wrong in Room.get_east_status")
            print(f"East is type {type(self.east)}")
            print("Code is saying it is not None, a Room, or a Door")
            return -1

    def get_west_status(self):
        if self.west == None:
            return 0
        elif type(self.west) == Room:
            return 1
        elif type(self.west) == Door:
            if not self.west.is_locked:
                return 2
            else:
                return 3
        else:
            print("Something went very wrong in Room.get_west_status")
            print(f"West is type {type(self.west)}")
            print("Code is saying it is not None, a Room, or a Door")
            return -1


class Door():
    
    def __init__(self, description, room_one, room_two, key_id=None, is_locked=True):
        self.description = description
        self.room_one = room_one
        self.room_two = room_two
        self.key_id = key_id
        self.is_locked = is_locked

    def get_other_room(self, current_room):
        if (current_room == self.room_one and current_room != self.room_two):
            return self.room_two
        elif (current_room != self.room_one and current_room == self.room_two):
            return self.room_one
        else:
            print("Door defined incorrectly")
            print(f"Door room_one is: {self.room_one.name}")
            print(f"Door room_two is: {self.room_two.name}")
            return False
    
    def try_key(self, attempted_key):
        if self.key_id == attempted_key.id:
            self.locked = not self.locked
            return True
        else:
            return False