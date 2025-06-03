## 関数・メソッド（クラス）

- ヘルパー関数<br>
特定の処理をより簡単に行うために、既存の関数をラップしたり、機能を拡張したり**既存処理を部分改良**するための関数

### `split()`
戻り値は常にリスト型
```py
text = "apple banana cherry"
words = text.split()
print(words)  # ["apple", "banana", "cherry"]

url = "sports/football/fw"
# 指定したデリミタ（区切り文字）で分割も可能
url_paths = url.split('/')
print(url_paths)  # ["sports", "football", "fw"]
```

### `join(イテラブル)`
指定したデリミタ（区切り文字）で配列を結合する
```py
url_paths = ["sports", "football", "fw"]

# デリミタ.join(イテラブル)
url = "/".join(url_paths)
print(url)
```

### `replace()`
文字列内の特定の部分（文字列）を指定した別の文字列で置換
```py
# 第一引数には置換対象の文字列（target）を、
# 第二引数には変更文字列（src）を、
# 第三引数には置換個数の上限（count）を、
# それぞれダブルクォーテーションで囲って指定
str.replace(target, src, count)

# 具体例
anaconda = "anaconda"
# すべて置換
print(anaconda.replace("a", "A"))
# AnAcondA

# 初めの一つだけ置換
print(anaconda.replace("a", "A", 1))
# Anaconda

# 2つ目まで置換
print(anaconda.replace("a", "A", 2))
# AnAconda
```

### `startswith`, `endswith`
```py
# 先頭が指定した接頭辞から始まる場合は True を返す
文字列.startswith(接頭辞の文字列)

# 末尾が指定した接尾辞で終わる場合は True を返す
文字列.endswith(接尾辞の文字列)
```

`startswith`, `endswith`ともに引数には**タプル形式で複数値を指定できる**
```py
url = "https://example.co.jp"
if url.startswith(("https://", "http://", "/")):
    # True の場合の処理
```

### `isnumeric()`
文字列が数字だけで構成されているかどうかを調べる（返り値：Boolean）
```py
文字列.isnumeric()
```

### `range()`
引数に指定した数と内容（範囲）で処理内容が変わってくる
  - `range(終了値)`
  ```py
  # 0〜9まで格納された list生成
  print(list(range(10)))
  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  ```

  - `range(開始値, 終了値)`
  ```py
  # 20〜30まで格納された list生成
  print(list(range(20, 31)))
  # [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
  ```

  - `range(開始値, 終了値, オフセット)`<br>
  第三引数の`オフセット`には負の整数も指定可能
  ```py
  # 20〜30までの5の倍数（5刻み）のものが格納された list生成
  print(list(range(20, 31, 5)))
  # [20, 25, 30]
  ```

### `enumerate`<br>
イニュームレイト：列挙型（`enum`）のことで、イテラブルから要素を取り出す時に何番目に取り出した要素なのかを把握できる。戻り値は **`カウント`と`要素の値`のタプル`tuple()`** となる。
```py
for i, elm in enumerate('イテラブル', '開始値'):
  # 処理
```
第二引数の`開始値`はカウントの開始値を指す。

### `count`
対象文字列内における検索文字列の出現回数を取得する
```py
search_str: str = '検索文字列'
target_str_ary.count(search_str)
```

### `index`
指定した値に一致する要素のうち最も先頭に近い要素のインデックスが取得できる<br>`JavaScript`でいう`indexOf`メソッドに近い。
```py
target_lists = ['hoge', 'foo', 'bar', 'piyo']
target_lists.index('bar') # 2

# index(値, 開始インデックス, 終了インデックス)
```

- `JavaScript`における`index`と近しい挙動のメソッド
  - `indexOf`メソッド
  ```js
  const lists = ['hoge', 'foo', 'bar', 'piyo'];
  lists.indexOf('bar'); // 2
  ```
  - `findIndex`メソッド<br>
  配列内の指定された条件（テスト関数`hasTargetStr`）に合格する **最初の要素のインデックス** を返す。（テスト関数`hasTargetStr`に）合格する要素がなかった場合は`-1`を返す。
  ```js
  const lists = ['hoge', 'foo', 'bar', 'piyo'];
  const hasTargetStr = (word) => word === 'bar';
  console.log(lists.findIndex(hasTargetStr)); // 2
  ```

