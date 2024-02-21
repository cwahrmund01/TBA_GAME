class Item():
    def __init__(self, name):
        self.name = name


class Weapon(Item):
    def __init__(self, name, damage, one_time=False):
        super().__init__(name)
        self.damage = damage
        self.one_time = one_time