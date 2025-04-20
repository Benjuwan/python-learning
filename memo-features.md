## `pass`文
処理をパスする（何もしない）ための構文。
```py
for i in range(10000):
  # 構文ルール上、ここに何らかの処理を記述しなければならない
  # しかし特に記述することが無いような場合に pass 文を使う
  pass
```
関数やクラス作成時に「何もしない処理や挙動が発生」したものの、構文ルール的に何かしらを記述しなければならない場合に`pass`文を使用する。<br>または、後で処理を書くことを意図して、とりあえず`pass`を置いておくようなプレースホルダー的な使い方もあるそう。

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

## ビルトイン関数（組み込み関数）
### type
`JavaScript`でいう[`typeof`](https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Operators/typeof)にあたる。引数に指定したオブジェクトの型を表示する。
```py
type(オブジェクト)
```

#### `isinstance`
`JavaScript`でいう[`instanceof`](https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Operators/instanceof)（左辺が右辺`クラス`のインスタンスであるかどうか）にあたる。<br>引数に指定したオブジェクトが**特定のクラスかどうかをチェック**する。
```py
# isinstance(オブジェクト, クラス)
print(isinstance(123, int))     # True
print(isinstance("123", int))   # False
print(isinstance("123", str))   # True
print(isinstance(3.14, float))  # True
```

> [!NOTE]
> - あるクラスの派生クラス（サブクラス）かどうかをチェックする`issubclass`関数というのもある
> ```py
> issubclass(クラスA, クラスB)
> # クラスA が クラスB のサブクラスであるかどうかをチェックし、
> # True の場合は True、False の場合は False となる。
> ```

### 文字列をPython式に評価する`eval`（イーヴァル）関数
`JavaScript`の[`eval`](https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Global_Objects/eval)と同じ。<br>指定された文字列をPython式として評価し、その式の値を返す。<br>例えば、ユーザーが入力したPython式を評価して結果の値を求める、などできる。
```py
# eval(文字列)
while True:
    result = eval(input("=")) # list('python') と入力すると...
    if result == "q":
        break
    print(result)
```

### プログラムを実行する`exec`（エグゼック）関数
指定された文字列をPythonプログラムとして実行する。戻り値はなし（`None`）。
```py
exec(文字列)
```

`compile`関数を使って**Pythonプログラムをコンパイルして生成される「コードオブジェクト」**も扱える。
```py
exec(コードオブジェクト)
```

#### プログラムをコンパイルする`compile`関数
指定された文字列やファイルの内容をPythonプログラムとしてコンパイルしてコードオブジェクトを返す。返ってきたコードオブジェクトは`exec`関数で実行できる。
```py
compile(文字列, '<string>', 'exec')
```

### `assert`文
...であることを断言（assert）する、という文脈で使用される。<br>
主に、デバッグやテストに用いる`Python`処理系のビルトイン機能で、例えば「この式の値は`True`である」と断言する、といった使い方になる。<br>
一度に複数の式を指定することも可能。<br>
式の値が`True`の場合は何もないが、`False`の場合は`AssertionError`という例外が発生する。つまり、**例外が発生しなかった場合に自分の想定が正しかった（意図通りの挙動）ということを確認**できる。

```py
# である ことを断定
assert 式

# ではない ことを断定
assert not 式
```

- 実装例
```py
# 年が400で割り切れる場合は「うるう年」
# 年が100で割り切れず、4で割り切れる場合も「うるう年」
def leap_year(year: int):
    return year % 400 == 0 or year % 100 > 0 and year % 4 == 0

# 処理実行して何も表示されなければok
assert not leap_year(1900)
assert leap_year(2000)
assert not leap_year(2019)
assert leap_year(2020)
assert not leap_year(2024) # AssertionError 発生 
```

> [!NOTE]
> - `Python`でのテスト
> プログラムのテストを実施するには（例：`pytest`のような）本格的なテストツールやテストフレームワークを使う必要があるものの、シンプルな実装内容の場合は`assert`文で済むことも多い。

### `format`関数
指定された書式指定に従って値を整形し、結果の文字列を返す関数。

