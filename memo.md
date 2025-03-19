## 備忘録 / 雑多メモ
### オフサイドルール
`Python`では、インデントやスペースがコード整形ではなく**コードの意図や構造を表現する**オフサイドルールが適用されている。

### 処理（`Pythonインタプリンタ`）の終了方法
バックエンド言語なのでターミナル・コマンドプロンプトでの処理実行が多い。もし処理を終了したい場合は以下の操作を行う。
  - Windows<br>
  `ctrl + z`+`enter`キー押下
  - Mac/Linux<br>
  `com/ctrl + d`
  - Windows/Mac/Linux 共通<br>
  `quit()`または`com/ctrl + c`（`KeyboardInterrupt`：キーボードによる中断）

### 変数について
`Python`では、`JavaScript`でいう変数宣言（`let`や`const`）を用いずに変数を作成するため`var`のように再宣言も再代入（再定義）も可能な仕様になっている。<br>
例えば、定数を作成する方法は無く普通の変数を使用するため、変更（再代入）しようと思えばできてしまう。<br>
また、命名規則について**単語の区切りは基本的にスネークケース**で行う。

#### 定数について
慣習的に**定数には大文字を用いてプログラマーに明示的に定数である意図表示**を行う（結局、仕様としては書き換え可能ではあるが）。

> [!NOTE]
> `Python`では、変数は明示的に管理・把握しやすくするためにあるもので、実際は**値ごとに付与される参照値（メモリアドレス）に紐づく**形で管理される言語仕様になっている。<br>
> 参照値（メモリアドレス ／ オブジェクトID）の確認は`id(変数)`で行える。

#### その他特徴（`global` / `nonlocal`）
- `Python`では**スコープ内に同名の変数がある場合はスコープ内のものが優先（適用）される**が`global`宣言子を用いることで**グローバル変数に代入**できる。
```py
def good_morning():
    global txt
    txt = "good morning"
    print(f"good_morning: {txt}")


txt = "good afternoon"
good_morning()
print(txt)

# global 無効時の出力結果
# good_morning: good morning
# good afternoon  # 関数実行時前の代入が有効になっている

# global 有効時の出力結果
# good_morning: good morning
# good morning
```

- **関数内の関数で同名の変数を扱う**かつ上記`global`のような振る舞いを行いたい場合は`nonlocal`を用いる。
```py
def good_morning_afternoon():
    def good_afternoon():
        nonlocal good_afternoon_txt
        good_afternoon_txt = "good afternoon"
        print(f"good_afternoon: {good_afternoon_txt}")

    good_afternoon_txt = "hello world."
    good_afternoon()
    print(f"good_morning_afternoon: {good_afternoon_txt}")


good_morning_afternoon()

# nonlocal 無効時の出力結果
# good_afternoon: good afternoon
# good_morning_afternoon: hello world.  # 関数実行時前の代入が有効になっている

# nonlocal 有効時の出力結果
# good_afternoon: good afternoon
# good_morning_afternoon: good afternoon
```

### 計算式について
`Python`の計算式は、原則「左結合（左側にある式を優先的に計算）」するが`**`（べき乗）のみ「右結合」で処理（計算）される。明示的に`()`を使って計算式を書くのが無難。

#### 除算（割り算）について
`/`を用いて除算（割り算）を行うと浮動小数点（型）として、`//`を用いて除算を行うと整数（型）として扱われる。
```py
print(4 / 2)  # 2.0
print(4 // 2) # 2
```

#### 桁数の調整
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
theBool: bool = True または False

# TypeScript `const theAry_str: string[]`
theAry_str: list[str] = ['hoge', 'foo', 'bar']

# TypeScript `const theAry_int: number[]`
theAry_int: list[int] = [10, 100]

# TypeScript `const theAry_StrOrInt: (string | number)[]`
theAry_StrOrInt: list[str | int] = [10, "hoge", 100, "foo", True] # True は 1 として扱われる（bool は int としても扱えるため）が、明示的に 1 に置き換えた方がわかりやすい
```

---

## `JavaScript（TypeScript）`と`Python`の似ている記法まとめ
### `f文字列`：`JavaScript`でいうテンプレートリテラル（バックティック）
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

### `三項演算子（条件式）`
  - `TypeScript（JavaScript）`
  ```js
  const score: number = 85;
  const result: string = score >= 60 ? "passed" : "failed";
  console.log(`"You ${result} the test.`);
  ```
 
  - `Python`
  ```py
  score = 85
  # <trueの値> if <条件> else <falseの値>
  result = "passed" if score >= 60 else "failed"
  print(f"You {result} the test.")
  ```

### 配列/リストの操作（`map`, `filter`）
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

### 引数のデフォルト値を設定
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

### 辞書（`Python`）とオブジェクト（`JavaScript`）の取り回し
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

### 分割代入
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
