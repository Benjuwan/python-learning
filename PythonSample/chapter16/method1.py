class Color:
    def __init__(self, r, g, b):
        self.r, self.g, self.b = r, g, b

    def __str__(self):
        return f'({self.r}, {self.g}, {self.b})'

print(Color(255, 128, 0))
