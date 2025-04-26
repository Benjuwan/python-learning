## テキストファイルの入出力
```py
with open("ファイル名", "w", encoding="文字エンコーディング") as 変数:
  文…
```

- 具体例
```py
# anothers フォルダに message.txt が無い場合は新規作成され、既にある場合は上書き保存される
with open("../anothers/message.txt", "w", encoding="utf-8") as message_txt_file:
    message_txt_file.write("Hello\n")
    message_txt_file.write("Python\n")
    message_txt_file.write("World\n")
```

### `open`関数
ファイルを開く組み込み関数で、ファイルオブジェクト（ファイルを表すオブジェクト）を返す。上記例の場合`as`後の変数に当該ファイルオブジェクトが格納される。
- 第一引数：<br>操作対象となるファイル名
  - ディレクトリ名を含むパス指定も可能
- 第二引数：<br>ファイルに対する具体的な操作指示。記述省略すると`r`判定となる。
  - `r`：読み込み（デフォルト）
  - `w`：書き込み
    - ※指定したファイルが存在しない場合は新規作成され、既にある場合は上書き保存される
  - `a`：追加書き込み
- 第三引数：<br>ファイル読み書きの際の文字エンコーディング（例：`utf-8`, `shift-jis`, and so on...）

### `with`文
内側の文を実行し終えると開いたファイルを自動的に閉じてくれる。`with`文を使わずに`open`関数を実行すると、開いたファイルオブジェクトの`close`メソッドを使って手動で閉じなければならなくなる。

### ファイルオブジェクトのメソッド
- `write`
ファイルにテキストを書き込める。末尾で改行しないので改行したい場合は`\n`を記述する。

- `read`
ファイルのテキストを文字列にする。
```py
# `open`関数の第二引数を省略して`r`（読み込み）操作を実施
with open("../anothers/message.txt", encoding="utf-8") as message_txt_file:
    print(message_txt_file.read().replace("\n", " "))
```

### `csv`モジュール
CSVファイルの入出力を実現する標準ライブラリ。

```py
import csv

with open("ファイル名", "w", encoding="文字エンコーディング", newline="") as 変数:
  csv.writer(変数).writerows(イテラブル)
```

> [!NOTE]
> `csv`モジュールを使う場合、引数`newline`を指定しないと**改行が余分に出力されて各行の間に空行が入ってしまう**ので`newline`に空文字列（`""`）を指定する。

- 具体例
```py
import csv

# anothers フォルダに items.csv が無い場合は新規作成され、既にある場合は上書き保存される
for_csv_txt_lists = [("hat", 2000), ("shirt", 1000), ("socks", 500)]
with open("../anothers/items.csv", "w", encoding="utf-8", newline="") as csv_file:
    csv_file_obj = csv.writer(csv_file)
    csv_file_obj.writerows(for_csv_txt_lists)
```

- `writer(ファイルオブジェクト)`<br>
CSVファイルを操作するためのオブジェクトを作成。この`writer`オブジェクトを通じて以下メソッドを用いたCSVファイルの編集作業を行う。

- `writerows(イテラブル)`<br>
`writer`オブジェクトを通じて、CSVファイルに「複数行」をまとめて書き込むメソッド。
引数に指定するイテラブルの要素をCSVファイルの各行として出力する。

- `writerow(イテラブル)`<br>
`writer`オブジェクトを通じて、CSVファイルに「1行」を書き込むメソッド。
引数に指定するイテラブルの要素をCSVファイルの各行として出力する。

- `reader(ファイルオブジェクト)`<br>
`reader`オブジェクトはイテラブルとして働き、対象CSVファイルの各行に含まれる値をリストとして返す。

```py
with open("../anothers/items.csv", encoding="utf-8") as csv_file:
    csv_reader_obj = csv.reader(csv_file)
    for item in csv_reader_obj:
        print(item)
        # ['hat', '2000']
        # ['shirt', '1000']
        # ['socks', '500']

    # 各値をタプル形式でまとめたリストを生成
    items = [tuple(item) for item in csv_reader_obj]
    print(items)
    # [('hat', '2000'), ('shirt', '1000'), ('socks', '500')]

    # lambda 引数: （返却される）式
    print(sorted(items, key=lambda item: int(item[1])))
    # [('socks', '500'), ('shirt', '1000'), ('hat', '2000')]

    print(sorted(items, key=lambda item: int(item[1]), reverse=True))
    # [('hat', '2000'), ('shirt', '1000'), ('socks', '500')]
```

### `json`モジュール
jsonファイルの入出力を実現する標準ライブラリ。

```py
import json

with open("ファイル名", "w", encoding="文字エンコーディング") as 変数:
  json.dump(イテラブル, 変数, indent=整数)
```

- 具体例<br>
```py
# anothers フォルダに items.json が無い場合は新規作成され、既にある場合は上書き保存される
for_json_dict = [
    {"name": "hat", "price": 2000},
    {"name": "shirt", "price": 100},
    {"name": "socks", "price": 500},
]
with open("../anothers/items.json", "w", encoding="utf-8") as json_file:
    json.dump(for_json_dict, json_file, indent=2)
# [
#   {
#     "name": "hat",
#     "price": 2000
#   },
#   {
#     "name": "shirt",
#     "price": 100
#   },
#   {
#     "name": "socks",
#     "price": 500
#   }
# ]
```

- `dump`関数（`write`系処理）<br>
対象ファイルにイテラブルの内容を書き込む関数
  - `indent`キーワード引数<br>
  `indent`に整数を指定するとJSONファイルに改行やインデントが入って可読性が増す。※人が読まない場合は`indent`キーワード引数は特に不要。

- `load`関数（`read`系処理）<br>
対象JSONファイルを読み込む関数
```py
with open("../anothers/items.json", encoding="utf-8") as json_file:
    print(json.load(json_file))
# [{'name': 'hat', 'price': 2000}, {'name': 'shirt', 'price': 100}, {'name': 'socks', 'price': 500}]
```

## ファイルに関する色々な操作
### ファイルの一覧取得
- `glob`（グラブ）モジュール<br>
標準ライブラリ。指定したディレクトリにあるファイルの一覧を取得できる。例えば、特定の拡張子を持つファイルだけを列挙したり、サブディレクトリを含めてファイルを列挙したりできる。

- ファイルの一覧取得
```py
import glob
# 指定したパス（※ファイルやディレクトリの場所を指す文字列）にあるファイルの一覧を取得する。
# 返り値はファイル一覧のリスト形式（イテラブル）となる
glob.glob(パス)

# サブディレクトリも含める場合は以下の記述となる
# キーワード引数`recursive`を`True`にすることでサブディレクトリも処理対象となる
glob.glob(パス, recursive=True)

# * でワイルカード指定となる
# 例えば、以下の記述だと`.txt`拡張子のファイルだけを列挙する
glob.glob(*.txt)
```
