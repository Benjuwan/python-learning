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

    def eat(self):
        print('eating', self.name)

class Toy(Item):
    def __init__(self, name, price, target_age):
        super().__init__(name, price)
        self.target_age = target_age

    def show(self):
        super().show()
        print('target age:', self.target_age)

    def play(self):
        print('playing with', self.name)

class Shokugan(Food, Toy):
    def __init__(self, name, price,
                 use_by_date, target_age):
        self.name = name
        self.price = price
        self.use_by_date = use_by_date
        self.target_age = target_age

    def show(self):
        super().show()

print(Food.__mro__)
