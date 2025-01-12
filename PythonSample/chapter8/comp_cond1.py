a = []
for x in range(1, 16):
    if x%15 == 0:
        a.append('Fizz Buzz')
    elif x%5 == 0:
        a.append('Buzz')
    elif x%3 == 0:
        a.append('Fizz')
    else:
        a.append(x)
print(a)
