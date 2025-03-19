# チャプター 8

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


def payment_divisiton():
    try:
        price = int(input("価格："))
        if price <= 0:
            raise Exception("The price must be >= 0.")
        people = int(input("人数："))
        result = price // people
        print(f"result: {result}")

    # 大部分の例外の基底クラス{Exception}を指定して包括的に処理
    # except Exception:
    #     print("error.")

    # 複数の例外を指定
    # except (ValueError, ZeroDivisionError):
    #     print("error.")

    # 例外を単体指定
    except ValueError:
        print("ValueError： is not INT.")
    # 例外を単体指定（ZeroDivisionError：割る方が 0の場合に発生するエラー）
    except ZeroDivisionError:
        print("ZeroDivisionError： must be != 0.")

    except Exception as e:
        print(e)
    finally:
        print("-" * 25)


# payment_divisiton()


duplicate_counter += 1
duplicate_count(duplicate_counter)


# 以下の記述を
# numbers = []
# for i in range(10):
#     numbers.append(i**2)
# print(numbers) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 以下の記述に変更
numbers = [(i + 1) ** 2 for i in range(10)]
print(numbers)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 集合
the_set = set()
for i in range(10):
    the_set.add((i + 1) ** 2)
print(f"集合：{the_set}")

# 上記処理の内包表記ver
the_set_comprehension = {(i + 1) ** 2 for i in range(10)}
print(f"集合：{the_set_comprehension}")

# 辞書
the_dict = {}
for i in range(10):
    # dict[キー] = 値
    the_dict[f"No.{i + 1}"] = (i + 1) ** 2
print(f"辞書：{the_dict}")

# the_dict_comprehension = {(i + 1) ** 2: i for i in range(10)}
the_dict_comprehension = {f"No.{i + 1}": (i + 1) ** 2 for i in range(10)}
print(f"辞書：{the_dict_comprehension}")

# 多重ループ関連
# 九九（掛け算表）
for y in range(9):
    for x in range(9):
        # ()は必須
        column = (y + 1) * (x + 1)
        # x軸数値が9の倍数 （x軸の数値が9で割り切れる場合） の処理
        if (x + 1) % 9 == 0:
            print(f"{column:2d}")
        else:
            print(f"{column:2d}", end="|")

# 九九（掛け算表）配列形式
multiple_lists = []
for x in range(1, 10):
    for y in range(1, 10):
        multiple_lists.append(x * y)

# 多重ループの内包表記
# [式 for 変数A in イテラブルA for 変数B in イテラブルB]
# 左に書いたものは外側のループ、右に書いたものは内側のループとなり、更に右側に足していくとネストしたループ（三重、四重...）なども実現できる。集合や辞書でも（[]が異なるだけで）同じ記法
print([x * y for x in range(1, 10) for y in range(1, 10)])

# リスト内リストを生成：以下のように階層的なループ処理も簡潔に実現できる
print([[x * y for x in range(1, 10)] for y in range(1, 10)])

for i in range(9):
    print(multiple_lists[i::9])

# 内包表記と if文の組み合わせ
# [式A for 変数 in イテラブル if 式B]
# 式Bの値 が True の場合は式Aを評価した値をリストに追加し、式Bの値が False の場合は式Aを評価せず値をリストにも追加しない。集合や辞書でも（[]が異なるだけで）同じ記法
print([i for i in range(20) if i % 3 != 0 and i % 2 != 0])

# 上記「内包表記と if文の組み合わせ」を使用しないver
target_numbers = []
for i in range(20):
    if i % 3 != 0 and i % 2 != 0:
        # print(i, end=",")
        target_numbers.append(i)

print(target_numbers)


# FixxBuzz
def FizzBuzz():
    FizzBuzz_result = []
    for i in range(1, 16):
        if i % 5 == 0 and i % 3 == 0:
            # print("FizzBuzz")
            FizzBuzz_result.append("FizzBuzz")
        elif i % 5 == 0:
            # print("Buzz")
            FizzBuzz_result.append("Buzz")
        elif i % 3 == 0:
            # print("Fizz")
            FizzBuzz_result.append("Fizz")
        else:
            # print(i)
            FizzBuzz_result.append(i)

    print(FizzBuzz_result)


FizzBuzz()


def FizzBuzz_xai():
    FizzBuzz_result = [
        "FizzBuzz"
        if i % 5 == 0 and i % 3 == 0
        else "Buzz"
        if i % 5 == 0
        else "Fizz"
        if i % 3 == 0
        else i
        for i in range(1, 16)
    ]
    print(FizzBuzz_result)


FizzBuzz_xai()

# 単純なものなら [三項演算子 for 変数 in イテラブル] は開発効率が良いかも
fruits = ["banana", "apple", "melon", "water-melon"]
check_APPLE = [fruit.upper() if fruit == "apple" else "" for fruit in fruits]
print(check_APPLE)

duplicate_counter += 1
duplicate_count(duplicate_counter)

# genObj = (i * i for i in range(10))
# print(genObj)

# for g in genObj:
#     print(g, end=" ")


# def g():
#     for x in range(10):
#         yield x * x


# for y in g():
#     print(y, end=" ")


def my_range(start, finish):
    x = start
    while x < finish:
        yield x
        x += 1


def my_range2(start, finish, count):
    for _ in range(count):
        yield from my_range(start, finish)


g_list = []
for y in my_range2(1, 10, 3):
    print(y, end=" ")
    g_list.append(y)


print(f"\n {g_list}")
for _ in range(3):
    print(g_list[0:9])


duplicate_counter += 1
duplicate_count(duplicate_counter)


def loop(f):
    for i in range(10):
        print(f"{f(i)}...\n" if i == 9 else f(i), end=" ")


# def square(x):
#     return x * x


# loop(square)


# ラムダ式で上記を表現
# lambda 引数: 式
# loop(lambda x: x * x)
loop(lambda x: x**3)

duplicate_counter += 1
duplicate_count(duplicate_counter)

target_sort_tuple_list = [
    ("burger", 110, 234),
    ("potato", 150, 226),
    ("shake", 120, 218),
]
print(target_sort_tuple_list)
print(sorted(target_sort_tuple_list, reverse=True))


print(sorted(target_sort_tuple_list, key=lambda item: item[1]))


# 上記を関数定義で実行
def price_sort(item):
    return item[1]


print(sorted(target_sort_tuple_list, key=price_sort))


# 大きい順にソートさせるために reverse=True を指定
print(sorted(target_sort_tuple_list, reverse=True, key=lambda item: item[2]))


# 上記を関数定義で実行
def highcalory_sort(item):
    return item[2]


print(sorted(target_sort_tuple_list, reverse=True, key=highcalory_sort))


# 大きい順にソートさせるために reverse=True を指定
print(sorted(target_sort_tuple_list, reverse=True, key=lambda item: item[2] / item[1]))


# 上記を関数定義で実行
def highcalory_per_price_sort(item):
    return item[2] / item[1]


print(
    sorted(
        target_sort_tuple_list,
        reverse=True,
        key=highcalory_per_price_sort,
    )
)

duplicate_counter += 1
duplicate_count(duplicate_counter)

