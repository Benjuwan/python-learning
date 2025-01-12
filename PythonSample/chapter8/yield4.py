def my_range(start, stop):
    x = start
    while x < stop:
        yield x
        x += 1

def my_range2(start, stop, count):
    for i in range(count):
        yield from my_range(start, stop)

for y in my_range2(1, 10, 3):
    print(y, end=' ')
