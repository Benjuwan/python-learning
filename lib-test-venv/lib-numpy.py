import numpy as np


def test_numpy():
    # Create a 1D array
    arr_1d = np.array([1, 2, 3])
    assert arr_1d.shape == (3,)
    assert arr_1d[0] == 1

    # Create a 2D array
    arr_2d = np.array([[1, 2], [3, 4]])
    assert arr_2d.shape == (2, 2)
    assert arr_2d[0, 0] == 1

    # Perform element-wise addition
    arr_sum = arr_1d + 10
    assert np.array_equal(arr_sum, np.array([11, 12, 13]))

    # Perform matrix multiplication
    arr_mult = np.dot(arr_2d, arr_2d)
    assert np.array_equal(arr_mult, np.array([[7, 10], [15, 22]]))


# Numpy での CSVファイルの読み込み
# loadtxt() は CSVファイルを読み込み、NumPy の多次元配列（`numpy.ndarray`オブジェクト）を返す
# `delimiter`には","を指定（※値が空白で区切られている場合は省略可能）
# `encroding`には"utf-8"など文字コードを指定する（※ ASCII（アスキー）の場合は省略可能）
# ```
# 配列 = numpy.loadtxt(ファイル名, delimiter=区切り文字, encroding=文字コード)
# ```

numpy_csv_ary = np.loadtxt("../PythonSample/chapter13/score.csv", delimiter=",")
print(numpy_csv_ary[:5])  # 最初の5行
print(numpy_csv_ary[-5:])  # 最後の5行

# 1次元配列に変換
numpy_csv_flat_ary = numpy_csv_ary.flatten()
print(numpy_csv_flat_ary[-5:])  # 最後の5行
# [81. 89. 44.  2.  4.]

# 各配列の要素数を確認
# 配列.shape で各配列の要素数をまとめたタプルを確認できる
print(len(numpy_csv_ary), numpy_csv_ary.shape)
# 200 (200, 3) # 200行3列の2次元配列

# NumPy の多次元配列は、Python のリストと同じようにインデックスを指定して要素を取得できる
print(numpy_csv_ary[0])  # 1行目の要素を取得 [20. 52. 76.]
print(numpy_csv_ary[2][1])  # 3行目の2列目の要素を取得 60.0

# ある行や列をまとめて取得する場合は、[:]（スライス）または...（エリプシル）を用いる
# - 特定行を丸ごと取得
# `配列[行のインデックス]`
print(numpy_csv_ary[5])
# 6行目の要素を取得 [ 86.  62.  78.]

# - 特定列を丸ごと取得
# `配列[:, 列のインデックス]`
print(numpy_csv_ary[:, 2][:5])
# [ 76. 100.  59. 100.  42.]

# `配列[..., 列のインデックス]`
print(list(map(int, numpy_csv_ary[..., 2]))[:5])
# [76, 100, 59, 100, 42]

# 範囲を指定して要素を取得
# `配列[開始行インデックス:終了行インデックス, 開始列インデックス:終了列インデックス]`
print(numpy_csv_ary[2:5, 1:2])
# [[60.0][66.0][96.0]]

# 2列目が95以上の値を持つ行を取得
print(numpy_csv_ary[numpy_csv_ary[:, 2] > 95])
# 上記のような真偽値がTrueの値のみ抽出する記述を「ブール配列インデックス」と呼ぶ
# 例えば、上記を以下のように記述すると真偽値が返ってくる
print(numpy_csv_ary[:, 2] > 95)

"""
「ブール配列インデックス」では、＆（アンパサド）、|（パイプライン、バーティカルバー）、~（チルダ）などを用いることで、複数の条件を組み合わせることができる
- `&`（アンパサド）: AND条件
- `|`（パイプライン、バーティカルバー）: OR条件
- `~`（チルダ）: NOT条件
- `^`（キャレット）: XOR条件（片方だけTrue）
- `==`（イコール）: 等しい

これら（複数）条件に適用する処理を行いたい場合は以下のように`all`または`any`関数を用いる方法もある

- `all`: 全ての条件がTrueの場合にTrueを返す
```
numpy.all(配列, 軸番号)
```

- `any`: いずれかの条件がTrueの場合にTrueを返す
```
numpy.any(配列, 軸番号)
```

※軸番号は`axis`キーワード引数を用いることでも指定可能

- 多次元配列の場合
最も外側の角括弧が0次元目、次の角括弧が1次元目、...と数えていく。
例えば、二次元配列の場合は軸番号に0を指定すると「全ての行」について、1を指定すると「全ての列」について、要素の真偽値を合成する
"""