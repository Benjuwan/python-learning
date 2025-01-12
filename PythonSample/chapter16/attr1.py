class A:
    pass

a = A()
setattr(a, 'x', 123)
print(getattr(a, 'x'))
print(hasattr(a, 'x'))
delattr(a, 'x')
print(hasattr(a, 'x'))
