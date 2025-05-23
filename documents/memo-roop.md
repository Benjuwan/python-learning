## 繰り返し（ループ）処理
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
