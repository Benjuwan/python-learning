# チャプター 16（応用編：オブジェクトについてより深く知る）


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 特殊メソッド：前後に2個ずつ_（アンダースコア）が付いた特殊な名前を持つメソッド
    # クラスに特殊メソッドを定義すると、そのクラスのオブジェクトに対して色々な演算を実装できる
    # __str__：print関数でオブジェクトを出力できる特殊メソッド
    def __str__(self):
        return f"特殊メソッド ｜ x:{self.x} y:{self.y}"

    # インスタンスメソッドの定義
    def console_log(self, push_elm="."):
        print(f"x:{self.x} y:{self.y}{push_elm}")

    # 静的メソッド
    @staticmethod
    def sample_staticmethod(name="World"):
        return f"hello {name}!"

    # クラスメソッド
    # 第一引数 cls を使って、呼び出しに使われたクラスを受け取る（※ PEP8 では cls という引数名が推奨されている）
    @classmethod
    def sample_classmethod(cls, lang="Python"):
        return f"cls is {cls}.\n I'm learing {lang}."


print(Point(1, 2))  # 特殊メソッド __str__ のお陰で入力内容が出力される

Point(1, 2).console_log()  # これはインスタンスメソッド
Point(1, 2).console_log("!")  # これはインスタンスメソッド

print(Point.sample_staticmethod())  # これは静的メソッド
print(Point.sample_staticmethod("Alice"))  # これは静的メソッド

print(Point.sample_classmethod())  # これはクラスメソッド
print(Point.sample_classmethod("React"))  # これはクラスメソッド

"""
他にも[多くの特殊メソッド](https://docs.python.org/ja/3.13/reference/datamodel.html#special-method-names)が存在する
"""
