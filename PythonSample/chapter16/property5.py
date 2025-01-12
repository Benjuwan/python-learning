class Item:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = max(value, 0)

x = Item('burger', 100)
print(x.name, x.price)

x.price = 110
print(x.name, x.price)

x.price = -100
print(x.name, x.price)
