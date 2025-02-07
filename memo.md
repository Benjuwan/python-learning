## 備忘録・メモ
- オフサイドルール<br>
`Python`では、インデントやスペースがコード整形ではなく**コードの意図や構造を表現する**オフサイドルールが適用されている。

- 処理（`Pythonインタプリンタ`）の終了方法
バックエンド言語なのでターミナル・コマンドプロンプトでの処理実行が多い。もし処理を終了したい場合は以下の操作を行う。
  - Windows<br>
  `ctrl + z`+`enter`キー押下
  - Mac/Linux<br>
  `com/ctrl + d`
  - Windows/Mac/Linux 共通<br>
  `quit()`または`com/ctrl + c`（`KeyboardInterrupt`：キーボードによる中断）

- 変数について<br>
`Python`では、`JavaScript`でいう変数宣言（`let`や`const`）を用いずに変数を作成するため`var`のように再宣言も再代入もお構いなく可能な仕様になっている。<br>例えば、定数を作成する方法は無く普通の変数を使用するため、変更（再代入）仕様と思えばできてしまう。
  - 定数について<br>
  慣習的に**定数には大文字を用いてプログラマーに明示的に定数である意図表示**を行う（結局、仕様としては書き換え可能ではあるが）。<br>また、**単語の区切りは基本的にスネークケース**で行う。<br><br>
`Python`では、変数は明示的に管理・把握しやすくするためにあるもので、実際は**値ごとに付与される参照値（メモリアドレス）に紐づく**形で管理される言語仕様になっている。参照値（メモリアドレス ／ オブジェクトID）の確認は`id(変数)`で行える。

- 厳密等価演算子<br>
`Python`には、厳密等価演算子（`===`,`!==`）がないが、数値を`==`（または`is`）や`!=`（または`is not`）で比較する際に`Python`処理系が自動的に両者の型を合わせて（暗黙的型変換）から値を比較してくれる。<br>より厳密に判定したい場合は`type(変数-a) == type(変数-b)`, `type(変数-a) != type(変数-b)`のように記述する。
```py
# example-1
print(1 == 1.0)  # True: int と float でも値が等しいため
print(1 is 1.0)  # False: 'is' はオブジェクトの同一性を比較するため

# example-2
a = 100         # int
b = 100.0       # float
if type(a) == type(b) and a == b:
    print("型も値も一致しています")
else:
    print("型または値が一致しません")
```

- 計算式について<br>
`Python`の計算式は、原則「左結合（左側にある式を優先的に計算）」するが`**`（べき乗）のみ「右結合」で処理（計算）される。明示的に`()`を使って計算式を書くのが無難。

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
```

- `pass`文
処理をパスする（何もしない）ための構文。
```py
for i in range(10000):
  # 構文ルール上、ここに何らかの処理を記述しなければならない
  # しかし特に記述することが無いような場合に pass 文を使う
  pass
```
関数やクラス作成時に「何もしない処理や挙動が発生」したものの、構文ルール的に何かしらを記述しなければならない場合に`pass`文を使用する。<br>または、後で処理を書くことを意図して、とりあえず`pass`を置いておくようなプレースホルダー的な使い方もあるそう。

## 関数・メソッド（クラス）
- `range()`<br>
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

- `enumerate`<br>
イニュームレイト：列挙型（`enum`）のことで、イテラブルから要素を取り出す時に何番目に取り出した要素なのかを把握できる。戻り値は **`カウント`と`要素の値`のタプル`tuple()`** となる。
```py
for i, elm in enumerate(イテラブル, 開始値):
  # 処理
```
第二引数の`開始値`はカウントの開始値を指す。

### 関数定義
他の言語同様`関数名(引数, ...)`という形で記述していくし、関数の呼び出し方も同じだが、`def`という宣言子を前置したり、`関数名(引数, ...):`パラメータ後に`:`を置いたり`Python`独自の記法もある。関数名もまた変数同様に区切り部分はアンダースコア`_`で繋いでいくのが一般的。<br>使用頻度の低い引数にはデフォルト値を設けて省略することもできる。<br><br>

- 渡された引数`arg`が数値型に変換可能かをチェックする関数<br>
```py
def convert_to_number(arg: str | int | float) -> int | float | None:
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

#### 引数の指定
- イテラブルアンパッキング（`*イテラブル`）<br>
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

