def f():
    x = 123
    print('locals:', locals())

f()
y = 456
print('globals:', globals())
