class Food:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show(self):
        print(self.name, self.price)

x = Food('milk', 150)
x.show()

y = Food('egg', 200)
y.show()
