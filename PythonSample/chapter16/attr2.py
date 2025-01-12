class A:
    pass

a = A()
setattr(a, 'x', 123)

print(dir(a))
print(vars(a))
