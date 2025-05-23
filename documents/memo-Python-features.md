## 内包表記（`comprehension`）について
データ構造（リストなどのイテラブル）を作成するときに役立つ構文で、簡潔な記述（プログラム）でリスト（`list`）や集合（`set`）、辞書（`dict`）に**格納する値を生成**できる。

### リストの内包表記
以下のような要領で他のデータ構造（集合や辞書）の内包表記も実現できる
```py
[式 for 変数 in イテラブル]

# 内包表記におけるアンパッキング（スプレッド演算子）
[式 for 変数, ... in イテラブル]
```

- 具体例
```py
# 以下の記述（0〜9までの2乗）を
numbers = []
for i in range(10):
    numbers.append(i**2)
print(numbers) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 以下の記述（1〜10までの2乗）に変更
numbers = [(i + 1) ** 2 for i in range(10)]
print(numbers)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

### 集合の内包表記
※集合の性質を当然持っているので、取り出し順は保証されず、重複した値は排除される。
```py
{式 for 変数 in イテラブル}

# 内包表記におけるアンパッキング（スプレッド演算子）
{式 for 変数, ... in イテラブル}
```

- 具体例
```py
# 集合
the_set = set()
for i in range(10):
    the_set.add((i + 1) ** 2)
print(f"集合：{the_set}")

# 上記処理の内包表記ver
the_set_comprehension = {(i + 1) ** 2 for i in range(10)}
print(f"集合：{the_set_comprehension}")
```

### 辞書の内包表記
```py
{keyの式: valueの式 for 変数 in イテラブル}

# 内包表記におけるアンパッキング（スプレッド演算子）
{keyの式: valueの式 for 変数, ... in イテラブル}
```

- 具体例
```py
# 辞書
the_dict = {}
for i in range(10):
    # `dict[キー] = 値` で辞書に要素を追加
    # 指定したキーが当該辞書に含まれていない場合は「キーと値の組を新たに追加」
    # 含まれている場合は「そのキーに対応する値を書き換える」
    the_dict[f"No.{i + 1}"] = (i + 1) ** 2
print(f"辞書：{the_dict}")

# the_dict_comprehension = {(i + 1) ** 2: i for i in range(10)}
the_dict_comprehension = {f"No.{i + 1}": (i + 1) ** 2 for i in range(10)}
print(f"辞書：{the_dict_comprehension}")
```

> [!NOTE]
> - タプルの内包表記はない<br>
> タプルチックな書き方をしたものは全く別物の「[ジェネレーター式](#ジェネレーター式--ジェネレーター関数)」として扱われる

### 多重ループの内包表記
以下の多重ループ（で実装された「九九（掛け算表）」）をベースに進める。
```py
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
for i in range(9):
    print(multiple_lists[i::9])
```

多重ループの内包表記では、**左に書いたものは外側のループ、右に書いたものは内側のループ**となる。<br>
更に右側に足していくとネストしたループ（三重ループ、四重ループ...）を実現できる。<br>
集合や辞書でも（[]が異なるだけで）以下と同じ記法。
```py
[式 for 変数A in イテラブルA for 変数B in イテラブルB]
```

- 具体例（多重ループの内包表記）
```py
print([x * y for x in range(1, 10) for y in range(1, 10)])

# リスト内リストを生成
# 以下のように階層的なループ処理も簡潔に実現できる
print([[x * y for x in range(1, 10)] for y in range(1, 10)])
```

### 内包表記と if文の組み合わせ
`式B`の値 が`True`の場合は`式A`を評価した値をリストに追加し、`式B`の値が`False`の場合は`式A`を評価せず値をリストにも追加しない。<br>
集合や辞書でも（[]が異なるだけで）以下と同じ記法。
```py
[式A for 変数 in イテラブル if 式B]
```
- 具体例（内包表記と if文の組み合わせ）
```py
# 0～19までの数値で、2でも、3でも割り切れない数値を出力
print([i for i in range(20) if i % 3 != 0 and i % 2 != 0])
# [1, 5, 7, 11, 13, 17, 19]

# 上記「内包表記と if文の組み合わせ」を使用しないver
target_numbers = []
for i in range(20):
    if i % 3 != 0 and i % 2 != 0:
        # print(i, end=",")
        target_numbers.append(i)

print(target_numbers)
```

#### 内包表記と三項演算子の組み合わせ
```py
[三項演算子 for 変数 in イテラブル]

# 三項演算子
# <trueの値> if <条件> else <falseの値>
```

- 具体例（内包表記と三項演算子の組み合わせ）<br>
※`FizzBuzz`に関する処理について、簡潔ではあるものの非常に可読性が悪いので使い方に注意。
```py
def FizzBuzz():
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