### `sorted(イテラブル)`
ソート機能
- 引数
  - `reverse`：<br>`True`にすることで反転
  - `key`：<br> **ソート基準（値）** となる`関数`を指定できる。`Python`は（シーケンスの）各要素に対して指定された関数を適用し、その結果をソートの基準として使用する。デフォルトのソートは「シーケンス間で対応する要素同士を前から順次比較（小さい方を前に）する」という方法。
    - シーケンス：<br>文字列やリストなどインデックスで要素の位置を指定（＝指定したインデックスで要素を取得）できるオブジェクトのこと

> [!NOTE]
> - `key`引数について<br>
> `key`引数に渡す関数は**引数を明示的に指定する必要がない**。<br>
> 注意事項として**常に一つの要素だけを関数に渡すので直接的に複数引数を持つ関数は使えない**。<br>
> 複数の引数を持つ関数を使用したい場合には、クロージャを使った関数定義にするなど工夫が必要となる。

```py
some_numbers = [100, 10, 25, 8, 64]

# [8, 10, 25, 64, 100]
print(sorted(some_numbers))

# [100, 64, 25, 10, 8]
print(sorted(some_numbers, reverse=True))

# ----- key 引数を使った具体例
target_sort_tuple_list = [("burger", 110, 234), ("potato", 150, 226), ("shake", 120, 218)]

# price でソート
print(sorted(target_sort_tuple_list, key=lambda item: item[1]))

# 上記 lambda式 を関数定義で実行
def price_sort(item):
    return item[1]

# key の関数には引数を明示的に指定しない
print(sorted(target_sort_tuple_list, key=price_sort))
```

---

> [!NOTE]
> - `.sort()`<br>
> `リスト.sort()`も機能としては`sorted(イテラブル)`と全く同じで、<br>
> 取れる引数である`reverse`と`key`も同じ働きをする。<br>
> 違いとしては`リスト.sort()`の場合は**リスト専用**であり、**元リストを並び替える破壊的処理**である点。

## 関数定義
他の言語同様`関数名(引数, ...)`という形で記述していくし、関数の呼び出し方も同じだが、`def`という宣言子を前置したり、`関数名(引数, ...):`パラメータ後に`:`を置いたり`Python`独自の記法もある。<br>
**関数の命名規則もまた変数同様に区切り部分はアンダースコア`_`で繋いでいく**のが一般的。<br>
使用頻度の低い引数にはデフォルト値を設けて省略することもできる。<br><br>

> [!NOTE]
> - 引数のデフォルト値について<br>
> 引数にデフォルト値を設定する場合`args=default_value`という形、つまり**キーワード引数**のような形式になる。<br>
> しかしデフォルト値を指定した引数はキーワード引数として扱われるわけではなく、あくまで**実際の使用時に指定する引数の在り方**でキーワード引数を判定している。
> ```py
> def f(start: int | None = None, ...):
>  
> f(100, ...)
> # 100 を設定値に指定 = start 引数はデフォルト値を持った引数として扱われる
> 
> f(start=100, other_keyword='', ...)
> # 100 を設定値に指定 = start 引数はキーワード引数として扱われる
> ```

- 渡された引数`arg`が数値型に変換可能かをチェックする関数<br>
```py
def convert_to_number(arg: str | int | float) -> int | float | None:
    """
    JSDoc のような関数へのコメントや説明の記述箇所及び記法（三重クオートで囲う）
    関数宣言（名）の直後に記述する
    ---
    渡された引数`arg`が数値型に変換可能かをチェックする関数
    [convert_to_number 関数の概要]
    Args:
        arg: str | int | float  # 文字列 | 整数 | 浮動小数点数 を引数として受け取る

    Returns:
        int | float | None      # 整数 | 浮動小数点数 | 何もなし を返す
    """
    try:
        # 整数（型）変換に試みる
        return int(arg)
    except ValueError:
        try:
            # 整数変換に失敗した場合は浮動小数点（型）への変換を試みる
            return float(arg)
        except ValueError:
            # ここまで全て失敗した場合は None を返す
            return None
```

