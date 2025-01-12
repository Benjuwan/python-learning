def order(main, side, drink):
    print('main :', main)
    print('side :', side)
    print('drink:', drink)

order('hotcake', *['fruit'], **{'drink': 'tea'})
