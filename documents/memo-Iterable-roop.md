## イテラブル（反復可能なオブジェクト・繰り返し可能要素）や`Python`の各種データ構造
目的に応じた適切なデータ構造を用いるのが大切

### リスト
#### リストの特徴
- シーケンスなのでインデックスやスライスが扱える
  - シーケンス：<br>
  文字列やリストなどインデックスで要素の位置を指定（＝指定したインデックスで要素を取得）できるオブジェクトのこと
- ミュータブルなので、要素の追加や削除が可能

---

最もベーシックで無難なミュータブルなデータ構造。
```py
# 9までの list[int] を生成
list(range(10))
```

- `list()`関数に`辞書{dict}`を渡すと、デフォルトで`辞書`の`key`のイテレータを返す
```py
lang_dict = {"ja": "japanese", "en": "English", "fr": "french"}
print(list(lang_dict))
# ['ja', 'en', 'fr']
```

- リストのコピー（シャローコピー）<br>
`JavaScript`のそれ同様**破壊的処理によって元の配列（の中身）が変わってしまう**ケースがあるので適宜シャローコピーを用いるのが大切
```py
# スライス
copied_lists = リスト変数[:]

# copy メソッド
copied_lists = リスト変数.copy()
```

---

> [!NOTE]
> - `Python`でのスライス<br>
> `JavaScript`の`slice(開始インデックス, 終了インデックス)`と異なり、`Python`では`[開始インデックス:終了インデックス:ストライド]`という記述で配列のスライスを実現する。
> ```py
> # 先頭から終了インデックスまで
> 文字列またはイテラブル[:終了インデックス]
> 
> # 開始インデックスから末尾まで
> 文字列またはイテラブル[開始インデックス:]
> 
> # 先頭から末尾まで
> 文字列またはイテラブル[:]
>
> # （開始インデックスが負の値なので）末尾から先頭まで
> # （例：最後の5つを取得）
> 文字列またはイテラブル[-5:] # 末尾-5から先頭まで
> ```
> 
> - ストライドについて<br>
> ステップとも呼ばれるオフセットのことで**要素を指定した個数ごとに取り出す**ための機能。
> ```py
> # 1文字目から末尾まで 2ストライドごとに抽出
> print("-W-E-L-C-O-M-E-"[1::2])
> ```

---

##### リストでの要素の取り扱い
  - 要素の追加
  ```py
  リスト.append(値) # 破壊的処理

  # 累算代入文（破壊的処理）
  リスト変数 += イテラブル
  # JavaScript でいうpushメソッドによる結合と近いニュアンス
  # リスト.push(...イテラブル)

  # extend メソッド（破壊的処理）
  リスト.extend(イテラブル)

  # スライス（破壊的処理）
  リスト[len(リスト):] = イテラブル
  ```

  - 任意の箇所へ要素を追加<br>
  `JavaScript`でいう`splice`メソッドに近いニュアンス
  ```py
  # リストの途中に要素を挿入
  リスト.insert(インデックス, 値)

  # スライス
  リスト[開始インデックス:終了インデックス] = イテラブル
  # 空リストを代入することで指定した範囲の要素を削除可能
  リスト[開始インデックス:終了インデックス] = []
  ```

  - リストの連結・結合
  ```py
  # 新しい変数に代入する形
  concat_lists = list_a + list_b

  # JavaScript でいうスプレッド演算子での展開結合または、concatメソッドによる結合と近いニュアンス
  # const concat_lists = [...list_a, ...list_b];
  # list_a.concat(list_b)

  # 既存のリストを更新する形（累算代入文）
  list_a += list_b

  # JavaScript でいうpushメソッドによる結合
  # list_a.push(...list_b)
  ```

  - リストの削除
  ```py
  del リスト[インデックス]

  リスト.pop(インデックス)
  # JavaScript と違って引数にインデックス（数値型）を取る

  リスト.remove(値)

  # 指定した範囲の削除
  # 終了インデックスに対応する要素は除外される（取り出されない）ので注意
  del リスト[開始インデックス:終了インデックス]

  # 空リストを代入する方法
  リスト[開始インデックス:終了インデックス] = []

  # 全て削除
  リスト.clear()

  # JavaScript でいう splice(0)
  # const lists: string[] = ["beer", "wine", "whisky", "water", "soda"];
  # lists.splice(0);

  # リストが変数に代入されている場合
  # 空配列を代入することで全削除が可能
  リスト変数 = []
  ```

