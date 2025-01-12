def count(*t, start=1, **d):
    for i, x in enumerate(t, start):
        print('[', i, ']', x)
    for i, (k, v) in enumerate(d.items(), len(t)+start):
        print('[', i, ']', k, ':', v)

count('hotcake', 'pizza', snack='parfait', dinner='steak', start=100)
count('hotcake', 'pizza', snack='parfait', dinner='steak')
