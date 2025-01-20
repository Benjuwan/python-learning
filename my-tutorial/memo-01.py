# チャプター3章まで

import random
import math

# 区切り（兼改行）用の文字列
duplicateCounter: int = 0
duplicateStr: str = "-+-"


# 区切り（兼改行）用の文字列を表示する関数
def duplicateCount(duplicateCounter: int):
    if duplicateCounter == 1:
        print("\n" + str(duplicateCounter), duplicateStr * 20, "\n")
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

hellotxt = "hello.txt"
print(len(hellotxt), len(hellotxt) - 1)
print(hellotxt[len(hellotxt) - 1])
print(hellotxt.split("."))

# JavaScript での join は、要素を適用対象にして join 関数の引数にデリミタを指定する
# const helloTxt = 'hello.txt'
# console.log(helloTxt.split('.').join(''))

# Python での join は、デリミタ（区切り文字）を適用対象にして join 関数の引数に要素を指定する（＝ JavaScript と逆のアプローチ方法）
pythonJoin = "".join(hellotxt.split("."))
print(pythonJoin, id(pythonJoin))

sameStr_hellotxt_01: str = (
    hellotxt.split(".")[0] + hellotxt.split(".")[len(hellotxt.split(".")) - 1]
)
sameStr_hellotxt_02: str = hellotxt.replace(".", "")
sameStr_hellotxt: bool = id(sameStr_hellotxt_01) == id(sameStr_hellotxt_02)
print(id(hellotxt), id(sameStr_hellotxt_01), id(sameStr_hellotxt_02))
print(sameStr_hellotxt_01, sameStr_hellotxt_02, sameStr_hellotxt)

hellotxt_hyphon: str = hellotxt.replace(".", "-")
print(hellotxt_hyphon)

duplicateCounter += 1
duplicateCount(duplicateCounter)

welcome = "-W-e-l-c-m-o-m-e-."
# upper 大文字, lower 小文字
print("".join(welcome.upper().split("-")))
# replace(対象文字, 置換文字, 個数)
print(
    math.floor(len(welcome) / 2), welcome.replace("-", "", math.floor(len(welcome) / 2))
)

anaconda = "anaconda"
print(anaconda.replace("a", "A"))
print(anaconda.replace("a", "A", 1))
print(anaconda.replace("a", "A", 2))

duplicateCounter += 1
duplicateCount(duplicateCounter)

pathName = "/posts/animals/cat"
# 文字列の先頭が引数に指定した文字列と一致するかどうか
isPathNameStr: bool = pathName.startswith("/")
# 文字列の末尾が引数に指定した文字列と一致するかどうか
isCatPost: bool = pathName.endswith("dog")
print(isPathNameStr, isCatPost)

duplicateCounter += 1
duplicateCount(duplicateCounter)

pythonCreatorName = "Guido van Rossum"
theFirstName = pythonCreatorName.split(" ")[0]
findFirstName = pythonCreatorName.find(theFirstName)
findFirstNameIndex = pythonCreatorName.index(theFirstName)
print(theFirstName, findFirstName, findFirstNameIndex)

theMiddleName = pythonCreatorName.split(" ")[1]
findMiddleName = pythonCreatorName.find(theMiddleName)
findMiddleNameIndex = pythonCreatorName.index(theMiddleName)
print(theMiddleName, findMiddleName, findMiddleNameIndex)

# isExist3rdStr: bool = pythonCreatorName.split(" ")[2] is not None
isNotExist3rdStr: bool = pythonCreatorName.split(" ")[2] is None
print(isNotExist3rdStr)

theFamilyName = pythonCreatorName.split(" ")[2]
findFamilyName = pythonCreatorName.find(theFamilyName)
findFamilyNameIndex = pythonCreatorName.index(theFamilyName)
print(theFamilyName, findFamilyName, findFamilyNameIndex)


duplicateCounter += 1
duplicateCount(duplicateCounter)

# count 対象要素（文字列）に引数に指定した文字が何文字あるか
print("internationalization".count("i"))
print("internationalization".count("tion"))