### タプル
#### タプルの特徴
- シーケンスなのでインデックスやスライスが扱える
- **イミュータブルなので要素の変更や追加、削除といった編集操作は受け付けない**

---

リストなど他のデータ構造と違って **「配列数が固定で、中身・要素（の型）は自由」** というイミュータブルなデータ構造。
```py
# 9までの tuple[int, ...] を生成
tuple(range(10))

# () で要素を囲う 
theTuple = ("Alice", 24, "tokyo", 23.5)

# 要素が一つの場合
# タプルと認識してもらうには末尾に , が必要
theSingleTuple = ("Alice", )
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

### 集合
#### 集合の特徴
- ミュータブルなので、要素の追加や削除が可能
- 同じ値を重複して保存（格納）できない
- **値を取り出す時の順序が保証されない**（例：出力する度に並び順が変わる）
- **イミュータブルな値のみ格納可能**（※厳密にはハッシュが計算できる値のみ格納可能）
- 指定した値が含まれているか瞬時に判定できる

---

数学の集合論をベースにした、重複のない要素のコレクション。
```py
# 9までの set[int] を生成
set(range(10))

# {} で要素を囲う 
# リストから集合を作成（重複は自動的に削除）
numbers_set = set([1, 2, 2, 3, 3, 4])
numbers = {1, 2, 2}
number = {1}
print(numbers_set, numbers, number)

trafic_signal = {"green", "red", "blue"}
# 値を取り出すときの順序が保証されない
print(trafic_signal) # {'green', 'blue', 'red'}
```

> [!NOTE]  
> ##### `list`はミュータブルなので {集合} には格納不可能
> ```py
> # リストはミュータブル（ハッシュ法で計算できない性質）なので格納不可
> theSet = {["bar", "red", "blue", "green", "piyo"]}
> print(theSet)
> # TypeError: unhashable type: 'list'
> ```

##### 集合での要素の取り扱い
  - `add`<br>
  要素追加のメソッドは`append`ではなく`add`を使用する
  ```py
  集合.add(値)
  # the_set.add("hoge")

  # 累算代入文で追加
  集合 |= {値, ...}
  # the_set |= {"foo", "bar"}
  ```

  - `remove`<br>
  要素を削除。指定した値が当該集合に含まれていない場合は`KeyError`という例外が発生する。
  ```py
  集合.remove(値)

  # 累算代入文で削除
  集合 -= {値, ...}
  ```

  - `pop`<br>
  ```py
  # 先頭から一つ削除（※ JavaScript のそれとは逆なので注意）
  集合.pop()
  ```

  - `clear`<br>
  全ての要素を削除
  ```py
  集合.clear()
  ```

  - `discard`<br>
  要素を削除。指定した値が当該集合に含まれていない場合は何もしない。
  ```py
  集合.discard(値)
  ```

  - **複数要素**をまとめて編集（追加・削除）する集合に特有の演算
    - 複数の集合から**新しい集合**を作成
      - `集合A | 集合B`： <br>
      集合A または集合B に含まれる要素の集合（和集合）
      - `集合A & 集合B`： <br>
      集合A かつ集合B に含まれる要素の集合（積集合）  
      - `集合A - 集合B`： <br>
      集合A から集合B に含まれる要素を削除した集合（差集合）
      - `集合A ^ 集合B`： <br>
      集合A または集合B の片方だけに含まれる要素の集合（対称差）

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
      - `集合A |= 集合B`：<br>
      集合A に集合B の要素を追加（和集合の操作）
      - `集合A &= 集合B`：<br>
      集合A に集合B との共通要素のみを残す（積集合の操作）
      - `集合A -= 集合B`：<br>
      集合A から集合B に含まれる要素を削除
      - `集合A ^= 集合B`：<br>
      集合A に集合B の要素を追加し、共通要素を削除（対称差の操作）

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

> [!NOTE]
> #### `frozenset()`関数
> ミュータブルな集合を生成する`set()`とは異なり、`frozenset()`は**イミュータブルな集合（オブジェクト）を生成**する<br>
> 用途としては「集合を（イミュータブルな値しか格納できない）集合に格納」する場合や「集合を（イミュータブルなキーしか指定できない）辞書のキーに使用」する場合など

### 辞書
#### 辞書の特徴
- ミュータブルなので、要素の追加や削除が可能
- 同じキーを重複して格納できない（※値は重複してもよい）
  - 指定したキーが既にある場合は、**そのキーに対応する値が書き換え**られる。指定したキーが含まれていない場合は、**キーと値の組が新たに追加**される。
- **イミュータブルなキーのみ**格納できる（※値はミュータブルでもよい）
- キーを取り出す時の順序はキーの格納順となる

---

キーと値のペアを格納するコレクション（`JavaScript`でいうオブジェクトに近い）。
```py
# {'key': 'value'} という dict[str, str] を生成
dict({"key": "value"})

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

