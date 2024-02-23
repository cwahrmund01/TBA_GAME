import item

class Inventory():
    def __init__(self, *argv):
        self.contents = list(argv)

        self.capacity = 12
    
    def __str__(self):
        number_of_items = self.get_number_items()
        out_string = f"Inventory Contents ({number_of_items}/{self.capacity}): \n"
        for itm in self.contents:
            out_string += f"{str(itm)}\n"
        return out_string

    def sort_contents(self):
        self.contents = sorted(self.contents)

    def get_number_items(self):
        return len(self.contents)
    
    def inventory_is_full(self):
        return self.get_number_items() == self.capacity

    def get_item_by_name(self, item_name):
        for i in range(self.get_number_items()):
            if self.contents[i].name == item_name:
                return self.contents[i]
        
        return None

    def get_item_index_by_name(self, name):
        for i in range(self.get_number_items()):
            if self.contents[i].name == name:
                return i
        
        return None

    def remove_item(self, item):
        index = self.get_item_index_by_name(item.name)
        self.contents.pop(index)
    
    def remove_item_by_name(self, item_name):
        index = self.get_item_index_by_name(item_name)
        self.contents.pop(index)

    def add_item(self, item):
        if self.inventory_is_full():
            return False
        else:
            self.contents.append(item)
            self.sort_contents()
            return True

def inventory_from_json(json_inventory):
    inv = Inventory()
    for _, json_item in json_inventory.items():
        new_item = item.item_from_json(json_item)
        inv.add_item(new_item)

    return inv
