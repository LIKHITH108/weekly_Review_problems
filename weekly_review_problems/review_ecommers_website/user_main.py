from item_cart_class import Cart,Item

class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.cart = []

    def add_to_cart(self, item, quantity):
        
        for cart_item in self.cart:
            if cart_item.item.id == item.id:
                cart_item.quantity += quantity
                cart_item.total_price = cart_item.item.price * cart_item.quantity
                item.update_quantity(quantity)
                return
        
        
        self.cart.append(Cart(item, quantity))
        item.update_quantity(quantity)

    
    def cal_cart_value(self):
        total_value = sum(cart_item.total_price for cart_item in self.cart)
        return total_value
    
a = Item(1,"pen", 50000, 3)
b = Item(2,"oencil", 500, 9)


userr = User(1,"Likhith")


userr.add_to_cart(a, 2)
userr.add_to_cart(b, 3)


print(f"Total cart value of is : {userr.cal_cart_value()}")