##### 辞書での要素の取り扱い
  - `get`<br>
  指定したキーに対応する値を取得できる。当該辞書に含まれないキーを指定かつデフォルト値も指定されていない場合は`None`が返ってくる（デフォルト値が指定されている場合はデフォルト値を返す）。
  ```py
  # 指定した
  辞書.get(キー)
  辞書.get(キー, デフォルト値)
  ```

  - 要素の追加または更新（`辞書[キー] = 要素`）<br>
  辞書に要素を追加（指定したキーが当該辞書に含まれていない場合は、**キーと値の組が新たに追加**される。含まれている場合は、**そのキーに対応する値が書き換え**られる）

  - 異なる辞書同士の結合
  ```py
  dict1 = {'a': 1, 'b': 2}
  dict2 = {'b': 3, 'c': 4}

  # 新しい辞書を作成 (Python 3.9以降)
  merged = dict1 | dict2  # {'a': 1, 'b': 3, 'c': 4}

  # 既存の辞書を更新 (Python 3.9以降)
  dict1 |= dict2  # dict1は{'a': 1, 'b': 3, 'c': 4}になります
  ```
  ※キーが重複する場合は**常に後の辞書（右側の辞書）の値が優先**されるので注意

  - `del`<br>
  指定したキー（キーと値の組＝要素）を削除する。当該辞書に含まれていない場合は例外（`KeyError`）が発生する。
  ```py
  del 辞書[キー]
  ```

  - `pop`<br>
  指定したキー（キーと値の組＝要素）を削除し、対応する値を返す。当該辞書に含まれないキーを指定かつデフォルト値も指定されていない場合は例外（`KeyError`）が発生する（デフォルト値が指定されている場合はデフォルト値を返す）。
  ```py
  辞書.pop(キー)
  辞書.pop(キー, デフォルト値)
  ```
  
  - `clear`<br>
  辞書の全ての要素を削除
  ```py
  辞書.clear()
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

## オブジェクト
`Python`でいうオブジェクトとは、**特定の機能や挙動（振る舞い）を実現するためのデータや処理（操作）をひとまとめにしたデータ構造体**を指す。それら**オブジェクトを組み合わせてプログラムを構築・開発していくのをオブジェクト指向プログラミング（OOP）**としている。<br>
※他方、`FP`とは関数プログラミングを指す。<br><br>
各オブジェクトがどのようなデータ構造を持っているのかは**クラスを通じて定義**し、先の「特定の機能や挙動を実現する」ための**データをデータ属性**、**処理（に該当する属性）をメソッド**と呼ぶ。<br>
クラスは「設計図」で、「その設計図から生成される実体・実物」をインスタンスといい、一般的にオブジェクトとはこのインスタンスオブジェクトを指す。

---

> [!NOTE]
> ※インスタンス生成時において`JavaScript`のように`new`を接頭辞として前置する必要ない。クラスの作成は似たような記述となっている。
> - `TypeScript（JavaScript）`
> ```js
> class Person {
>   // インスタンスのプロパティ初期化
>   // private 修飾子により、クラス外から直接アクセスできないプロパティとして宣言
>   constructor(private name: string, private age: number) {}
> 
>   // メソッドを定義
>   greet(): string {
>     return `Hello, I'm ${this.name}`;
>   }
> }
> ```

---

- `Python`でのクラス指定（生成）
  - `_init__`は、コンストラクタ関数（インスタンスのプロパティ初期化処理）のようなもの
  - `self`は`this`のようなもの
```py
class Food:
    # クラス属性（クラス共通のデータや処理）
    counter = 0

    # __init__ は、コンストラクタ関数（インスタンスのプロパティ初期化処理）のようなもの
    def __init__(self, name, price):
        # self は this のようなもの
        self.name = name
        self.price = price
        Food.counter += 1 # クラス属性

    # （インスタンス）メソッドの作成
    def show(self):
        print(f"No.{Food.counter} / {self.name}: {self.price}")

