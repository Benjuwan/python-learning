def count(*t, **d):
    for i, x in enumerate(t, 1):
        print('[', i, ']', x)
    for i, (k, v) in enumerate(d.items(), len(t)+1):
        print('[', i, ']', k, ':', v)

count('hotcake', 'pizza', snack='parfait', dinner='steak')
