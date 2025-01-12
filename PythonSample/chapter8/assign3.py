t = 0
while True:
    x = input('price: ')
    if x == 'q':
        break
    t += int(x)
    print('total:', t)