- 辞書アンパッキング（`**dict`）<br>
 `dict`から`key`と`value`を取り出し**「`key`=`"value"`」というキーワード引数**として関数に渡すことができる。
```py
dessert = {"main": "puding", "side": "cookie", "drink": "tea"}
# 各キーワード引数： main="puding", side="cookie", drink="tea"
order_meals(**dessert)
```

> [!NOTE] 
> 構文エラー回避のためにも「位置引数またはイテラブルアンパッキングは左側に、キーワード引数または辞書アンパッキングは右側に配置」と覚えておく

- 可変長引数（`print`関数のように任意個の引数を受け取る関数）<br>
関数定義の際、パラメータに`(*引数)`または`(**引数)`と記述する。
  - `(*引数)`と記述<br>
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
  - `(**引数)`と記述<br>
  任意個の**キーワード引数を辞書**として受け取る
  ```py
  def mutable_args_dict_f(**args):
      for k, v in args.items():
          print(f"{k}： Good {v}")


  # キーワード引数として渡す
  mutable_args_dict_f(Gozen="Morning", Gogo="Afternoon", Yugata="Evening", Yoru="Night")
  ```


## 繰り返し処理
```py
# リストの要素を直接繰り返し
for element in array:
    print(element)

# 数値範囲での繰り返し
for i in range(len(array)):
    print(array[i])
```

- インデックスと要素の両方を使う場合<br>
```py
# enumerate：イテラブル（反復可能なオブジェクト・繰り返し可能要素）に対して各要素とそのインデックスをペアとして返す
for i, element in enumerate(array):
    print(f"{i}: {element}")
```

### `while`
他の言語と同様の（繰り返し処理）機能。指定した条件を達するまで繰り返し処理を行う。
```py
index_key_while = 0
# index_key_while が 10になるまで 1ずつインクリメント
while index_key_while < 10:
    index_key_while += 1
    print(index_key_while)
```

### `continue`と`break`
- `continue`<br>
他の言語と同様、`for`や`while`の繰り返し処理におけるスキップ機能。ループ内部に残っている処理を実行せずに次の処理に移行する。

- `break`<br>
他の言語と同様、`for`や`while`の繰り返し処理における強制終了機能。ループ内部に残っている処理を実行せずに当該繰り返し処理を終了する。

## `Python`での配列操作について（シャローコピーの必要性有無）
`Python`では破壊的メソッド（`append`, `extend`, `sort`など）と非破壊的メソッド（`sorted`など）が明確に区別されているそうで、一般的にリストのコピーを作成してから操作を行うという習慣はない。
```py
# 破壊的メソッドの例
numbers = [3, 1, 2]
# resultはNone（破壊的メソッドは基本的にNoneを返す）
result = numbers.sort()
print(numbers)  # [1, 2, 3]

# 非破壊的メソッドの例
numbers = [3, 1, 2]
sorted_numbers = sorted(numbers)  # 新しいリストを返す
print(numbers)  # [3, 1, 2]
print(sorted_numbers)  # [1, 2, 3]

# 破壊的メソッドと非破壊的メソッドの組み合わせ例
numbers = [1, 2, 3]
numbers.append(4)  # 破壊的操作・メソッドだと明確に分かる
sorted_numbers = sorted(numbers)  # 非破壊的「関数」だと明確に分かる
numbers.sort()  # 破壊的メソッドだと明確に分かる
```

  - `Python`でのシャローコピー作成方法
  ```py
  numbers = [1, 2, 3]

  # シャローコピーを作成する方法
  numbers_copy = numbers.copy()
  # または numbers_copy = numbers[:] （先頭から末尾までスライスでリスト要素を抽出）
  # または numbers_copy = list(numbers) （listクラスを使用して listオブジェクトを生成）

  # ディープコピーを作成する方法
  from copy import deepcopy
  numbers_deep_copy = deepcopy(numbers)
  ```

  - `JavaScript`でいう `shift`, `unshift` や `pop`, `push` のような配列操作について
  ```py
  my_list = [1, 2, 3]

  # JavaScript の pop() と同じ - 末尾から要素を削除して返す
  last_element = my_list.pop()  # 3を返し、リストは[1, 2]になる

  # JavaScript の push() と同じ - 末尾に要素を追加
  my_list.append(4)  # [1, 2, 4]になる

  # JavaScript の shift() と同じ - 先頭から要素を削除して返す
  first_element = my_list.pop(0)  # 1を返し、リストは[2, 4]になる

  # JavaScript の unshift() と同じ - 先頭に要素を追加
  my_list.insert(0, 5)  # [5, 2, 4]になる
  ```
  これらはすべて**破壊的メソッド**であることに注意