- 詳細：[書式指定ミニ言語仕様](https://docs.python.org/ja/3.13/library/string.html#formatspec)

- 具体例
```py
float_elm = 1 / 3
print(format(float_elm))
# 0.3333333333333333

# .小数点以下桁数f
print(format(float_elm, ".2f"))  # 小数点以下2桁を表示
# 0.33

# {式:書式指定}
print(f"{1 / 3:.2f}")
# 0.33

# 千の位ごとに ,を挿入
print(format(100000000000000000, ","))
# 100,000,000,000,000,000

# 千の位ごとに _を挿入
print(format(100000000000000000, "_"))
# 100_000_000_000_000_000
```

---
### `round`関数
数値の小数部分を指定した桁数に丸めて返す。（第二引数の）桁数を省略した場合は数値に最も近い整数を返す。引数には整数と浮動小数点を指定できる。
```py
print(round(1 / 3))     # 0（※数値に最も近い整数）
print(round(1 / 3, 2))  # 0.33（※少数部を2桁に丸めている）
```

数値に最も近い整数が奇数と偶数の2種類発生した場合は**偶数が優先**される。
```py
print(round(3 / 2))     # 2
print(round(3 / 2, 2))  # 1.5
```

第二引数に**負の値**を指定した場合は、**その桁数に準じて整数を丸める**ことができる
```py
print(round(123, -1))  # 120 （下1桁を丸める）
print(round(123, -2))  # 100 （下2桁を丸める）
print(round(123, -3))  # 0   （下3桁を丸める）
```

---

> [!NOTE]
> - `.小数点以下桁数f`の記法は`JavaScript`で言えば[`toFixed()`メソッド](https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Global_Objects/Number/toFixed)にあたる
> ```js
> function financial(x) {
>  return Number.parseFloat(x).toFixed(2);
> }
>
> console.log(financial(123.456)); // "123.46"
> ```

### `f`文字列
`JavaScript`でいうテンプレートリテラル（バックティック）の記法と似ていて、`{}`の中に変数や式、処理をそのまま記述して（その結果を反映した）文字列を表現できる。

- 桁数の調整
```py
# 基本的な使い方
number = 5
print(f"{number:2d}")  # " 5" （幅2文字で右寄せ）
# x * y - フォーマットする値
# : - フォーマット指定の開始
# 2 - 表示する幅（文字数）
# d - 整数（decimal）として表示

# 実際の動作を確認
numbers = [1, 5, 10, 42]
for n in numbers:
    print(f"{n:2d}")  # それぞれの数字が2文字分の幅で右寄せされる

# その他
# 左寄せ（<）
print(f"{5:<2d}")  # "5 "

# 中央寄せ（^）
print(f"{5:^2d}")  # "5 "

# ゼロ埋め
print(f"{5:02d}")  # "05"

# より大きな幅を指定
print(f"{5:4d}")   # "   5"

# {式:書式指定} という記述も可能
print(f"{1 / 3:.2f}") # 0.33
```

### バイナリデータ（テキストではないデータ）の取り扱い
- `bytes`関数<br>イミュータブルなバイト列を返す
```py
bytes(文字列, encoding=文字エンコーディング)
bytes(整数)         # 整数が示すバイト数のバイト列やバイト配列を生成する
bytes(イテラブル)   # イテラブルの要素（※0以上255未満の整数である必要がある）を格納したバイト列やバイト配列を生成する

# 具体例
bytes('python', encoding='utf-8')
```

- `bytearray`関数<br>ミュータブルなバイト配列を返す
```py
bytearray(文字列, encoding=文字エンコーディング)
bytearray(整数)         # 整数が示すバイト数のバイト列やバイト配列を生成する
bytearray(イテラブル)   # イテラブルの要素（※0以上255未満の整数である必要がある）を格納したバイト列やバイト配列を生成する

# 具体例
bytearray('python', encoding='utf-8')
```

バイト列またはバイト配列はどちらも 0以上255未満の整数（1バイト：8ビットの符号なし整数を並べたもの）

- `memoryview(オブジェクト)`<br>指定したオブジェクト内部にあるメモリを操作するための関数。コピーは作らず、元メモリを操作する。

#### `bin`
整数を2進数の文字列に変換する。<br>`binary（バイナリ、2進数）`
```py
print(bin(123))     # 0b1111011
print(f"{123:b}")   # 1111011
print(f"{123:#b}")  # 0b1111011 ← 0b が付く
```

#### `oct`
整数を8進数の文字列に変換する。<br>`octal（オクタル、8進数）`
```py
print(oct(123))     # 0o173
print(f"{123:o}")   # 173
print(f"{123:#o}")  # 0o173 ← 0o が付く
```

#### `hex`
整数を16進数の文字列に変換する。<br>`hexadecimal（ヘクサデシマル、16進数）`
```py
print(hex(123))     # 0x7b
print(f"{123:x}")   # 7b
print(f"{123:#x}")  # 0x7b ← 0x が付く
```

### 計算式について
`Python`の計算式は、原則「左結合（左側にある式を優先的に計算）」するが`**`（べき乗）のみ「右結合」で処理（計算）される。明示的に`()`を使って計算式を書くのが無難。

#### 除算（割り算）について
`/`を用いて除算（割り算）を行うと浮動小数点（型）として、`//`を用いて除算を行うと整数（型）として扱われる。
```py
print(4 / 2)  # 2.0
print(4 // 2) # 2
```

##### `divmod()`
除算（割り算）の商と剰余（余り）を求め、タプルにまとめて返す関数。引数の数値には整数と浮動小数点が指定できる。
```py
divmod(数値A, 数値B) # 数値Aを数値Bで除算した時の「商と剰余のタプル」を返す

# 具体例
print(divmod(30, 5)) # (6, 0)
print(divmod(53, 3)) # (17, 2)
```

### `abs`（エービーエス）
数値の絶対数を返す関数（`abs`は`absolute number`の略称）
```py
abs(数値) # 引数の数値には「整数、浮動小数点、複素数」が指定できる

# 具体例
print((123))        # 123
print((-456))       # 456
print((12.3))       # 12.3
print(abs(-12.3))   # 12.3
```

### `pow`（パウ）
べき乗計算（`**`）を行う関数。引数の数値には「整数、浮動小数点、複素数」が指定できる。
```py
pow(数値A, 数値B)           # 数値Aを数値B乗した数
pow(数値A, 数値B, 数値C)    # 数値Aを数値B乗した数を数値Cで割った余り

# 具体例
print(pow(2, 3))  # 2の3乗 -> 8
print(pow(2, 3, 5))  # 2の3乗を5で割った余り -> 3
```

### `min`, `max`
複数の引数（文字列型含む）またはイテラブルから最小（`min`）、最大（`max`）の要素・値を取得する。

- 複数の引数
```py
# 文字列型の場合は文字コード順
print(min("blue", "red", "green"))  # blue
print(max("blue", "red", "green"))  # red
```

- イテラブル
```py
some_numbers = [100, 10, 25, 8, 64]
print(min(some_numbers))  # 8
print(max(some_numbers))  # 100
```

### `sum`
イテラブルに含まれる数値の合計値を算出する。
```py
want_sum_numbers = [90, 75, 80, 100, 85]
print(sum(want_sum_numbers))       # 430
print(sum(want_sum_numbers) / 5)   # 平均値：86.0
print(sum(want_sum_numbers) // 5)  # 平均値：86（//を使うことで整数として表現）
```

> [!NOTE]
> - `sum`は、`JavaScript`でいう`reduce`関数
> ```js
> const want_sum_numbers = [90, 75, 80, 100, 85];
> const sum_result = want_sum_numbers.reduce((accu, curr) => accu + curr, 0);
> console.log(sum_result); // 430
> ```

### `repr`（レプル）
オブジェクトの内容を表す文字列を返す関数。`repr`関数の結果に[`eval`関数](#文字列をpython式に評価するevalイーヴァル関数)を適用すると`Python`のプログラムとして実行できるようになる。
```py
representation = repr("Python") # 'Python'
print(representation)
representation = repr("パイソン") # 'パイソン'
print(representation)
```

### `ascii`
`repr`同様、オブジェクトの内容を表す文字列を返す関数だが、**ASCII文字（アスキー文字）以外をエスケープ処理**する。
```py
ascii_no_esc = ascii("Python") # 'Python'
print(ascii_no_esc)
ascii_esc = ascii("パイソン")   # '\u30d1\u30a4\u30bd\u30f3'
print(ascii_esc)
```