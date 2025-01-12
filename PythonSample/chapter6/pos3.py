def order(main, side, drink):
    print('main :', main)
    print('side :', side)
    print('drink:', drink)

snack = ['hotcake', 'fruit']
order(*snack, 'tea')
