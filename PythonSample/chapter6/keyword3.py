def order(main, side, drink):
    print('main :', main)
    print('side :', side)
    print('drink:', drink)

dessert = {'main': 'parfait', 'side': 'cookie', 'drink': 'cocoa'}
order(**dessert)
