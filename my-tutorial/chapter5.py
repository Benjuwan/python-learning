# チャプター 5

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


def input_test_check_count_len():
    entries_1 = input("入力欄1:")  # internationalization

    # AND演算子（左辺が True の場合に右辺を返す： False の場合は False を返す）
    result_entries_1 = (
        entries_1.count("tion") > 0 and f"entries_1: {entries_1.count('tion')}"
    )

    # OR演算子（左辺が False の場合に右辺を返す： True の場合は True を返す）
    # result_entries_1 = len(entries_1) <= 0 or f"entries_1: {len(entries_1)}"
    print(entries_1, result_entries_1)

    entries_2 = input("入力欄2:")
    print(entries_2)


# input_test_check_count_len()

duplicateCounter += 1
duplicateCount(duplicateCounter)


def check_lot_numbers(entried: None | str | int | float = None) -> None:
    # 数値型かどうかを判定して変換する関数
    def convert_to_number(entryNumber: str | int | float) -> int | float | None:
        try:
            # 整数変換に試みる
            return int(entryNumber)
        except ValueError:
            try:
                # 整数変換に失敗した場合は浮動小数点への変換を試みる
                return float(entryNumber)
            except ValueError:
                # ここまで全て失敗した場合は None を返す
                return None

    # 宝くじの当選チェックを行う関数
    def is_check_get_prize(entryNumber: int | float):
        if entryNumber == 123456:
            print(f"{entryNumber} is a Special Prize!\nWow!")
            print("congratulations")
        elif str(entryNumber)[-4:] == "7890":
            # 下4桁に一致 （str(entryNumber)[len(str(entryNumber)) - 4 :]）
            # console.log(entryNumber.slice(entryNumber.length -4, entryNumber.length)); // '123456': 2文字目から6文字目まで
            print(f"{entryNumber} is a 2nd Prize!\nGift Box")
        elif str(entryNumber)[len(str(entryNumber)) - 2 :] == "05":
            # 下2桁に一致 （str(entryNumber)[len(str(entryNumber)) - 2 :]）
            # console.log(entryNumber.slice(entryNumber.length -2, entryNumber.length)); // '123456': 4文字目から6文字目まで
            print(f"{entryNumber} is a 3rd Prize!\nStamp Sheet")
            print("game set.")
        else:
            print(f"{entryNumber} is no Prize.")

    # 初期入力が None の場合
    if entried is None:
        entryNumber: str = input("入力欄：")

        # 前者： 6文字未満または15文字以上は処理不能（無効判定処理）
        # 後者： 6文字以上かつ15文字未満の場合（※有効判定処理を if not で false 判定を対象にしている = 前者の条件と同じ）
        # if len(entryNumber) < 6 or len(entryNumber) > 15:
        if not (6 <= len(entryNumber) <= 15):
            print("need min 6 characters, max 15 characters.")
            return

        convert_number = convert_to_number(entryNumber)
        if convert_number is None:
            print("we accept only numbers.")
            return

        is_check_get_prize(convert_number)

    # 初期入力が与えられた場合
    else:
        convert_number = convert_to_number(entried)
        if convert_number is None:
            print("we accept only numbers.")
            return

        is_check_get_prize(convert_number)


# check_lot_numbers(123456)
# check_lot_numbers(159753)
# check_lot_numbers("159753")
# check_lot_numbers(3.14)
# check_lot_numbers()

duplicateCounter += 1
duplicateCount(duplicateCounter)

greeting = ["Morning", "Afternoon", "Evening", "Night"]
for greet in greeting:
    print(f"Goog {greet}.")

for c in "PYTHON\n".lower():
    print(c, end="")

meals = ["beaf", "pork", "chicken"]
# 対象配列（イテラブル）をコピーしないとイテラブルとインデックスに齟齬が生じて意図した繰り返し処理がなされない
for meal in meals.copy():
    if meal == "pork":
        meals.remove(meal)
    else:
        print(f"list | {meal}")

# タプルはイミュータブル
meals_tuple = ("beaf", "pork", "chicken")
for meal in meals_tuple:
    print(f"tuple | {meal}")

# 集合は順不同
meals_set = {"beaf", "pork", "chicken"}
for meal in meals_set:
    print(f"set | {meal}")

# 辞書
meals_dict = {"beaf": 199, "pork": 99, "chicken": 49}
# type aryType = {
#   beaf: number;
#   pork: number;
#   chicken: number;
# };
# const theAry: aryType = { beaf: 199, pork: 99, chicken: 49 };

for meal in meals_dict:
    print(
        f"dict では key が出力される | {meal} → ブラケット記法で値を出力：{meals_dict[meal]}"
    )

