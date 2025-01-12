class Color:
    def __init__(self, r, g, b):
        self.r, self.g, self.b = r, g, b

    def __str__(self):
        return f'({self.r}, {self.g}, {self.b})'

    @staticmethod
    def cyan():
        return Color(0, 255, 255)

    @classmethod
    def aqua(cls):
        return cls.cyan()

print(Color.aqua())