- `check_duplicate_words_and_count`関数<br>
対象文字列配列内`list[str]`の各文字列内にある重複文字と重複回数をチェックする関数
```py
duplicate_lists: list[str] = [
    "beer",
    "www",
    "apple",
    "banana",
    "soda",
    "benjuwan jijao",
]


def check_duplicate_words_and_count(
    target_duplicate_lists: list[str], optional_arg=None
):
    results: set = set()
    for chars in target_duplicate_lists:
        for c in chars:
            count = chars.count(c)
            if count >= 2:
                # set（集合）にはイミュータブルしか格納できない
                results.add((chars, c, count))
            else:
                continue

    results_list: list = sorted(results)
    print(
        f"{len(results_list)}\n {results_list} {f'\n{optional_arg}' if optional_arg is not None and optional_arg else ''}"
    )


check_duplicate_words_and_count(duplicate_lists)
```

### 引数の指定
#### イテラブルアンパッキング（`*イテラブル`）
引数に指定したイテラブルを展開して関数の引数に渡すことができる位置引数で、`JavaScript`でいうスプレッド演算子（配列中身の展開）に近いような働きをする。
```py
def f(arg1, arg2, arg3, arg4):
    print(f"Good {arg1}.")
    print(f"Good {arg2}.")
    print(f"Good {arg3}.")
    print(f"Good {arg4}.")


greeting = ["Morning", "Afternoon", "Evening", "Night"]
f(*greeting)
```

#### 辞書アンパッキング（`**dict`）
 `dict`から`key`と`value`を取り出し**「`key`=`"value"`」というキーワード引数**として関数に渡すことができる。
```py
dessert = {"main": "puding", "side": "cookie", "drink": "tea"}
# 各キーワード引数： main="puding", side="cookie", drink="tea"
order_meals(**dessert)
```

> [!NOTE] 
> 構文エラー回避のためにも「位置引数またはイテラブルアンパッキングは左側に、キーワード引数または辞書アンパッキングは右側に配置」と覚えておく

#### コマンドライン引数
コマンドプロンプトやターミナルでコマンド入力する際に**コマンドに対して与える引数**のこと。<br>
これにより、**コマンドラインから特定処理の実行（計算やファイル編集、操作など）が可能**となる。

```bash
コマンド 引数
```

##### `Python`ファイルに対するコマンドライン引数の実行
```bash
python hoge.py 引数
```

コマンドライン引数を受け取るには、標準ライブラリ`sys`（シス）モジュールを使用する。`sys`モジュールの`argv`（アーグブイ）属性がプログラム名とコマンドライン引数のリストとなる。
```py
import sys

# プログラム名と引数のリストを取得
# 取得したリスト[0]にはプログラム名が入り、以降のインデックスには引数が続く
sys.argv # 属性なので()は無し

# 指定した位置（インデックス）の値を取得
sys.argv[0] # プログラム名
sys.argv[1] # 第一引数
sys.argv[2] # 第二引数

# プログラム名と引数の個数を取得
len(sys.argv)
```

##### コマンドライン引数の具体例
```py
# python chapter11.py 1 2 3
print(sys.argv)
# 結果：['chapter11.py', '1', '2', '3']

print(len(sys.argv))    # 4
print(sys.argv[0])      # chapter11.py
print(sys.argv[-1])     # 3
```

