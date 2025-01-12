def f():
    global text
    text = 'Good Bye'
    print('f():', text)

text = 'Hello'
f()
print(text)
