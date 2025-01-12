def f():
    def g():
        nonlocal text
        text = 'Good Night'
        print('g():', text)

    text = 'Good Morning'
    g()
    print('f():', text)

f()
