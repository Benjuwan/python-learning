def loop(f):
    for i in range(10):
        print(f(i), end=' ')

def square(x):
    return x*x

loop(square)
