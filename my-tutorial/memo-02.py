# チャプター 4～xx 章まで

# 区切り（兼改行）用の文字列
duplicateCounter: int = 0
duplicateStr: str = "-+-"


# 区切り（兼改行）用の文字列を表示する関数
def duplicateCount(duplicateCounter: int):
    if duplicateCounter == 1:
        print(f"\n{str(duplicateCounter)} {duplicateStr * 20} \n")
    else:
        print(f"{str(duplicateCounter)} {duplicateStr * 20} \n")


duplicateCounter += 1
duplicateCount(duplicateCounter)

# 配列操作

theAry: list[str] = []
theAry = ["hoge", "foo", "bar"]
print(theAry)

theAry_StrOrInt: list[str | int] = []
theAry_StrOrInt = [10, "hoge", 100, "foo"]
print(theAry_StrOrInt)

duplicateCounter += 1
duplicateCount(duplicateCounter)


flavor: list[str] = ["vanilla", "chocolate", "strawberry"]
print(flavor)

someTypeAry: list[int | float | str] = ["one", 2, 3.0]

from0to10: list[int] = list(range(10))
print(from0to10)

add_from0to10 = list(map(lambda n: n + 1, from0to10))
print(add_from0to10)

maped_from0to10: list[str | int] = list(
    map(lambda n: f"No.{n + 1 if type(n) is int else n}", from0to10)
)
print(maped_from0to10)

duplicateCounter += 1
duplicateCount(duplicateCounter)

# const Python = 'Python'
# console.log(Python.toLowerCase().split(''));
strAry_python = list("Python".lower())
print(strAry_python)

drinks = ["coffee", "tea", "milk", "water"]
print(drinks)
print(drinks[2])

drinks[3] = "cola"

duplicateCounter += 1
duplicateCount(duplicateCounter)

for i, drink in enumerate(drinks):
    if drink == "tea" or drink == "cola":
        targetIndex = i
        print(f"{drink.upper()}, {drinks[targetIndex].upper()}, {targetIndex}")

print(drinks)

duplicateCounter += 1
duplicateCount(duplicateCounter)

# const drinks = ["coffee", "tea", "milk", "water"]
# drinks.slice(1,3)
print(f"slice | {drinks[1:3]}")

newDrinks: list[str] = list(
    filter(lambda drink: drink == "tea" or drink == "milk", drinks)
)
print(f"filter | {newDrinks}")

copied_newDrinks: list[str] = newDrinks.copy()
print(f"copy | {copied_newDrinks}")

copied_newDrinks = list(map(lambda drink: f"healthy-{drink}", copied_newDrinks))
print(newDrinks, copied_newDrinks)

duplicateCounter += 1
duplicateCount(duplicateCounter)

animals = list("dogs-cats-birds-rabits-wolfs".split("-"))
print(f"origin | {animals}")

copied_animals = animals.copy()
copied_animals.append("zebras")  # 破壊的メソッド
copied_animals += ["rions"]  # イテラブルとして代入するので[]が必須
copied_animals.extend(
    ["eagles"]
)  # 破壊的メソッド、イテラブルとして代入するので[]が必須
copied_animals[len(copied_animals) :] = [
    "humans"
]  # イテラブルとして代入するので[]が必須
print(f"origin | {animals}\ncopied | {copied_animals}")

concat_animals = animals + copied_animals
print(concat_animals)

duplicateCounter += 1
duplicateCount(duplicateCounter)
