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

duplicateCounter += 1
duplicateCount(duplicateCounter)

concat_animals = animals + copied_animals
print(concat_animals)
# animals += copied_animals
# print(animals)

del concat_animals[1]  # cats
dogs = concat_animals.pop(0)
print(dogs)
eagles = concat_animals.pop(-2)
print(eagles)

concat_animals.remove("rions")

print(concat_animals)

filtered_animals = list(
    filter(lambda animal: animal != "zebras" and animal != "humans", concat_animals)
)
print(f"filtered_animals | {filtered_animals}")

humansUpperCase = list(
    map(
        lambda animal: f"theGreatest-{animal.upper()}"
        if animal == "humans"
        else animal,
        concat_animals,
    )
)
print(humansUpperCase)

print(animals)
for i, animal in enumerate(animals):
    if i == 0 or i == 2 or i == 6:
        print(animal)

duplicateCounter += 1
duplicateCount(duplicateCounter)

# const list1 = [1, 2, 3, 4, 5];
# list1.splice(1, 1, 100) // 2 を 100 に置換
# console.log(list1)
# list1.splice(3, 0, 400) // 4 のまえに 400 を追加
# console.log(list1)
# list1.splice(2, 1) // 3 を削除
# console.log(list1)

# Python で splice のようなことをするには
list1 = [1, 2, 3, 4, 5]

# より明確な書き方
list1[1] = 100  # 置換
print(list1)
list1.insert(3, 400)  # 挿入
print(list1)
del list1[2]  # 削除
print(list1)

# スライス記法を使った場合（一度に複数要素を追加したい場合に有用）
# list1[1:2] = [100]      # 置換
# list1[3:3] = [400]      # 挿入
# list1[2:3] = []         # 削除

list1 = []
# list1.clear()
print(list1)

duplicateCounter += 1
duplicateCount(duplicateCounter)

lorem_ipsum = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
lorem_ipsum_ary = lorem_ipsum.replace(",", "").split(" ")
print(lorem_ipsum_ary, f"{len(lorem_ipsum_ary)} words")

counter_ut = lorem_ipsum_ary.count("ut")
print(counter_ut)

lorem_ipsum_join = "_".join(lorem_ipsum_ary)
print(lorem_ipsum_join)

duplicateCounter += 1
duplicateCount(duplicateCounter)

menu = ["burger", "potato", "shake"]
menu += menu
print(menu)
# 対象文字が配列の何番目にあるかどうか
firstshake = menu.index("shake")
print(firstshake)
secondshake = menu.index("shake", firstshake + 1, len(menu))
print(secondshake)

copied_menu = menu.copy()
# 破壊的処理
copied_menu.sort()
copied_menu.reverse()
print(f"{menu}\n{copied_menu}")

# 非破壊的処理
sorted_menu = sorted(menu)
sorted_menu_True = sorted(menu, reverse=True)  # 逆順にソート
print(f"{sorted_menu}\n{sorted_menu_True}")

duplicateCounter += 1
duplicateCount(duplicateCounter)

int_lists: list[int] = [1, 100, 50, 30, 5, 8000]
min_int: int = min(int_lists)
max_int: int = max(int_lists)
print(min_int, max_int)

duplicateCounter += 1
duplicateCount(duplicateCounter)

theList: list[str | int | float] = ["Alice", 24, "tokyo", 23.5]
theTuple = ("Alice", 24, "tokyo", 23.5)
theSingleTuple = ("Alice",)  # タプルと認識してもらうには末尾に , が必要
print(theList[2], theTuple[2])
print(f"theTuple（{theTuple}）\n更新前 {id(theTuple)}")
theTuple = ("Alice", 32, "osaka", 24)
print(f"theTuple（{theTuple}）\n更新後 {id(theTuple)}")

duplicateCounter += 1
duplicateCount(duplicateCounter)

# alphabet = tuple("ABCDEFG")
alphabet = list("ABCDEFG")
# 分割代入（アンパッキング）
first, second, third, *rest, final = alphabet
print(first, second, third, final, rest)

duplicateCounter += 1
duplicateCount(duplicateCounter)

# --- TypeScript で以下のリスト・タプルを表現
# const restaurant_menu: (string | number)[][] = [["sushi", 780, 180.5], ["tempura", 640, 320.5]];

# type MenuItem = [string, number, number];
# const restaurant_menu: MenuItem[] = [["sushi", 780, 180.5], ["tempura", 640, 320.5]];
# --- TypeScript で以下のリスト・タプルを表現

# リスト
# restaurant_menu = [["sushi", 780, 180.5], ["templa", 640, 320.5]]
# restaurant_menu.append(["takoyaki", 120, 200.5])

# タプル
restaurant_menu = [("sushi", 780, 180.5), ("templa", 640, 320.0)]
restaurant_menu.append(("takoyaki", 120, 200.5))

templa_tuple = restaurant_menu[1]
print(templa_tuple)
cousine, price, calories = templa_tuple
print(cousine, price, calories)

duplicateCounter += 1
duplicateCount(duplicateCounter)

numbers_set: set[int] = set([1, 2, 2, 3, 3, 4])
numbers: set[int] = {1, 2, 2}
number = {1}
print(numbers_set, numbers, number)

trafic_signal: set[str] = {"green", "red", "blue"}
print(trafic_signal)

str_set_lower = set("abcdefg")
str_set_upper = set(list("ABCDEFG"))
print(str_set_upper, sorted(str_set_upper), type(str_set_upper))
print(str_set_lower, sorted(str_set_lower), type(str_set_lower))

str_set_anaconda = set("str_set_anaconda")
print(str_set_anaconda)

duplicateCounter += 1
duplicateCount(duplicateCounter)

print(f"{'green' in trafic_signal} # True")
print(f"{'pink' in trafic_signal} # False")
print(f"{'purple' not in trafic_signal} # True")
print(f"{'red' not in trafic_signal} # False")

duplicateCounter += 1
duplicateCount(duplicateCounter)


def isExist_targetUserInfo(
    targetUserTuple: tuple[str, str], targetUserGroup: set[tuple[str, str]]
):
    # 検索対象（要素・文字）は完全一致の記述でないと正しく機能しない
    # 今回の場合だと tuple[str, str] という型（形）
    return targetUserTuple in targetUserGroup


def isNotExist_targetUserInfo(
    targetUserTuple: tuple[str, str], targetUserGroup: set[tuple[str, str]]
):
    return targetUserTuple not in targetUserGroup


users_info: set[tuple[str, str]] = {("admin", "abc123"), ("guest", "def567")}
isExist_admin = isExist_targetUserInfo(("admin", "abc123"), users_info)  # True
isExist_master = isExist_targetUserInfo(("guest", "abc123"), users_info)  # False
print(isExist_admin, isExist_master)

isNotExist_admin = isNotExist_targetUserInfo(("guest", "abc123"), users_info)  # True
isNotExist_master = isNotExist_targetUserInfo(("admin", "abc123"), users_info)  # False
print(isNotExist_admin, isNotExist_master)

duplicateCounter += 1
duplicateCount(duplicateCounter)
