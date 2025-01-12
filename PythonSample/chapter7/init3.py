class Food:
    def __init__(self, name, price):
        self.name = name
        self.price = price

x = Food('milk', 150)
print(x.name, x.price)

y = Food('egg', 200)
print(y.name, y.price)
