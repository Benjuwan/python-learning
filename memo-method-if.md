## 関数・メソッド（クラス）
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

### `join()`
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

### `sorted`
ソート機能。第二引数として`reverse`というキーワード引数が用意されており`True`にすることで反転できる。
```py
some_numbers = [100, 10, 25, 8, 64]

# [8, 10, 25, 64, 100]
print(sorted(some_numbers))

# [100, 64, 25, 10, 8]
print(sorted(some_numbers, reverse=True))
```

- 参照：[`Python`での配列操作について（シャローコピーの必要性有無）](#pythonでの配列操作についてシャローコピーの必要性有無)

### `min`, `max`
イテラブルから最小（`min`）、最大（`max`）の要素・値を取得する。
```py
some_numbers = [100, 10, 25, 8, 64]
print(min(some_numbers))  # 8
print(max(some_numbers))  # 100
```

## 関数定義
他の言語同様`関数名(引数, ...)`という形で記述していくし、関数の呼び出し方も同じだが、`def`という宣言子を前置したり、`関数名(引数, ...):`パラメータ後に`:`を置いたり`Python`独自の記法もある。<br>
**関数の命名規則もまた変数同様に区切り部分はアンダースコア`_`で繋いでいく**のが一般的。<br>
使用頻度の低い引数にはデフォルト値を設けて省略することもできる。<br><br>

> [!NOTE]
> - 引数のデフォルト値について<br>
> 引数にデフォルト値を設定する場合`args=default_value`という形、つまり**キーワード引数**のような形式になる。<br>
> しかしデフォルト値を指定した引数はキーワード引数として扱われるわけではなく、あくまで**実際に使用時に指定する引数の在り方**でキーワード引数を判定している。
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

### 例外処理（`try - except`）
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

- `raise`（レイズ）<br>
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

## 条件文
### `if`
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

### 三項演算子
```py
# <trueの値> if <条件> else <falseの値>
result = "passed" if score >= 60 else "failed"
```

### `AND演算子`と`OR演算子`
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

### 厳密等価演算子
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

### `in`： 所属検査演算（メンバーシップテスト演算）
指定した値が含まれているか瞬時に判定する演算
```py
trafic_signal = {"green", "red", "blue"}
print(f"{'green' in trafic_signal} # True")
print(f"{'pink' in trafic_signal} # False")
print(f"{'purple' not in trafic_signal} # True")
print(f"{'red' not in trafic_signal} # False")
```

#### `in`演算子, `not in`演算子は**各種データ構造（リスト、タプル、集合、辞書）のほか、文字列にも使用**できる
```py
# 値が含まれていることを判定（in演算子）
値 in イテラブルまたは文字列

# 値が含まれていないことを判定（not in演算子）
値 not in イテラブルまたは文字列
```
ハッシュ法のおかげで集合と辞書は特に`in`と`not in`を高速に実行できる。

---

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

---
