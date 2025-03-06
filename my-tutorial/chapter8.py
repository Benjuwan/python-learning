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
print({(i + 1) ** 2 for i in range(10)})

# 辞書
print({(i + 1) ** 2: i for i in range(10)})

numbers_dict = {}
for i in range(10):
    # dict[キー] = 値
    numbers_dict[f"No.{i + 1}"] = i**2
print(numbers_dict)
