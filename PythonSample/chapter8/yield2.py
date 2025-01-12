def g():
    for x in range(10):
        yield x*x

for y in g():
    print(y, end=' ')
