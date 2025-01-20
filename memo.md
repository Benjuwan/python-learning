## 備忘録・メモ
- オフサイドルール<br>
`Python`では、インデントやスペースがコード整形ではなく**コードの意図や構造を表現する**オフサイドルールが適用されている。

- 変数について<br>
`Python`では、`JavaScript`でいう変数宣言（`let`や`const`）を用いずに変数を作成するため`var`のように再宣言も再代入もお構いなく可能な仕様になっている。<br>例えば、定数を作成する方法は無く普通の変数を使用するため、変更（再代入）仕様と思えばできてしまう。
  - 定数について<br>
  慣習的に**定数には大文字を用いてプログラマーに明示的に定数である意図表示**を行う（結局、仕様としては書き換え可能ではあるが）。<br>また、単語の区切りは基本的にスネークケースで行う。

- 厳密等価演算子<br>
`Python`には、厳密等価演算子（`===`,`!==`）がないが、数値を`==`や`!=`で比較する際に`Python`処理系が自動的に両者の型を合わせて（暗黙的型変換）から値を比較してくれる。

- 計算式について<br>
`Python`の計算式は、原則「左結合（左側にある式を優先的に計算）」するが`**`（べき乗）のみ「右結合」で処理（計算）される。明示的に`()`を使って計算式を書くのが無難。

- 繰り返し処理
```py
# リストの要素を直接繰り返し
for element in array:
    print(element)

# 数値範囲での繰り返し
for i in range(len(array)):
    print(array[i])

# インデックスと要素の両方を使う場合
# enumerate：イテラブル（反復可能なオブジェクト）に対して各要素とそのインデックスをペアとして返す
for i, element in enumerate(array):
    print(f"{i}: {element}")
```

- `Python`での配列操作について（シャローコピーの必要性有無）
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

- 型定義について
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

- リスト（配列）について
目的に応じた適切なデータ構造を用いるのが大切
  - リスト： 最もベーシックで無難なミュータブルなデータ構造
  - タプル： イミュータブル（不変）にした場合
  - 集合： 検索を速くしたい場合
  - 辞書： 検索を速くしたい場合

  - リストの生成<br>`list(イテラブル：繰り返し可能なオブジェクト)`

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

- `JavaScript`でいう`三項演算子`
  - `TypeScript（JavaScript）`
  ```js
  const score: number = 85;
  const result: boolean = score >= 60 ? "passed" : "failed";
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
