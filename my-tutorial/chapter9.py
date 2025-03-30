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
food_price = [110, 150, 120]

for food in zip(food_name, food_price):
    print(f"{food[0]} is {food[1]} yen.")

for n, p in zip(food_name, food_price):
    print(f"{n} is {p} yen.")
