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


def f(arg1, arg2, arg3, arg4):
    print(f"Good {arg1}.")
    print(f"Good {arg2}.")
    print(f"Good {arg3}.")
    print(f"Good {arg4}.")


greeting = ["Morning", "Afternoon", "Evening", "Night"]
f(*greeting)

dessert = {"main": "puding", "side": "cookie", "drink": "tea"}
order_meals(**dessert)
print()

theDessert = [
    {"main": "puding", "side": "cookie", "drink": "tea"},
    {"main": "chocolate_cake", "side": "nuts", "drink": "cocoa"},
    {"main": "cheese_cake", "side": "mint", "drink": "coffee"},
]
for dessert in theDessert:
    print(dessert)
    order_meals(dessert["main"], dessert["side"], dessert["drink"])
    print()


def mutable_args_tuple_f(*args):
    for i, t in enumerate(args):
        print(f"{i + 1}番目のイテラブル要素「Good {t}」")
        if i == (len(args) - 1):
            print()


# タプル（形式）の位置引数として渡す
mutable_args_tuple_f("Morning", "Afternoon", "Evening", "Night")


def mutable_args_dict_f(**args):
    for k, v in args.items():
        print(f"{k}： Good {v}")


# キーワード引数として渡す
mutable_args_dict_f(Gozen="Morning", Gogo="Afternoon", Yugata="Evening", Yoru="Night")


def view_ordered_menus(*meal_tuple, **meal_dict):
    for i, elm in enumerate(meal_tuple):
        print(f"[ {i + 1} ] {elm}")
    for i, (k, v) in enumerate(meal_dict.items(), len(meal_tuple)):
        print(f"[ {i + 1} ] {k} : {v}")


view_ordered_menus("hotcake", "pizza", snack="parfait", dinner="steak")
