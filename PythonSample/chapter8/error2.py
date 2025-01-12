while True:
    price = input('price: ')
    if not price.isnumeric():
        print('Input an integer.')
        print('-'*25)
        continue
    count = input('count: ')
    if not count.isnumeric():
        print('Input an integer.')
        print('-'*25)
        continue
    price = int(price)
    count = int(count)
    if count == 0:
        print('The count must be != 0.')
        print('-'*25)
        continue
    print('price//count =', price//count)
    print('-'*25)
