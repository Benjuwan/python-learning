def order(main, side, drink):
    print('main :', main)
    print('side :', side)
    print('drink:', drink)

order(main='steak', side='salad', drink='coffee')
order(main='steak', drink='coffee', side='salad')
order(side='salad', drink='coffee', main='steak')
order(side='salad', main='steak', drink='coffee')
order(drink='coffee', main='steak', side='salad')
order(drink='coffee', side='salad', main='steak')
