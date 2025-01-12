def leap_year(y):
    return y%400 == 0 or y%100 != 0 and y%4 == 0

assert not leap_year(1900)
assert leap_year(2000)
assert not leap_year(2019)
assert leap_year(2020)
