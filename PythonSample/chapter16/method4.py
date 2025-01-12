class Color:
    def __init__(self, r, g, b):
        self.r, self.g, self.b = r, g, b

    def __str__(self):
        return f'({self.r}, {self.g}, {self.b})'

    @classmethod
    def cyan(cls):
        return Color(0, 255, 255)

print(Color.cyan())
