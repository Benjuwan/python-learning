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
