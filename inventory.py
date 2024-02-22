import item

class Inventory():
    def __init__(self, *argv):
        self.contents = argv

        self.capacity = 10
    
    def __str__(self):
        pass

    def sort_contents():
        pass

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
        self.contents.append(item)

def inventory_from_json(json_inventory):
    pass