# ブラケット記法以外で value を取得する方法
# dict.items() で key と value を分割代入
for key, value in meals_dict.items():
    print(f"{key} is {value} yen.")

# 複数のタプルを分割代入
practice = [("beaf", 199), ("pork", 99), ("chicken", 49)]
# practice = (("beaf", 199), ("pork", 99), ("chicken", 49))
# practice = {("beaf", 199), ("pork", 99), ("chicken", 49)}
for key, value in practice:
    print(f"{key}: {value}")

duplicateCounter += 1
duplicateCount(duplicateCounter)

print(list(range(10)))
print(list(range(20, 31)))
print(f"{list(range(20, 31, 2))}\n\n")

# 九九の表
for x in range(1, 10):
    for y in range(1, 10):
        # 2桁（decimal）で統一
        print(f"{x * y:2d}", end="")
        # （縦軸の）最後の数字（9）以外は区切り文字を入れる
        if y != 9:
            print(" |", end="")
    # 各行の最後（xの繰り返し処理の最後）で改行
    print()

duplicateCounter += 1
duplicateCount(duplicateCounter)

order_drink_list = ["beer", "wine", "whisky", "water", "soda"]
for i, drink in enumerate(order_drink_list, 1):
    print(f"DrinkOrder-No.{i:03d}: {drink}")
    # print(i)

# for i in range(len(order_drink_list)):
#     print(f"DrinkOrder-No.{i + 1:03d}: {order_drink_list[i]}")

order_drink_set = {"beer", "wine", "whisky", "water", "soda"}
order_drink_set_copied = order_drink_set.copy()
for i in range(len(order_drink_set_copied)):
    print(f"DrinkOrder-No.{i + 1:02d}: {order_drink_set_copied.pop()}")
print(order_drink_set, order_drink_set_copied)

# reversed を用いたカウントダウン
for i in reversed(range(11)):
    print(i, end=" ")
print()  # 処理後に改行

# reversed の引数に直接 enumerate は指定できない
# ※ シーケンス（インデックスで要素の位置を指定できるオブジェクト）でなかったり、処理に必要なメソッド（__reversed__()）などを持っていなかったりするため
order_drink_list_copied = order_drink_list.copy()
# for i, drink in reversed(enumerate(order_drink_list_copied)):
for i, drink in reversed(list(enumerate(order_drink_list_copied))):
    print(f"DrinkOrder-No.{i + 1:03d}: {order_drink_list_copied[i]}")

duplicateCounter += 1
duplicateCount(duplicateCounter)

index_key_while = 0
while index_key_while < 10:
    index_key_while += 1
    print(index_key_while)
print(f"index_key_while：{index_key_while}")


def create_catalogs():
    catalogs = []
    while len(catalogs) < 5:
        item = input(
            f"{f'現在の{catalogs}の中身：' if len(catalogs) > 0 else 'catalogs'}に追加する商品名："
        )
        if item in catalogs:
            print(f"{item}は既に catalogs：{catalogs}に登録されています")
            continue
        elif item == "its over":
            break
        catalogs.append(item)
    print(catalogs)


# create_catalogs()

duplicateCounter += 1
duplicateCount(duplicateCounter)

exam_score: list[int] = [32, 78, 64, 84, 71, 45, 56, 99]
for score in exam_score:
    if score < 70:
        continue
    else:
        print(f"{score}.your passed.")

duplicateCounter += 1
duplicateCount(duplicateCounter)

duplicate_lists: list[str] = [
    "beer",
    "www",
    "apple",
    "banana",
    "soda",
    "benjuwan jijao",
]


def check_duplicate_words_and_count(
    target_duplicate_lists: list[str], optional_arg=None
):
    results: set = set()
    for chars in target_duplicate_lists:
        for c in chars:
            count = chars.count(c)
            if count >= 2:
                # set（集合）にはイミュータブルしか格納できない
                results.add((chars, c, count))
            else:
                continue

    results_list: list = sorted(results)
    print(
        f"{len(results_list)}\n {results_list} {f'\n{optional_arg}' if optional_arg is not None and optional_arg else ''}"
    )


check_duplicate_words_and_count(duplicate_lists)

duplicateCounter += 1
duplicateCount(duplicateCounter)


def check_entry_wordstype():
    entry_word = input("文字入力：")
    if len(entry_word) == 0:
        return
    print(
        f"入力文字{entry_word}は「{set(entry_word)}」から成る「{len(set(entry_word))}文字」で形成されています"
    )


check_entry_wordstype()

duplicateCounter += 1
duplicateCount(duplicateCounter)
