class Item:
    def __init__(self, id, name, price, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

    def update_quantity(self, quantity):
        self.quantity -= quantity


class Cart:
    def __init__(self, item, quantity):
        self.item = item
        self.quantity = quantity
        self.total_price = item.price * quantity