class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

x = Item('burger', 100)
print(x.name, x.price)
