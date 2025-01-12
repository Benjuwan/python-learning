while True:
    try:
        price = int(input('price: '))
        count = int(input('count: '))
        print('price//count =', price//count)
    except ValueError:
        print('Input an integer.')
    except ZeroDivisionError:
        print('The count must be != 0.')
    print('-'*25)