# 生成時 self に該当する部分（第一引数）は省略
x = Food("milk", 150)
```

- `Python`でのクラスの命名規則：クラス名はパスカルケース（例：HelloWorld）で命名<br>
クラス名の1文字目は大文字で2文字目以降は小文字、複数の単語から構成される場合はパスカルケース（`HelloWorld`）で命名するのが一般的。つまり、変数名や関数名のようにアンダースコア（`_`）を用いた命名規則とは異なる。<br>
※ただし、クラス内のデータ属性名やメソッド名については変数名や関数名の命名規則に準ずるので注意。

- `Python`におけるプライベートメソッド
`Python`では仕様としてのプライベートメソッドはなく（＝すべてパブリックとして扱われる）、`_`を前置したり、マングリングを行ったりして明示的にそれを表現する。
```py
      # _を前置しているだけで、外から呼び出せるので注意
      def __init__(self, name, price):
        self._name = name
        self._price = price

      def show(self):
        print(f"{self._name}: {self._price}")
```

- マングリング（`mangling`：分からなくすること）<br>
念入りに属性への操作を制限したい場合、**属性名の先頭に2個のアンダースコア`__`を付ける**ことで、自動的に`_クラス名__属性名`というような属性名に変換される。<br>
しかし結局はマングリングも**明示的な表現という範疇を超えない**ので注意。<br>
※`__init__`のような前後に2個のアンダースコア`__`が付いたものはマングリングの対象とならない。

### 基底クラス（スーパークラス）と派生クラス（サブクラス）
`JavaScript`のクラスでいう`extends`のように`Python`にも**継承**があり、ニュアンスは`JavaScript`のそれと同じく**親クラスのデータや処理・操作を受け継ぐ**というもの。<br>
※派生の関係を指し示す際に汎化という言葉で関係性を表現する
```py
# Python は単一継承、多重継承の両方とも対応
class SubClass(SuperClass01, SuperClass02, ...):
    # 処理

    # オーバーライド（上書き）機能
    # オーバーライドを実現するには「基底クラスのものと同名（今回の場合は view_els ）」にしなければならない
    def view_els(args, ...):
      # メソッドの処理
```

- 実装例
```py
# 基底クラス（スーパークラス）
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show(self):
        print(f"{self.name}: {self.price}")


