def order(main, side, drink):
    print('main :', main)
    print('side :', side)
    print('drink:', drink)

order(*['parfait'], **{'drink': 'cocoa'}, side='cookie')
