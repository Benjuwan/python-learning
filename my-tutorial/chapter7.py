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


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show(self):
        print(f"{self.name}: {self.price}")


class Food(Item):
    # 基底クラスの __init__ 引数も指定する（今回は name, price）
    def __init__(self, name, price, used_limit):
        # JavaScript と同様に super() 関数で基底クラスの該当内容を継承（今回は コンストラクタ部分）
        super().__init__(name, price)
        self.used_limit = used_limit

    def show(self):
        # JavaScript と同様に super() 関数で基底クラスの該当内容を継承（showメソッド）
        super().show()
        print(f"{self.name}: {self.price}: {self.used_limit}")


class Toy(Item):
    def __init__(self, name, price, target_age):
        super().__init__(name, price)
        self.target_age = target_age

    def show(self):
        # super().show()
        print(f"{self.name}: {self.price}: {self.target_age}")


Food_instance = Food("chocolate", 100, 180)
Food_instance.show()
Toy_instance = Toy("figure", 350, 3)
Toy_instance.show()
