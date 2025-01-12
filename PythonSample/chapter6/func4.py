def odd_even(n):
    if n != int(n):
        return 'error'
    return 'odd' if n%2 else 'even'

print(odd_even(5))
print(odd_even(6))
print(odd_even(7.7))
