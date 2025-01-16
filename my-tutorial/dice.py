#  python dice.py で処理実行

import random

# 1～6までの数値を出すダイス
print("random", random.randint(1, 6))

print("total", (100 + 50) / 2, type((100 + 50) / 2))
print("total", (100 + 60) / 2, type((100 + 60) / 2))

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
print("\hoge\Foo\\bar")
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
