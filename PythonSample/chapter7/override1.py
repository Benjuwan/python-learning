class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show(self):
        print('name:', self.name)
        print('price:', self.price)

class Food(Item):
    def __init__(self, name, price, use_by_date):
        super().__init__(name, price)
        self.use_by_date = use_by_date

    def show(self):
        super().show()
        print('use-by date:', self.use_by_date)

class Toy(Item):
    def __init__(self, name, price, target_age):
        super().__init__(name, price)
        self.target_age = target_age

    def show(self):
        super().show()
        print('target age:', self.target_age)

x = Food('chocolate', 100, 180)
x.show()

print()

y = Toy('figure', 350, 3)
y.show()
