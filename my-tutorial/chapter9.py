# チャプター 9

# 区切り（兼改行）用の文字列
duplicate_counter: int = 0
duplicate_str: str = "-+-"


# 区切り（兼改行）用の文字列を表示する関数
def duplicate_count(duplicate_counter: int):
    if duplicate_counter == 1:
        print(f"\n{str(duplicate_counter)} {duplicate_str * 20} \n")
    else:
        print(f"{str(duplicate_counter)} {duplicate_str * 20} \n")


duplicate_counter += 1
duplicate_count(duplicate_counter)

float_elm = 1 / 3
print(format(float_elm))
print(format(float_elm, ".2f"))
print(f"{1 / 3:.2f}")

# 千の位ごとに ,を挿入
print(format(100000000000000000, ","))

# 千の位ごとに _を挿入
print(format(100000000000000000, "_"))

print(abs(123))
print(abs(-456))
print(abs(12.3))
print(abs(-12.3))

print(divmod(30, 5))
print(divmod(53, 3))

print(pow(2, 3))  # 2の3乗
print(pow(2, 3, 5))  # 2の3乗を5で割った余り

print(round(1 / 3))  # 0
print(round(1 / 3, 2))  # 0.33

print(round(3 / 2))  # 2
print(round(3 / 2, 2))  # 1.5

print(round(123, -1))  # 120
print(round(123, -2))  # 100
print(round(123, -3))  # 0

print(min("blue", "red", "green"))  # blue
print(max("blue", "red", "green"))  # red

want_sum_numbers = [90, 75, 80, 100, 85]
print(sum(want_sum_numbers))  # 430
print(sum(want_sum_numbers) / 5)  # （平均値）86.0
print(sum(want_sum_numbers) // 5)  # （平均値）86

food_name = ["burger", "potato", "snack"]
food_price = [90, 150, 120]

for food in zip(food_name, food_price):
    print(f"{food[0]} is {food[1]} yen.")

for n, p in zip(food_name, food_price):
    print(f"{n} is {p} yen.")

print(list(zip(food_name, food_price)))

print(list(map(len, food_name)))  # [6, 6, 5]
convert_str_list = list(map(str, food_price))
print(list(map(len, convert_str_list)))  # [2, 3, 3]

fruits = ["apple", "", "grape", "melon", "", "", "water-melon"]
print(len(fruits))  # 7

print(list(filter(len, fruits)))
# ['apple', 'grape', 'melon', 'water-melon']

print(len(list(filter(len, fruits))))  # 4

person_a_socre = [90, 75, 88, 100, 82]
person_b_socre = [90, 85, 98, 100, 96]
print(all([score > 80 for score in person_a_socre]))  # False
print(all([score > 80 for score in person_b_socre]))  # True
print(any([score < 80 for score in person_a_socre]))  # True
print(any([score < 80 for score in person_b_socre]))  # False


some_numbers = [1, 2, 3]
iterator = iter(some_numbers)
print(next(iterator))
print(next(iterator))
print(next(iterator))
# print(next(iterator))  # next が無いので StopIteration 発生

print(bin(123))  # 0b1111011
print(oct(123))  # 0o173
print(hex(123))  # 0x7b

print(f"{123:b}")  # 1111011
print(f"{123:#b}")  # 0b1111011
print(f"{123:o}")  # 173
print(f"{123:#o}")  # 0o173
print(f"{123:x}")  # 7b
print(f"{123:#x}")  # 0x7b

representation = repr("Python")  # 'Python'
print(representation)
representation = repr("パイソン")  # 'パイソン'
print(representation)

ascii_no_esc = ascii("Python")  # 'Python'
print(ascii_no_esc)
ascii_esc = ascii("パイソン")  # '\u30d1\u30a4\u30bd\u30f3'
print(ascii_esc)

print(isinstance(123, int))  # True
print(isinstance("123", int))  # False
print(isinstance("123", str))  # True
print(isinstance(3.14, float))  # True
