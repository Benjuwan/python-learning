# チャプター 6

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


def order_meals(main: str, side: str, drink: str):
    print(f"main  : {main}\nside  : {side}\ndrink : {drink}")


order_meals("steak", "salad", "coffee")

duplicate_counter += 1
duplicate_count(duplicate_counter)


def convert_to_number(arg: str | int | float) -> int | float | None:
    try:
        return int(arg)
    except ValueError:
        try:
            return float(arg)
        except ValueError:
            return None


def odd_even():
    entry_int = input("数値入力：")
    check_isInt = convert_to_number(entry_int)
    # check_isInt が None または float型の場合は処理終了
    if check_isInt is None or type(check_isInt) is float:
        print("only int.")
        return
    else:
        if int(entry_int) % 2 == 0:
            return "even"
        else:
            return "odd"


# print(odd_even())

duplicate_counter += 1
duplicate_count(duplicate_counter)

# dessert = {"main": "puding", "side": "cookie", "drink": "tea"}
# **dict（辞書アンパッキング）： dict の 各 key が引数名と一致する場合、その値を引数として渡せる
# order_meals(**dessert)

theDessert = [
    {"main": "puding", "side": "cookie", "drink": "tea"},
    {"main": "chocolate_cake", "side": "nuts", "drink": "cocoa"},
    {"main": "cheese_cake", "side": "mint", "drink": "coffee"},
]
for dessert in theDessert:
    order_meals(dessert["main"], dessert["side"], dessert["drink"])
    print()
