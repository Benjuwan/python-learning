# python dice.py で処理実行
# Mac では python3 dice.py で処理実行

import random
import math

# 1～6までの数値を出すダイス
print("random", random.randint(1, 6))

print("total", (100 + 50) / 2, type((100 + 50) / 2))

exNum = (100 + 60) / 2
exNum_int = math.floor(exNum)
print("total", exNum, exNum_int, type(exNum_int))

# 改行
print()
for i in range(10):
    print(i, end=" | ")

for i in range(10):
    print(i, end="")

# 改行
# print()
for c in " - Python Programing":
    print(c, end="")

# 改行
print()
print("benjuwan\njijao", len("benjuwan jijao"))
print("BenjuwanJijao", len("Benjuwan") + len("Jijao"))

# 改行
print()
# print("\hoge\Foo\\bar")
print("raw文字列", r"\hoge\Foo\\bar")

# 改行
print()
print("-".join(str(i) for i in range(random.randint(1, 25))))

# 改行
print()
print("Don\"t stop 'my love'.")

# 改行
print()
for i in range(3):
    print("start")
    print("stop")

# 改行
print()
x, y, z = 123, 4.56, "789"
print(x, y, z)

# 単数記述でないと型注釈できない
a: int | bool | str = 123
b: int = 123
idCheck = id(x) == id(a) == id(b)
print(id(x), id(a), id(b), idCheck)  # 参照値はすべて同じ

x = 19910228
# 以下をコメントアウトすると再代入（変更）前の参照値で評価される
idCheck = id(x) == id(a) == id(b)

print(id(x), id(a), id(b), idCheck)  # x の参照値以外はすべて同じ

a = True
print(a)
a = "hoge"
print(a)
