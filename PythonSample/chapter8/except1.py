while True:
    try:
        price = int(input('price: '))
        count = int(input('count: '))
        print('price//count =', price//count)
    except (ValueError, ZeroDivisionError):
        print('Error.')
    print('-'*25)
