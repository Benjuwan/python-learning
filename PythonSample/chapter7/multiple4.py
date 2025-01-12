class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show(self):
        print('name:', self.name)
        print('price:', self.price)

class Food(Item):
    def __init__(self, use_by_date, **rest):
        super().__init__(**rest)
        self.use_by_date = use_by_date

    def show(self):
        super().show()
        print('use-by date:', self.use_by_date)

    def eat(self):
        print('eating', self.name)

class Toy(Item):
    def __init__(self, target_age, **rest):
        super().__init__(**rest)
        self.target_age = target_age

    def show(self):
        super().show()
        print('target age:', self.target_age)

    def play(self):
        print('playing with', self.name)

class Shokugan(Food, Toy):
    pass

x = Shokugan(name='chocolate+figure', price=450,
             use_by_date=180, target_age=3)
x.show()
x.eat()
x.play()
