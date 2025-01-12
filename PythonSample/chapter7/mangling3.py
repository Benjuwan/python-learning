class Food:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def show(self):
        print(self._name, self._price)

x = Food('milk', 150)
x._price //= 2
x.show()
