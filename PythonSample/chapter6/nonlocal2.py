def f():
    def g():
        text = 'Good Night'
        print('g():', text)

    text = 'Good Morning'
    g()
    print('f():', text)

f()
