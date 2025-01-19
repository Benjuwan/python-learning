# チャプター3章まで

import random
import math

# 区切り（兼改行）用の文字列
duplicateCounter: int = 0
duplicateStr: str = "-+-"


# 区切り（兼改行）用の文字列を表示する関数
def duplicateCount(duplicateCounter: int):
    if duplicateCounter == 1:
        print("\n", str(duplicateCounter), duplicateStr * 20, "\n")
    else:
        print(str(duplicateCounter), duplicateStr * 20, "\n")


print("total", (100 + 50) / 2, type((100 + 50) / 2))

exNum = (100 + 60) / 2
exNum_int = math.floor(exNum)
print("exNum_int total", exNum, exNum_int, type(exNum_int))

# 改行
print()
for i in range(10):
    print(i, end=" | ")

for i in range(10):
    print(i, end="")

duplicateCounter += 1
duplicateCount(duplicateCounter)
for c in " - Python Programing":
    print(c, end="")

# 改行
print()
print("benjuwan\njijao", len("benjuwan jijao"))
print("BenjuwanJijao", len("Benjuwan") + len("Jijao"))

duplicateCounter += 1
duplicateCount(duplicateCounter)
# print("\hoge\Foo\\bar")
print("raw文字列", r"\hoge\Foo\\bar")

duplicateCounter += 1
duplicateCount(duplicateCounter)
print("-".join(str(i) for i in range(random.randint(1, 25))))

duplicateCounter += 1
duplicateCount(duplicateCounter)
print("Don\"t stop 'my love'.")

duplicateCounter += 1
duplicateCount(duplicateCounter)
for i in range(3):
    print("start")
    print("stop")

duplicateCounter += 1
duplicateCount(duplicateCounter)
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

duplicateCounter += 1
duplicateCount(duplicateCounter)

for i in range(10):
    isOdd: bool = i % 2 == 1
    isEven: bool = i % 2 == 0
    if isOdd:
        print("奇数", i)
    elif isEven:
        print("偶数", i)

duplicateCounter += 1
duplicateCount(duplicateCounter)
