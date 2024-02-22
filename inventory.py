import item

class Inventory():
    def __init__(self, *argv):
        self.contents = argv

        self.capacity = 10
        self.has_pack = False


def inventory_from_json(json_inventory):
    pass