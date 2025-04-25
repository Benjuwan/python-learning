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
