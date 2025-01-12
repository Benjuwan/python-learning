def loop(f):
    for i in range(10):
        print(f(i), end=' ')

loop(lambda x: x*x)
