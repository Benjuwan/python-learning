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


# 基底クラス
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show(self):
        print(f"{self.name}: {self.price}")


# 派生クラス（単一継承）
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

    def eat(self):
        print(f"--- eating {self.name}.")


# 派生クラス（単一継承）
class Toy(Item):
    def __init__(self, name, price, target_age):
        super().__init__(name, price)
        self.target_age = target_age

    def show(self):
        # super().show()
        print(f"{self.name}: {self.price}: {self.target_age}")

    def play(self):
        print(f"--- playing with {self.name}.")


Food_instance = Food("chocolate", 100, 180)
Food_instance.show()
Food_instance.eat()
Toy_instance = Toy("figure", 350, 3)
Toy_instance.show()
Toy_instance.play()


# 派生クラス（多重継承） ちなみに、Food, Toy の記述順を逆にすると？
class Syokugan(Food, Toy):
    def __init__(self, name, price, used_limit, target_age):
        # 以下の方法（super）だと{ Food.__init__() takes 4 positional arguments but 5 were given }というエラーが発生する
        # super().__init__(name, price, used_limit, target_age)
        self.name = name
        self.price = price
        self.used_limit = used_limit
        self.target_age = target_age

    def eat(self):
        print(f"--- eating {self.name.split('_')[0]}.")

    def play(self):
        print(f"--- playing with {self.name.split('_')[1]}.")

    def show(self):
        super().show()


Syokugan_instance = Syokugan("Choco_Doll", 450, 180, 3)
Syokugan_instance.show()
Syokugan_instance.eat()
Syokugan_instance.play()
