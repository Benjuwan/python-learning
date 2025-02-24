# チャプター 7

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


class Pass:
    pass


pass_class = Pass()


class Food:
    # __init__ は、コンストラクタ関数（インスタンスのプロパティ初期化処理）のようなもの
    def __init__(self, name, price):
        # self は this のようなもの
        self.name = name
        self.price = price
        print(name, price)


x = Food("milk", 150)
x.name = "egg"
print(x.name)