### その他 / 具体例
#### 可変長引数（`print`関数のように任意個の引数を受け取る関数）
関数定義の際、パラメータに`(*引数)`または`(**引数)`と記述する。
  - `(*引数)`と記述（位置引数として振る舞う）<br>
  任意個の**位置引数をタプル**として受け取る
  ```py
  def mutable_args_tuple_f(*args):
      for i, t in enumerate(args):
          print(f"{i + 1}番目のイテラブル要素「Good {t}」")
          if i == (len(args) - 1):
              print()


  # タプル（形式）の位置引数として渡す
  mutable_args_tuple_f("Morning", "Afternoon", "Evening", "Night")
  ```

  - `(**引数)`と記述（キーワード引数として振る舞う）<br>
  任意個の**キーワード引数を辞書**として受け取る
  ```py
  def mutable_args_dict_f(**args):
      for k, v in args.items():
          print(f"{k}： Good {v}")


  # キーワード引数として渡す
  mutable_args_dict_f(Gozen="Morning", Gogo="Afternoon", Yugata="Evening", Yoru="Night")
  ```
  
  - `(*引数)`と`(**引数)`の組み合わせ
  ```py
  def view_ordered_menus(*meal_tuple, **meal_dict):
      for i, elm in enumerate(meal_tuple):
          print(f"[ {i + 1} ] {elm}")
      # enumerate の第二引数に開始値（今回は meal_tuple の配列数）を指定
      # for 文の変数について、対象辞書の key と value をグループにしないとランタイムエラー（ValueError: not enough values to unpack）が発生する
      for i, (k, v) in enumerate(meal_dict.items(), len(meal_tuple)):
          print(f"[ {i + 1} ] {k} : {v}")


  view_ordered_menus("hotcake", "pizza", snack="parfait", dinner="steak")
  ```

  - `(*引数)`と`デフォルト値を持ったキーワード引数`、`(**引数)`の組み合わせ<br>
  ```py
  # **引数（辞書アンパッキング）のあとにはいかなる引数も指定できないので、デフォルト値を持ったキーワード引数（optional_start）は、*引数（位置引数）と**引数（キーワード引数）の間に指定
  def view_ordered_menus_xai(*meal_tuple, optional_start: int | None = None, **meal_dict):
      start = optional_start - 1 if type(optional_start) is int else 0
      for i, elm in enumerate(meal_tuple, start):
          print(f"[ {i + 1} ] {elm}")
      for i, (k, v) in enumerate(meal_dict.items(), (len(meal_tuple) + start)):
          print(f"[ {i + 1} ] {k} : {v}")


  # オプショナルな引数を指定
  view_ordered_menus_xai(
      "hotcake",
      "pizza",
      optional_start=55,
      snack="parfait",
      lunch="curry",
      dinner="steak",
  )
  print()

  # オプショナルな引数を省略（指定せず）
  view_ordered_menus_xai(
      "hotcake", "pizza", snack="parfait", lunch="curry", dinner="steak"
  )
  ```
  コード内のコメント通り、`**引数`（辞書アンパッキング）のあとにはいかなる引数も指定できないので、`デフォルト値を持ったキーワード引数`（`optional_start`）は、`*引数`（位置引数）と`**引数`（キーワード引数）の間に指定している。

## ビルトイン関数（組み込み関数）
### `pass`文
処理をパスする（何もしない）ための構文。
- 構文ルール上、何らかの処理を記述しなければならないが、特に記述することが無いような場合に`pass`文を使う
```py
for i in range(10000):
  # ここに何らかを記述しなければならないが、特に記述することが無い場合は pass を用いる
  pass
```
関数やクラス作成時に「何もしない処理や挙動が発生」したものの、構文ルール的に何かしらを記述しなければならない場合に`pass`文を使用する。<br>または、後で処理を書くことを意図して、とりあえず`pass`を置いておくようなプレースホルダー的な使い方もあるそう。

### type
`JavaScript`でいう[`typeof`](https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Operators/typeof)にあたる。引数に指定したオブジェクトの型を表示する。
```py
type(オブジェクト)
```

### `isinstance`
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