# 派生クラス（サブクラス）
class Food(Item):
    # 基底クラスの __init__ 引数も指定する（今回は name, price）
    def __init__(self, name, price, used_limit):
        # JavaScript と同様に super() 関数で基底クラスの該当内容を継承（今回は コンストラクタ部分）
        super().__init__(name, price)
        # 派生クラスの独自部分
        self.used_limit = used_limit

    def show(self):
        # JavaScript と同様に super() 関数で基底クラスの該当内容を継承（showメソッド）
        super().show()
        # 派生クラスの独自部分
        print(f"{self.name}: {self.price}: {self.used_limit}")
```

- `super`関数を使わないと「再帰（関数やメソッドが自分自身を呼び出すこと）エラー（`RecursionError`）」が発生するので注意<br>`Python`ではメモリ負荷の観点から再帰回数に上限が設けられている。

---

> [!NOTE]
> - プログラミングのクラスにおける`各アクセス修飾子`について
>   - **パブリック（`public`）** <br>全体公開。クラス内外から呼び出せる（どこからでも使用できる）。<br>*例：公園のように誰でも利用可能*
>   - **プライベート（`private`）** <br>当該クラス専用。当該クラス内でしか呼び出せない（使用できない）。<br>*例：自室の鍵付きの引き出しのように、自分しか開けられない*
>   - **プロテクティッド（`protected`）** <br>当該クラス及び子孫クラス専用。当該クラスと、その子クラスからしか呼び出せない（使用できない）<br>*例：家族共用のリビングのように、家族（子クラス含む）なら使えるが、外部の人は入れない*

```py
# アクティブラーニングで試用したテキトーな class
class hello_president:
    def __init__(self, name, familyname):
        self.name = name
        self.familyname = familyname

    def console_log(self):
        print(f"hello {self.name} {self.familyname} .")


hello_president("Donald", "Trump").console_log()
hello_president("Jhoe", "Biden").console_log()


# 継承
class hello_president_age(hello_president):
    def __init__(self, name, familyname, birth):
        super().__init__(name, familyname)
        self.birth = birth

    def console_log(self):
        year = int(self.birth[0:4])
        month = int(self.birth[4:6].replace("0", ""))
        day = int(self.birth[5:7].replace("0", ""))

        is_yet_future = (month > int(time.localtime().tm_mon)) or (
            day > int(time.localtime().tm_mday)
        )
        # print(is_yet_future)

        print(
            f"hello {self.name} {self.familyname} . your {(time.localtime().tm_year - year) - 1 if is_yet_future else time.localtime().tm_year - year} age now."
        )


hello_president_age("Donald", "Trump", "19460614").console_log()
hello_president_age("Jhoe", "Biden", "19421120").console_log()
```

## 繰り返し処理
### `for 変数 in イテラブル`
```py
# リストの要素を直接繰り返し
for element in array:
    print(element)

# 数値範囲での繰り返し
for i in range(len(array)):
    print(array[i])
```

### インデックスと要素の両方を使う場合
#### `enumerate`
イニュームレイト：列挙型（`enum`）のことで、イテラブルから要素を取り出す時に何番目に取り出した要素なのかを把握できる。戻り値は **`カウント`と`要素の値`のタプル`tuple()`** となる。
```py
for i, elm in enumerate('イテラブル', '開始値'):
  # 処理
```
第二引数の`開始値`はカウントの開始値を指す。

- 具体例
```py
# enumerate：イテラブル（反復可能なオブジェクト・繰り返し可能要素）に対して
# 各要素とそのインデックスをペアとして返す
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

## イテラブルに関する関数
### `zip`関数
複数のイテラブルに対して同時に繰り返し処理を行いたい場合に便利な関数。<br>
引数に指定された複数のイテラブルから要素を集めて**タプルにまとめて返す**。

