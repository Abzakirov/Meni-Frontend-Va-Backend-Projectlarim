class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Shop:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product):
        self.items.append(product)

    def calculate_total(self):
        total = sum(item.price for item in self.items)
        return total

def checkout(cart):
    total = cart.calculate_total()
    print("Total: $" + str(total))


mars_shop = Shop()
product1 = Product("Shirt", 20)
product2 = Product("Pants", 30)
mars_shop.add_product(product1)
mars_shop.add_product(product2)


cart = ShoppingCart()
cart.add_item(product1)
cart.add_item(product2)

checkout(cart)