## 型定義について
```py
# TypeScript `const theStr: string`
theStr: str = 'hoge'

# TypeScript `const theNum: number`
theNum: int = 0

# TypeScript `const theStrOrNum: string | number`
# `Union[str | int]`は ver.3.10 以降の記述なので`Union[str, int]`の方が互換性が高い記述方法 
theStrOrNum: str | int = 100

# TypeScript `const theBool: boolean`
theBool: bool = True

# TypeScript `const theAry_str: string[]`
theAry_str: list[str] = ['hoge', 'foo', 'bar']

# TypeScript `const theAry_int: number[]`
theAry_int: list[int] = [10, 100]

# TypeScript `const theAry_StrOrInt: (string | number)[]`
theAry_StrOrInt: list[str | int] = [10, "hoge", 100, "foo", True] # True は 1 として扱われる（bool は int としても扱えるため）が、明示的に 1 に置き換えた方がわかりやすい
```

## リスト（配列 / イテラブル（反復可能なオブジェクト・繰り返し可能要素））について
目的に応じた適切なデータ構造を用いるのが大切
  - **リスト**（`list(range(10)) # 9までの list[int] を生成`）： 最もベーシックで無難なミュータブルなデータ構造
    - `list()`関数に`辞書{dict}`を渡すと、デフォルトで`辞書`の`key`のイテレータを返す
    ```py
    lang_dict = {"ja": "japanese", "en": "English", "fr": "french"}
    print(list(lang_dict))
    # ['ja', 'en', 'fr']
    ```
  - **タプル**（`tuple(range(10)) # 9までの tuple[int, ...] を生成`）： イミュータブル（不変）にした場合
    - リスト（配列）とは違って **「配列数が固定で、中身・要素（の型）は自由」** というイミュータブルなデータ構造（＝インデックスやスライスなどで要素を変更できない）。
    ```py
    # () で要素を囲う 
    theTuple = ("Alice", 24, "tokyo", 23.5)
    theSingleTuple = ("Alice",)  # 要素が秘湯の場合、タプルと認識してもらうには末尾に , が必要
    ```
> [!NOTE]  
> - リストとタプルそれぞれにそれぞれを格納
> ```
> # タプル内にリストを格納
> list_in_tuple: tuple[list[str | int | float] | str, ...] = tuple(
>     ["hoge", "foo", ["hoge", 100, 1.23]]
> )
> # リスト内にタプルを格納
> tuple_in_list: list[tuple[str, int] | tuple[str, float, str]] = list(
>     [("hoge", 100), ("hoge", 1.23, "bar")]
> )
> print(f"list_in_tuple | {list_in_tuple}\ntuple_in_list | {tuple_in_list}")
> ```
  - **集合**（`set(range(10)) # 9までの set[int] を生成`）
    - 数学の集合論をベースにした、重複のない要素のコレクション
    ```py
    # {} で要素を囲う 
    # リストから集合を作成（重複は自動的に削除）
    numbers_set = set([1, 2, 2, 3, 3, 4])
    numbers = {1, 2, 2}
    number = {1}
    print(numbers_set, numbers, number)
    ```
      - 特徴
        - 同じ値を重複して保存（格納）できない
        - **値を取り出すときの順序が保証されない**（例：出力するたびに並び順が変わる）
        - 指定した値が含まれているか瞬時に判定できる
        ```py
        trafic_signal = {"green", "red", "blue"}
        print(trafic_signal) # {'green', 'blue', 'red'}
        ```
        - **イミュータブルな値のみ格納可能**
