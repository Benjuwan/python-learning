while True:
    try:
        price = int(input('price: '))
        if price < 0:
            raise Exception('The price must be >= 0.')
        count = int(input('count: '))
        print('price//count =', price//count)
    except ValueError:
        print('Input an integer.')
    except ZeroDivisionError:
        print('The count must be != 0.')
    except Exception as e:
        print(e)
    else:
        print('Thank you.')
    finally:
        print('-'*25)
