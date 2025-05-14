import pandas
from matplotlib import pyplot

"""
`Pandas`では`DataFrame`（データフレーム）と呼ばれるオブジェクトが主要な機能で、このオブジェクトを通じてCSVファイルのデータ（値や特定要素）の取得及び演算などを行える。

また、数値以外のデータを扱うことも可能で、列名を指定して列操作することもできるのが特徴。

内部で`NumPy`が利用されている。
"""

# Pandas で csvファイルを読み込む
"""
- read_csv()関数
csvファイルを読み込んでデータフレームオブジェクトを返す
```
データフレーム = pandas.read_csv(ファイル名, encoding=文字エンコーディング)
```
"""
csv_detaframe = pandas.read_csv(
    "../PythonSample/chapter13/score2.csv", encoding="utf-8"
)
# print(csv_detaframe)

print("-" * 45)

# データフレームの最初の指定した行数を取得（※行数を省略すると5行分取得）
print(csv_detaframe.head(3))

# データフレームの最後の指定した行数を取得（※行数を省略すると5行分取得）
print(csv_detaframe.tail())

print("-" * 45)

"""
（指定した列名）列を取得
```
データフレーム[列名]
```
"""
print(csv_detaframe["Japanese"])

"""
ブラケットでネストして複数の列名を一挙に取得（※各列を比較する際などに使用）
```
データフレーム[[列名, ...]]
```
"""
print(csv_detaframe[["Japanese", "Math"]])

print("-" * 45)

"""
Pandas での行の取得はスライスを用いる
```
データフレーム[開始行番号:終了行番号]
```
"""
print(csv_detaframe[0:10])

"""
ステップを指定して複数行ごとに取得することも可能
```
データフレーム[開始行番号:終了行番号:ステップ]
```
"""
print(csv_detaframe[0:10:3])
print("-" * 45)

"""
列と行を同時に取得
```
# 記述順は「行と列」どちらを先に書いても問題ない
データフレーム[列名][行のスライス]
データフレーム[行のスライス][列名]
```
"""
print(csv_detaframe["Japanese"].head())
print(csv_detaframe["Japanese"][0:3])
print(csv_detaframe[3:5]["Japanese"])
print("-" * 45)

# NumPy 同様に「ブール配列インデックス」を使用できる
# データフレーム[式]
print(csv_detaframe[csv_detaframe["Japanese"] >= 95])  # 国語の点数が95点以上の行を取得

print("-" * 45)

# 複数条件の場合は各条件を()で囲う
print(
    csv_detaframe[
        (csv_detaframe["English"] == 100) | (csv_detaframe["Japanese"] == 100)
    ]
)  # 英語または国語の点数が100点の行を取得

print("-" * 45)

"""
条件に合う要素だけを取得する`query`メソッド
```
データフレーム.query(文字列)
```
"""

print(csv_detaframe.query("Japanese >= 95"))
print(csv_detaframe.query("English == 100 or Japanese == 100"))
print("-" * 45)

"""
複雑な複数条件の場合は NumPy 同様に any, all を利用して対応する
※こちらも同様に「軸番号の指定が必要」なので注意
# NumPy のように NumPy オブジェクト（ライブラリ）を起点に各種メソッドを実行しないことに注意

- `all`: 全ての条件がTrueの場合にTrueを返す
```
データフレーム.all(配列, 軸番号)
```

- `any`: いずれかの条件がTrueの場合にTrueを返す
```
データフレーム.any(配列, 軸番号)
```

※軸番号は`axis`キーワード引数を用いることでも指定可能

- 多次元配列の場合
最も外側の角括弧が0次元目、次の角括弧が1次元目、...と数えていく。
例えば、二次元配列の場合は軸番号に0を指定すると「全ての行」について、1を指定すると「全ての列」について、要素の真偽値を合成する
"""

# いずれかが100点の行を取得
# NumPy のように NumPy オブジェクト（ライブラリ）を起点に any メソッドを実行しないことに注意
print(csv_detaframe[(csv_detaframe == 100).any(axis=1)])

# 1. (csv_detaframe == 100)：全要素に対する真偽値のデータフレーム
# 2. 上記データフレームの真偽値を any(axis=1) で全ての列方向について合成し、行ごとの真偽値を決定する
# 3. ブール配列インデックスの処理で（式に合致した）特定行を取得する

print("-" * 45)

"""
データフレームからは、データ（値や要素）を呼び出すだけでなく書き込むことも可能。例えば、データフレーム上の値を使って計算し、新たに（列を）追加するといったことができる。既存の行を指定した場合は上書きされる。

```
データフレーム[列名] = 値
```

上記記述（※列名には既存の列名と異なる新しい列名を指定すること）で新しい列を追加することができ、新規追加された列は既存列の末尾に挿入される。

- 単独の値を指定した場合「全ての行に同じ値がコピー」される
- 既存の行と行数が等しいデータフレームを指定した場合「既存の行に並ぶ形で新しい列が追加」される
"""

# csv_detaframe["Total"] = (
#     csv_detaframe["English"] + csv_detaframe["Math"] + csv_detaframe["Japanese"]
# )
# print(csv_detaframe)

"""
上記のような加算（合算）処理は sum メソッドを用いて実装するといちいち列名を記述する必要が無くなって効率的
```
データフレーム.sum(軸番号)
```

軸番号に0を指定すると「全ての行」について、1を指定すると「全ての列」について処理する
"""

csv_detaframe["Total"] = csv_detaframe.sum(axis=1)
print(csv_detaframe)

print("-" * 45)

"""
不要な列は del で削除できる
```
del データフレーム[列名]
```
"""
# del csv_detaframe["Total"]
# print(csv_detaframe)

"""
- CSVファイルへの保存
to_csv()メソッドは、デフォルトでは各行先頭に行番号を付与して出力する
```
データフレーム.to_csv(ファイル名)
```
既存ファイルを指定した場合は上書き保存される

デフォルト設定（行番号付与）が不要な場合は index キーワード引数に False を指定する
```
データフレーム.to_csv(ファイル名, index=False)
```
"""

csv_detaframe.to_csv("../anothers/lib-pandas.csv", index=False)

print("-" * 90)

"""
matplotlib セクション
"""

score = pandas.read_csv("../PythonSample/chapter13/score2.csv", encoding="utf-8")

pyplot.figure()

print("-" * 90)

"""
scikit-learn セクション
"""

print("-" * 90)