```py
food_name = ["burger", "potato", "snack"]
food_price = [110, 150, 120]

# zip(イテラブル, ...)
for food in zip(food_name, food_price):
    print(f"{food[0]} is {food[1]} yen.")
    # burger is 110 yen.
    # potato is 150 yen.
    # snack is 120 yen.

for n, p in zip(food_name, food_price):
    print(f"{n} is {p} yen.")
    # burger is 110 yen.
    # potato is 150 yen.
    # snack is 120 yen.
```

#### `zip`関数を用いた柔軟なイテラブル（リスト）生成
```py
food_name = ["burger", "potato", "snack"]
food_price = [110, 150, 120]

print(list(zip(food_name, food_price)))
# [('burger', 110), ('potato', 150), ('snack', 120)]
```

### `map`関数
指定した処理（条件）で加工した（イテラブル内の）各要素を返す。
```py
map(関数, イテラブル)
```

- 具体例
```py
food_name = ["burger", "potato", "snack"]
food_price = [90, 150, 120]

print(list(map(len, food_name)))        # [6, 6, 5]

# 数値型リストを文字列型リストへ変換し、上記と同じく各要素の文字列数を取得する
convert_str_list = list(map(str, food_price))
print(list(map(len, convert_str_list))) # [2, 3, 3]
```

### `filter`関数
指定した条件に合致する（イテラブル内の）要素を返す。
```py
filter(関数, イテラブル)
```

- 具体例
```py
fruits = ["apple", "", "grape", "melon", "", "", "water-melon"]
print(len(fruits)) # 7

print(list(filter(len, fruits)))
# ['apple', 'grape', 'melon', 'water-melon']
# len が 0以外（以上）のものが True 判定される

print(len(list(filter(len, fruits)))) # 4
```

### all
`JavaScript`でいう`every`にあたる。<br>
イテラブルの全ての要素が（指定した条件に）`True`の場合は`True`を返す。内包表記（`式 for 変数 in イテラブル`）と併用すると便利。
```py
person_a_socre = [90, 75, 88, 100, 82]
person_b_socre = [90, 85, 98, 100, 96]

# 全てが80以上
print(all([score > 80 for score in person_a_socre])) # False
print(all([score > 80 for score in person_b_socre])) # True
```

- `JavaScript`でいう`every`
```js
const person_a_socre = [90, 75, 88, 100, 82];
const person_b_socre = [90, 85, 98, 100, 96];

const all_method = (targetAry)=>{
    const result = targetAry.every(elm=>elm > 80);
    console.log(`${result}：全てが80以上`);
}
all_method(person_a_socre);
all_method(person_b_socre);
```

### any
`JavaScript`でいう`some`にあたる。<br>
どれか一つでも（指定した条件に）`True`の場合は`True`を返す。内包表記（`式 for 変数 in イテラブル`）と併用すると便利。
```py
person_a_socre = [90, 75, 88, 100, 82]
person_b_socre = [90, 85, 98, 100, 96]

# どれか一つでも80未満
print(any([score < 80 for score in person_a_socre]))  # True
print(any([score < 80 for score in person_b_socre]))  # False
```

- `JavaScript`でいう`some`
```js
const person_a_socre = [90, 75, 88, 100, 82];
const person_b_socre = [90, 85, 98, 100, 96];

const any_method = (targetAry)=>{
    const result = targetAry.some(elm=>elm < 80);
    console.log(`${result}：どれか一つでも80未満`);
}
any_method(person_a_socre);
any_method(person_b_socre);
```

### 簡潔にイテレータ（イテラブル内の各要素）を操作できる`iter`関数と`next`関数
```py
some_numbers = [1, 2, 3]
iterator = iter(some_numbers) # iter： 指定されたイテラブルに対するイテレータを返す
print(next(iterator))         # next： 指定されたイテレータから要素を一つ取り出す
print(next(iterator))
print(next(iterator))
print(next(iterator))         # next が無いので StopIteration（例外）発生
```
