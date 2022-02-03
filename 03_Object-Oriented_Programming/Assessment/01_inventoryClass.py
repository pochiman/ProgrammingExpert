##### Inventory Class #####

# Write an Inventory class, as defined below, that handles the management of inventory for a company.
# All instances of this class should be initialized by passing an integer value named max_capacity that 
# indicates the maximum number of items that can be stored in inventory.  Your Inventory class will need 
# to store items that are represented by a name, price and quantity.

# Your class should implement the following methods.

##### add_item(name, price, quantity): This method should add an item to inventory and return True if it was 
##### successfully added.  If adding an item results in the inventory being over capacity, your method should 
##### return False and omit adding this item to the inventory.  Additionally, if an item with the passed name 
##### already exists in inventory, this method should return False to indicate the item could not be added.

##### delete_item(name): This method should delete an item from inventory and return True if the item was 
##### successfully deleted.  If there is no item with the passed name, this method should return False.

##### get_most_stocked_item(): This method should return the name of the item that has the highest quantity in 
##### the inventory, and return None if there are no items in the inventory.  You may assume there will always 
##### be exactly one item with the largest quantity, except for the case where the inventory is empty.

##### get_items_in_price_range(min_price, max_price): This method should return a list of the names of items 
##### that have a price within the specified range (inclusively).

# Note: you may assume all input/arguments to your class will be valid and the correct types.
# For example, the max_capacity will always be greater than or equal to 0 and a valid integer.

# See below for an example of how the Inventory class should behave.

# >>> i = Inventory(4)
# >>> i.add_item('Chocolate', 4.99, 1)
# True
# >>> i.add_item('Cereal', 6.99, 1)
# True
# >>> i.add_item('Milk', 3.99, 2)
# True
# >>> i.add_item('Butter', 2.99, 1)
# False
# >>> i.delete_item('Bread')
# False
# >>> i.delete_item('Cereal')
# True
# >>> i.get_items_in_price_range(4.50, 6.50)
# ['Chocolate']

class Inventory:
    def __init__(self, max_capacity):
        self.max_capacity = max_capacity
        self.items = {}
        self.item_count = 0

    def add_item(self, name, price, quantity):
        if name in self.items:
            return False

        if self.item_count + quantity > self.max_capacity:
            return False

        self.items[name] = {"name": name, "price": price, "quantity": quantity}
        self.item_count += quantity
        return True

    def delete_item(self, name):
        if name not in self.items:
            return False

        self.item_count -= self.items[name]["quantity"]
        del self.items[name]
        return True

    def get_items_in_price_range(self, min_price, max_price):
        item_names = []

        for item in self.items.values():
            name = item["name"]
            price = item["price"]

            if min_price <= price <= max_price:
                item_names.append(name)

        return item_names

    def get_most_stocked_item(self):
        most_stocked_item_name = None
        largest_quantity = 0

        for item in self.items.values():
            name = item["name"]
            quantity = item["quantity"]

            if quantity > largest_quantity:
                most_stocked_item_name = name
                largest_quantity = quantity

        return most_stocked_item_name