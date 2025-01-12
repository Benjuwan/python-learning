def my_range(start, stop):
    x = start
    while x < stop:
        yield x
        x += 1

for y in my_range(100, 110):
    print(y, end=' ')
