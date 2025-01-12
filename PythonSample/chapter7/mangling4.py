class Food:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def show(self):
        print(self.__name, self.__price)

x = Food('milk', 150)
x.price //= 2
x.show()
