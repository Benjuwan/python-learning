try:
    print(1)
    try:
        print(2)
        1/0
        print(3)
    except ValueError:
        print(4)
    finally:
        print(5)
    print(6)
except ZeroDivisionError:
    print(7)
finally:
    print(8)
print(9)
