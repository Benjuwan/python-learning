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

> [!NOTE]
> #### 数値型の真偽値判定
> 0は`False`、（負の値含む）0以外は`True`という判定になる

### 三項演算子（条件式）
```py
# <trueの値> if <条件> else <falseの値>
result = "passed" if score >= 60 else "failed"
```

### `AND演算子`と`OR演算子`
`Python`における`AND演算子`は`&&`ではなく`and`、`OR演算子`は`||`ではなく`or`と記述する。

> [!NOTE]
> **`OR演算子`よりも`AND演算子`の方が演算子の優先順位が高い**ので、両方を一度の処理に含む場合は注意すること。

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
`Python`には、厳密等価演算子（`===`,`!==`）がない。

> [!NOTE]
> 数値を`==`（または`is`）や`!=`（または`is not`）で比較する際には、**`Python`処理系が自動的に両者の型を合わせて（暗黙的型変換）から値を比較**してくれる。<br>
> より厳密に判定したい場合は`type(変数-a) == type(変数-b)`, `type(変数-a) != type(変数-b)`のように記述する。

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