> [!NOTE]  
> - `list`はミュータブルなので{集合}には格納不可能
> ```py
> # リストはミュータブル（ハッシュ法で計算できない性質）なので格納不可
> theSet = {["bar", "red", "blue", "green", "piyo"]}
> print(theSet)
> # TypeError: unhashable type: 'list'
> ```
        - 要素追加のメソッドは`append`ではなく`add`を使用
      - **複数要素**をまとめて編集（追加・削除）する集合に特有の演算
        - 複数の集合から**新しい集合**を作成
            | 使い方             | 結果                                                    |
            |--------------------|---------------------------------------------------------|
            | `集合A l 集合B`    | 集合Aまたは集合Bに含まれる要素の集合（和集合）※`l`は実際はパイプラインと置換          |
            | `集合A & 集合B`    | 集合Aかつ集合Bに含まれる要素の集合（積集合）             |
            | `集合A - 集合B`    | 集合Aから集合Bに含まれる要素を削除した集合（差集合）     |
            | `集合A ^ 集合B`    | 集合Aまたは集合Bの片方だけに含まれる要素の集合（対称差） |

            - コード実行例
            ```py
            copied_trafic_signal_a = trafic_signal.copy() | {"bar", "piyo"}
            copied_trafic_signal_b = trafic_signal.copy() | {"hoge", "foo"}
            print(f"{copied_trafic_signal_a}\n{copied_trafic_signal_b}\n")
            # {'bar', 'red', 'blue', 'green', 'piyo'}
            # {'red', 'blue', 'foo', 'green', 'hoge'}

            print(f"| {copied_trafic_signal_a | copied_trafic_signal_b}")
            # | {'piyo', 'green', 'red', 'hoge', 'foo', 'blue', 'bar'}

            print(f"& {copied_trafic_signal_a & copied_trafic_signal_b}")
            # & {'red', 'green', 'blue'}

            print(f"a-b {copied_trafic_signal_a - copied_trafic_signal_b}")
            # a-b {'bar', 'piyo'}

            print(f"b-a {copied_trafic_signal_b - copied_trafic_signal_a}")
            # b-a {'hoge', 'foo'}

            print(f"b-b {copied_trafic_signal_b - copied_trafic_signal_b}")
            # b-b set()

            print(f"^ {copied_trafic_signal_a ^ copied_trafic_signal_b}")
            # ^ {'hoge', 'foo', 'piyo', 'bar'}
            ```

        - 累算代入文：集合によって左辺（集合A）の**既存内容を編集**

            | 使い方             | 結果                                                    |
            |--------------------|---------------------------------------------------------|
            | `集合A l= 集合B`   | 集合Aに集合Bの要素を追加（和集合の操作） ※`l`は実際はパイプラインと置換                 |
            | `集合A &= 集合B`   | 集合Aに集合Bとの共通要素のみを残す（積集合の操作）       |
            | `集合A -= 集合B`   | 集合Aから集合Bに含まれる要素を削除                       |
            | `集合A ^= 集合B`   | 集合Aに集合Bの要素を追加し、共通要素を削除（対称差の操作） |

            - コード実行例
            ```py
            print(f"{copied_trafic_signal_a}\n{copied_trafic_signal_b}\n")
            # {'bar', 'red', 'blue', 'green', 'piyo'}
            # {'red', 'blue', 'foo', 'green', 'hoge'}

            # copied_trafic_signal_a |= copied_trafic_signal_b
            # print(f"|= {copied_trafic_signal_a}")
            # {'foo', 'piyo', 'blue', 'red', 'green', 'hoge', 'bar'}

            # copied_trafic_signal_a &= copied_trafic_signal_b
            # print(f"&= {copied_trafic_signal_a}")
            # {'blue', 'green', 'red'}

            # copied_trafic_signal_a -= copied_trafic_signal_b
            # print(f"-= {copied_trafic_signal_a}")
            # {'bar', 'piyo'}

            # copied_trafic_signal_b -= copied_trafic_signal_a
            # print(f"-= {copied_trafic_signal_b}")
            # {'foo', 'hoge'}

            copied_trafic_signal_a ^= copied_trafic_signal_b
            print(f"^= {copied_trafic_signal_a}")
            # {'bar', 'foo', 'piyo', 'hoge'}
            ```

  - **辞書**（`dict({"key": "value"}) # {'key': 'value'} という dict[str, str] を生成`）
    - キーと値のペアを格納するコレクション（`JavaScript`でいうオブジェクトに近い）
    ```py
    for i in range(10):
      theDict: dict[str, str] = {f"key-{i}": f"value-{i}"}
      print(theDict)
      
    # {'key-0': 'value-0'}
    # {'key-1': 'value-1'}
    # {'key-2': 'value-2'}
    # {'key-3': 'value-3'}
    # {'key-4': 'value-4'}
    # {'key-5': 'value-5'}
    # {'key-6': 'value-6'}
    # {'key-7': 'value-7'}
    # {'key-8': 'value-8'}
    # {'key-9': 'value-9'}
    ```

    - 辞書の生成と各種データ構造からの変換
    ```py
    # 辞書の生成
    lang_dict = {"ja": "japanese", "en": "English", "fr": "french"}
    print(lang_dict)

    add_default_dict = dict(ja="japanese", en="English", fr="french")
    print(add_default_dict)

    # 他のデータ構造からの変換（dictで辞書生成）
    created_dict_target_Set = {("green", "hoge"), ("red", "foo")}
    created_dict_Set = dict(created_dict_target_Set)
    print(created_dict_Set) # 集合から
    # {'red': 'foo', 'green': 'hoge'} # 集合は取り出す順序がランダム

    created_dict_target_List = [("green", "hoge"), ("red", "foo")]
    created_dict_List = dict(created_dict_target_List)
    print(created_dict_List) # リストから
    # {'green': 'hoge', 'red': 'foo'}

    created_dict_target_Tuple = (["green", "hoge"], ["red", "foo"])
    created_dict_Tuple = dict(created_dict_target_Tuple)
    print(created_dict_Tuple) # タプルから
    # {'green': 'hoge', 'red': 'foo'}
    ```

    - 辞書（`key`+`value`）または辞書の`key`や`value`の取り回し
    ```py
    lang_dict = {"ja": "japanese", "en": "English", "fr": "french"}

    # キーの繰り返し
    for key in lang_dict.keys():
        print(key)
    # ja
    # en
    # fr

    # 値の繰り返し
    for value in lang_dict.values():
        print(value)
    # japanese
    # English
    # french

    # キーと値のペアの繰り返し
    for key, value in lang_dict.items():
        print(f"{key}: {value}")
    # ja: japanese
    # en: English
    # fr: french
    ```

  - **所属検査演算（メンバーシップテスト演算）**<br>
  指定した値が含まれているか瞬時に判定する演算
  ```py
  trafic_signal = {"green", "red", "blue"}
  print(f"{'green' in trafic_signal} # True")
  print(f"{'pink' in trafic_signal} # False")
  print(f"{'purple' not in trafic_signal} # True")
  print(f"{'red' not in trafic_signal} # False")
  ```

