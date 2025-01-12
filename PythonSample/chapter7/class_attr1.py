class Food:
    count = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Food.count += 1

    def show(self):
        print(Food.count, self.name, self.price)

x = Food('milk', 150)
x.show()

y = Food('egg', 200)
y.show()