FizzBuzz()
```

以下の`check_APPLE`みたいな単純なものだと開発効率が良いかも。
```py
# 単純なものなら [三項演算子 for 変数 in イテラブル] は開発効率が良いかも
fruits = ["banana", "apple", "melon", "water-melon"]
check_APPLE = [fruit.upper() if fruit == "apple" else "" for fruit in fruits]
print(check_APPLE)
# ['', 'APPLE', '', '']
```

## ジェネレーター式 / ジェネレーター関数
ジェネレーターはリスト同様にイテラブルなオブジェクト（`generator object`）だが、リストのように既存要素を格納しているのではなく、**処理要求される度に一つずつ生成**する特徴を持つ。<br>
処理要求される度に一つずつ生成するため、メモリの消費を抑えたり、無制限の値を生成できたりする利点がある。<br>
`React`でいう`React Server Component`のようにサーバー側で処理を実行し、クライアント側の（レンダリングなど処理）負担を軽減する仕組みに少し似ている。

### ジェネレーター式

```py
(式 for 変数 in イテラブル)

# 変数が複数ある場合
(式 for 変数, ... in イテラブル)
```

- 具体例
```py
# (式 for 変数 in イテラブル)
genObj = (i * i for i in range(10))
print(genObj)
# 0 1 4 9 16 25 36 49 64 81 
```

[内包表記](#内包表記comprehensionについて)と同じく、多重ループや条件分岐の実装も可能。

### ジェネレーター関数
ジェネレーター式で表現するには複雑なものを扱う際に使用する。通常の関数定義に似た記法だが、`return`の代わりに`yield`を用いるのが特徴。<br>
※`yield`は`return`と違って即座に処理終了しない特徴的な性質を持つ。

```py
def g():
    for x in range(10):
        yield x * x


for y in g():
    print(y, end=" ")
# 0 1 4 9 16 25 36 49 64 81
```

- `yield from`<br>
既存のジェネレーター（ジェネレーター関数やジェネレーター式）を利用して別のジェネレーター（ジェネレーター関数）を定義する
```py
def my_range(start, finish):
    x = start
    while x < finish:
        yield x # `return`と違って即座に処理終了しない
        x += 1


def my_range2(start, finish, count):
    for _ in range(count):
        yield from my_range(start, finish)


for y in my_range2(1, 10, 3):
    print(y, end=" ")
# 1〜10までの数値ジェネレーター（my_range）が 3回出力される（my_range2）
# 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 
```

## ラムダ（lambda）式（※Pythonにおいては**端的な関数定義**を実現）
関数型言語の機能の一つがラムダ式。関数型言語の基盤となっているラムダ計算という理論に由来している。<br>`
Python`においてはラムダ式を用いることで、簡単な関数定義において通常の関数定義よりも短く記述できるようになる。

```py
lambda 引数: 式

# 上記（ラムダ式）は以下の関数定義と同義
def 関数名(引数):
  return 式

---

# 引数が複数ある場合
lambda 引数, ...: 式
```

当該関数を、コールバック関数（別の関数の引数として渡される関数）として利用する場合、通常の関数定義よりもプログラムが簡潔になる場合がある。

- 具体例
```py
# 通常の関数定義
def loop(f):
    for i in range(10):
        print(f(i), end=" ")


def square(x):
    return x * x


loop(square)

---

def loop(f):
    for i in range(10):
        print(f(i), end=" ")


# ラムダ式で上記を表現
# lambda 引数: 式
loop(lambda x: x * x)
```

### `sort()`関数を用いた具体例
```py
# 食べ物, 値段, カロリー
target_sort_tuple_list = [("burger", 110, 234), ("potato", 150, 226), ("shake", 120, 218)]

# カロリーでソート
# 大きい順にソートさせるために reverse=True を指定
print(sorted(target_sort_tuple_list, reverse=True, key=lambda item: item[2]))


# 上記を関数定義で実行
def highcalory_sort(item):
    return item[2]


# sort() の key の関数には引数を明示的に指定しないので注意
print(sorted(target_sort_tuple_list, reverse=True, key=highcalory_sort))
```

## セイウチ演算子（代入式）
式を評価した値を変数に代入するとともに、その値を代入式の結果として返す。
```py
変数 := 式
```

代入式は端的にプログラミングできる（コードが短く簡潔になる）一方、可読性が低下するリスクもあるのでケースバイケースで使用するのが一般的。

- 具体例
```py
def walrus_example():
    # 入力内容が q でない間は入力内容を出力し続ける
    while x := input() != "q":
        print(x)


walrus_example()
```

## ダックタイピング
「オブジェクトがどのような型に属するかではなく、**どのようなメソッドや属性を持っているかで判断**する」という考え方。「アヒルのように歩き、アヒルのように鳴くなら、それはアヒルだ」という哲学から名付けられている。<br>
例えば、`TypeScript`でいう「期待するプロパティを持っていれば、他のプロパティを持っていても（指定した）型とみなされる**構造的部分型**」に近い考え。<br>
ただし「**コンパイル時**にダックタイピングの安全性をチェック」する`TypeScript`に対して、`Python`は**動的型付け言語**なので「**実行（ランタイム）時**にダックタイピングを行う」という違いがある。

## デコレーター（`@...`）
デコレーターは関数やクラスに特別な機能を付加する。

```py
# Bottle というPythonフレームワークを使ったデコレーターの利用例
@bottle.route('/bye')

def bye():
    return html.format('Bye!')
```

上記デコレーターには「Webブラウザが特定のURLにアクセスしたときに結果を返す関数を指定する働き」がある。