## 条件文
  - `if`
    - Python
    ```py
    isBool: bool = True
    if not (isBool):
      # False 判定の処理

    if isBool:
      # True 判定の処理

    # 複数条件
    if(A and B and C) # A かつ B かつ C
    if(A or B or C) # A または B または C

    elif 別の条件:
      # 別の条件が True 判定の処理

    else:
      # どの条件にも合致しなかった場合の処理
    ```

    - JavaScript
    ```js
    const isBool: boolean = true;
    if(!isBool) {
      // False 判定の処理
    }

    if(isBool) {
      // True 判定の処理
    }

    // 複数条件
    if(A && B && C) // A かつ B かつ C
    if(A || B || C) // A または B または C

    else if(別の条件) {
      // 別の条件が True 判定の処理
    }

    else {
      // どの条件にも合致しなかった場合の処理
    }
    ```

  - 三項演算子
  ```py
  # trueの値 if 条件 else falseの値
  result = "passed" if score >= 60 else "failed"
  ```

  - `AND演算子`と`OR演算子`
  `Python`における`AND演算子`は`&&`ではなく`and`、`OR演算子`は`||`ではなく`or`と記述する。
  ```py
  # AND演算子（左辺が True の場合に右辺を返す ※False の場合は左辺の結果（False）を返す）
  result_entries_1 = (
    entries_1.count("tion") > 0 and f"entries_1: {entries_1.count('tion')}"
  )

  # OR演算子（左辺が False の場合に右辺を返す ※True の場合は左辺の結果（True）を返す）
  result_entries_1 = len(entries_1) <= 0 or f"entries_1: {len(entries_1)}"
  print(entries_1, result_entries_1)
  ```

