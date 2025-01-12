class A:
    __slots__ = ['x', 'y']

a = A()
setattr(a, 'x', 123)
setattr(a, 'y', 456)
setattr(a, 'z', 789)