### `breakpoint`関数
デバッグのために意図的にプログラムを一時停止させる`breakpoint`を設ける関数。実行すると当該箇所（行）で[`pdb`（Pythonデバッガ）](https://docs.python.org/ja/3.13/library/pdb.html)に制御が移行する。

- `l（エル）+ enter` でプログラム表示（※ブレークポイントの位置確認）
- `p 変数（式）+ enter` で式を表示
- `n + enter` で一行進む
- `c + enter` で次のブレークポイントまで移動
- `s + enter` で対象関数の中に入る
- `r + enter` で対象関数を`return`まで実行

```py
first = 123
breakpoint() # ブレークポイント設置
second = 456
duplicate_count(duplicate_counter)
third = 789
breakpoint() # ブレークポイント設置
print(first, second, third)
```

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

## 計算式について
`Python`の計算式は、原則「左結合（左側にある式を優先的に計算）」するが`**`（べき乗）のみ「右結合」で処理（計算）される。明示的に`()`を使って計算式を書くのが無難。

### 除算（割り算）について
`/`を用いて除算（割り算）を行うと浮動小数点（型）として、`//`を用いて除算を行うと整数（型）として扱われる。
```py
print(4 / 2)  # 2.0
print(4 // 2) # 2
```

#### `divmod()`
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

## 例外処理（`try - except`）
`JavaScript`では`try - catch`だが、`Python`では`try - except`と記述する
```py
def payment_divisiton():
    try:
        price = int(input("価格："))
        people = int(input("人数："))
        result = price // people
        print(f"result: {result}")

    # 大部分の例外の基底クラス（Exception）を指定して包括的に処理
    # except Exception:
    #     print("error.")

    # 複数の例外を指定
    # except (ValueError, ZeroDivisionError):
    #     print("error.")

    # 例外を単体指定
    except ValueError:
        print("ValueError： is not INT.")
    # 例外を単体指定（ZeroDivisionError：割る方（今回の場合は people ）が 0の場合に発生するエラー）
    except ZeroDivisionError:
        print("ZeroDivisionError： must be != 0.")

    # 共通終了処理
    finally:
        print("-" * 25)


payment_divisiton()
```

- エラーや例外を意図的に無視（**※良くない実装なので注意**）<br>
`JavaScript`には無いが、以下のように記述すると`Python`ではエラーや例外を黙認できる
```py
except 例外:
  pass
```

- `Python`では、例外操作においても`else`文が使用できる
  - ※`else`は、**`except`より後かつ`finally`より前に書く**こと
```py
try: 
  # 成功処理（検証対象処理）
except 例外A:
  # 例外A
except 例外B:
  # 例外B
else:
  # 例外が発生しなかった場合のみ実行される処理
  # ※ try の内側に記述しても良いが else を使うことで明示的な記述となる
finally:
  # 共通終了処理
```

> [!NOTE]
> `Python`も、`JavaScript`同様「例外を投げて（※`JavaScript`でいう`throw new Error()`して）キャッチされなければ領域脱出する」仕様になっている

- ※`except`（例外設定処理）は**上から順に処理（先述優先）していく**ので注意<br>
一般的に、`except`節を記述するときは派生クラス（例：`ValueError`, `ZeroDivisionError`）を上に、基底クラス（例：`Exception`）を下に書く。

- 例外発生時は、その例外を処理する`except`節に出会うまで`finally`節以外の実行（処理）は全て省かれる。

### `raise`（レイズ）
`JavaScript`でいう`throw new Error()`
```py
raise 例外

# 例外の内容を表すオブジェクトを格納したうえで Exception を発生させる
raise Exception(オブジェクト)
```
- 具体例
```py
def payment_divisiton():
    try:
        price = int(input("価格："))
        if price <= 0:
            # 例外を投げる
            raise Exception("The price must be >= 0.")
            
        people = int(input("人数："))

    # 中略...

    # 例外オブジェクトの取得（例外 as 変数）
    except Exception as e:
        print(e)

    finally:
        print("-" * 25)


payment_divisiton()
```