## `JavaScript（TypeScript）`と`Python`の似ている記法まとめ
- `f文字列`：`JavaScript`でいうテンプレートリテラル（バックティック）
  - `TypeScript（JavaScript）`
  ```js
  const name: string = "John";
  const age: number = 30;
  console.log(`My name is ${name} and I am ${age} years old.`);
  ```
 
  - `Python`
  ```py
  name = "John"
  age = 30
  print(f"My name is {name} and I am {age} years old.")
  ```

- `三項演算子（条件式）`
  - `TypeScript（JavaScript）`
  ```js
  const score: number = 85;
  const result: string = score >= 60 ? "passed" : "failed";
  console.log(`"You ${result} the test.`);
  ```
 
  - `Python`
  ```py
  score = 85
  # trueの値 if 条件 else falseの値
  result = "passed" if score >= 60 else "failed"
  print(f"You {result} the test.")
  ```

- 配列/リストの操作
  - `TypeScript（JavaScript）`
  ```js
  const numbers: number[] = [1, 2, 3, 4, 5];
  // [2, 4, 6, 8, 10]
  const doubled = numbers.map(n => n * 2);
  // 2で割り切れる要素：[2, 4]
  const evens = numbers.filter(n => n % 2 === 0);
  ```
  
  - `Python`
  ```py
  numbers = [1, 2, 3, 4, 5]
  # [2, 4, 6, 8, 10]
  doubled = list(map(lambda n: n * 2, numbers))
  # [2, 4]
  evens = list(filter(lambda n: n % 2 == 0, numbers))
  ```
    - または`内包表記`を使用
    ```py
    doubled = [n * 2 for n in numbers]
    evens = [n for n in numbers if n % 2 == 0]
    ```

- 分割代入
  - `TypeScript（JavaScript）`
  ```js
  const [first, second] = [1, 2];
  const {name, age} = {name: "John", age: 30};
  ```

  - `Python`
  ```py
  first, second = [1, 2]
  person = {"name": "John", "age": 30}
  name, age = person.values()
  ```

- 引数のデフォルト値を設定
  - `TypeScript（JavaScript）`
  ```js
  function greet(name: string = "Guest"): string {
    return `Hello, ${name}!`;
  }
  ```

  - `Python`
  ```py
  def greet(name="Guest"):
    return f"Hello, {name}!"
  ```

- 辞書（`Python`）とオブジェクト（`JavaScript`）の取り回し
  - `TypeScript（JavaScript）`
  ```js
  const lang_dict = {"ja": "japanese", "en": "English", "fr": "french"}
  console.log(Object.keys(lang_dict)) // {dict}.keys()
  console.log(Object.values(lang_dict)) // {dict}.values()
  console.log(Object.entries(lang_dict)) // {dict}.items()
  ```

  - `Python`
  ```py
  lang_dict = {"ja": "japanese", "en": "English", "fr": "french"}

  lang_dict_keys = lang_dict.keys()
  print(lang_dict_keys) # Object.keys(object)

  lang_dict_values = lang_dict.values()
  print(lang_dict_values) # Object.values(object)

  lang_dict_items = lang_dict.items()
  print(lang_dict_items) # Object.entries(object)
  ```

- クラス
  - `TypeScript（JavaScript）`
  ```js
  class Person {
    // インスタンスのプロパティ初期化
    // private 修飾子により、クラス外から直接アクセスできないプロパティとして宣言
    // ちなみに、protected 修飾子だと、同じクラス内と子クラス（サブクラス）からのみアクセスが許される
    constructor(private name: string, private age: number) {}
    
    // メソッドを定義
    greet(): string {
        return `Hello, I'm ${this.name}`;
    }
  }
  ```

  - `Python`
  ```py
  class Person:
    # インスタンスのプロパティ初期化
    # self により、インスタンスに属するプロパティを定義
    # self.XXXX：インスタンス変数を設定
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # メソッドを定義
    def greet(self):
        return f"Hello, I'm {self.name}"
  ```

---

## 参照
- [【令和6年最新版】初心者でも、チーム開発でも美しく！Python開発環境構築のすすめ](https://qiita.com/musutafakemaru/items/332bd0193828aa66461d)
- [Pythonでのデバッグ、print()からic()に置き換えよう！](https://qiita.com/ryosuke_ohori/items/11b2ad43f1ae50f25cf5)
