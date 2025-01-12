def g():
    for x in range(10):
        yield x*x

print(g())
