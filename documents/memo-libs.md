## ライブラリ
Pythonのライブラリは`モジュール`と`パッケージ`の構成になっている。
- モジュール：特定機能を持ったプログラムの構成部品（`.pyファイル`）
  - `React`でいう**単一責務や関心の分離**にあたるか
```py
# `-m`： 指定したモジュールを起動するためのオプション（コマンド）
python -m モジュール
```

- パッケージ：複数のモジュールをひとまとめにしたもの（モジュールの詰め合わせ）
  - [`Atomicデザイン`](https://zenn.dev/bizlink/articles/b5c8985af8407a)でいう **`Organisms`（`Atoms`と`Molecules`で構成）** など下層パーツの組み合わせ例にあたるか

### モジュール化（自分でライブラリを用意・作成する場合）
モジュール化は必須ではないものの、行うことで関数（特定処理）の再利用化が捗るし、保守・管理もしやすくなる。

#### 単独実行または他プログラムからも利用可能なモジュールの作り方
1. はじめに、モジュールの主要な処理を関数にまとめる
2. モジュールを単独で（Pythonコマンドで）実行したときに関数を呼び出す処理を追加

```py
# 1. はじめに、モジュールの主要な処理を関数にまとめる
def 関数名(引数, ...):
  # 処理の記述...

# 2. モジュールを単独で（Pythonコマンドで）実行したときに関数を呼び出す処理を追加
if __name__ == "__main__":
  関数名(引数, ...)
```

- `__name__`<br>
モジュール名を返す特別な変数。
  - モジュールを単独実行したとき
  モジュール名は、`"__main__"`
  - 他プログラムから利用（呼び出）したとき
  モジュール名は、`（当該モジュール）ファイル名`（※`.py`拡張子除く）

```py
if __name__ == "__main__":
```
モジュール作成において、上記記述が必要な理由は**`__name__`が`"__main__"`に等しいかどうかチェックし、等しい場合はモジュールの主要な処理を行う関数を呼び出せるようにするため**であり、これにより単独でも他プログラムからでも使用できるようになる。

---

パッケージは、`パッケージ/サブパッケージ/サブサブパッケージ/モジュール`というような階層構造になっており、`.`記法で選択していく
- モジュール名の書き方（パッケージなし）
```py
モジュール名
```
- モジュール名の書き方（パッケージあり）
```py
パッケージ.モジュール名
```
- モジュール名の書き方（サブパッケージあり）
```py
パッケージ.サブパッケージ.….モジュール名
```

### ライブラリの使用方法
他の言語やフレームワークなどと同じように使用したい機能をインポートする。
```py
import モジュール名
```

- 具体例<br>
標準ライブラリ`random`モジュールをインポート

> [!NOTE]
> `Python`の`random`モジュールは疑似乱数（疑似的なランダム数値）を生成する機能を持っているが、`JavaScript`の`Math.random()`同様、**疑似乱数は暗号に使用可能な安全性を備えていない**のでセキュリティ事案には使用してはいけない。

```py
import random
print(random.randint(1, 6)) # 1から6までの乱数を生成
```

インポートしたモジュール名は上記のように`モジュール名.{変数 | メソッド(arg,...) | クラス(arg,...)}名`というように使用する

- 他の呼び出し方
```py
# モジュール名に別名を付けて使用する
import モジュール名 as 別名
# import random as r
# r.randint(1, 6)

# モジュール名を省いて（希望する機能を）使用する（呼び出す）
from モジュール名 import 機能名,...
# from random import randint
# randint(1, 6)

# 全ての機能をモジュール名を省いて使用する（呼び出す）
from モジュール名 import *

# インポートした機能に別名を付けて使用する
from モジュール名 import 機能名 as 別名
# from random import randint as ri
# ri(1, 6)
```

#### モジュールがパッケージ名を伴う場合
- パッケージ名を省いてモジュールを使用
```py
from パッケージ名 import モジュール名
```

- パッケージ名とモジュール名を省いて機能を使用
```py
from パッケージ名.モジュール名 import 機能名
```

##### 実用例
- URL文字列を解析して各種の要素を抽出する`urllib`ライブラリを使用
```py
# パッケージとモジュールをそれぞれインポート
import urllib
import urllib.parse

url_parse_result = urllib.parse.urlparse("https://github.com/Benjuwan/python-learning")
print(url_parse_result)
# ParseResult(scheme='https', netloc='github.com', path='/Benjuwan/python-learning', params='', query='', fragment='')

# パッケージを省略してモジュールをインポート
from urllib import parse

url_parse_result = parse.urlparse("https://github.com/Benjuwan/python-learning")
print(url_parse_result)

# パッケージとモジュールを省略して機能をインポート
from urllib.parse import urlparse

url_parse_result = urlparse("https://github.com/Benjuwan/python-learning")
print(url_parse_result)
```

### いくつかの標準ライブラリ
#### `random`
- `random`関数<br>
0.0以上 1.0未満のランダムな浮動小数点数を返す
```py
import random
print(random.random())
```

> [!NOTE]
> `Python`の`random`モジュールは疑似乱数（疑似的なランダム数値）を生成する機能を持っているが、`JavaScript`の`Math.random()`同様、**疑似乱数は暗号に使用可能な安全性を備えていない**のでセキュリティ事案には使用してはいけない。

- `randint`関数<br>
開始値（第一引数）から終了値（第二引数）までの乱数（整数値）を生成
```py
import random
print(random.randint(1, 6))
```

- `choice`関数<br>
第一引数に渡したシーケンス内の要素をランダムで取得（抽出）
```py
import random
target_list = ["Morning", "Afternoon", "Evening", "Night"]
print(random.choice(target_list))
```

- `shuffle`関数<br>
第一引数に渡したシーケンス内の要素順序を（ランダム）シャッフルする
```py
import random
target_list = ["Morning", "Afternoon", "Evening", "Night"]
random.shuffle(target_list)
print(target_list)
```

#### `time`
時刻の取得や変換を行うモジュール。<br>現在時刻（エポックからの経過秒数）を浮動小数点数で返す。<br>※エポック（UNIXエポック）とは大抵のシステムにおいて「1970年 1月 1日 0時 0分 0秒」を指す。

- `time`関数<br>
現在時刻（エポックからの経過秒数）を返す
```py
import time
print(time.time())
```

- `gmtime`関数<br>
UTCにおける現在時刻を取得できる
```py
import time
print(time.gmtime())
```

- `localtime`関数<br>
使用している環境（地域）の設定に基づいた現在時刻を取得できる
```py
import time
local_time = time.localtime()
print(local_time)
print(f"{local_time.tm_year}年{local_time.tm_mon}月{local_time.tm_mday}日 {local_time.tm_hour}時{local_time.tm_min}分{local_time.tm_sec}秒")
```

- `sleep`関数<br>
指定した秒数だけプログラム実行を停止する
```py
# 3秒後にこれ以降に続く処理を実行
time.sleep(3)
```

#### [`urllib`](https://docs.python.org/ja/3.13/library/urllib.html)（ユーアールエル・リブ）<br>
webページを取得できる標準ライブラリ。

```py
from urllib.request import urlopen

with urlopen("https://example.co.jp/") as sitedate:
    for content in sitedate:
        # print(content) # このままではバイト列で表示される

        # str でバイト列を utf-8 文字列に変換
        print(str(content, encoding="utf-8"), end="")
```

#### `sqlite3`
データベースをわざわざ用意する必要なく、RDBMS（リレーショナルデータベース・マネジメント・システム）の一種である`SQLite`を利用できる標準ライブラリ。<br>※処理を実行する上では`SQL`文の知識が必要。

- `connect()`関数<br>
データベースに接続し、接続を意味する`connection`オブジェクトを返す
```py
connection = sqlite3.connect("データベース名.db")
```

- `cursor()`メソッド<br>
`connection`オブジェクトを通じて、データベース操作関連の機能を提供するカーソルオブジェクト（イテラブル）を取得する。
```py
cursor_obj = connection.cursor()
```

- `execute()`メソッド<br>
RDBMS（本事例では`SQLite`）に対して`SQL`文を適用（発行・実行）する。<br>`SQL`文の中でシングルクォートを使う場合があるので、引数に指定する文字列はダブルクォートで記述するのが無難。
```py
cursor.execute("SQL文")
```

- `executemany`メソッド<br>
イテラブルに対して`SQL`文を繰り返し適用（発行・実行）する。
```py
cursor_obj.executemany("SQL文", イテラブル)
```

> [!NOTE]
> - SQL文の`?`<br>
> `execute()`や`executemany`メソッドにおいて、`SQL`文の中に`?`を書いておくと、その位置に値を埋め込むことができる。
> ```py
> # テーブルに行（値?, 値?）を追加
> cursor_obj.executemany("INSERT INTO テーブル VALUES (?, ?)", イテラブル)
> ```

- `commit()`メソッド<br>
（データベースを変更する`SQL`文を実行した際などに）`connection`オブジェクトを通じて、データベースへの変更確定（操作・処理）を行う。
```py
connection.commit()
```

- `close()`メソッド<br>
（`connection`オブジェクトを通じて）データベースへの接続を閉じる（終了する）ためのメソッド。
```py
connection.close()
```

#### `http.server`
Webサーバ（HTTPサーバ）の機能を提供する標準ライブラリ。しかし**セキュリティ的な懸念があるので利用時はあくまで開発用として扱う**こと。<br>本格的な開発には`Django`,`Flask`などフレームワークを用いるべき。これらのフレームワークは、セキュリティや拡張性、運用性に優れた機能を備えている。

#### `CGI`モジュール
- `CGI`（Common Gateway Interface）<br>
Webサーバ上でプログラムを動かすための仕組み。例えば、`CGI`を使うとWebブラウザからのリクエストに基づいてWebサーバ上でプログラムを実行し、プログラムの出力（処理結果）をWebブラウザに返すことができる。<br>事例ケースとしては、ユーザーが入力したフォーム内容をプログラムで受け取って処理するなど。

```py
#!/usr/bin/env python3
import cgi
```

上記「`#!/usr/bin/インタプリンタ`」の部分は「シバン（シェバン）」と言って MacOS / Linux で`CGI`プログラムを実行するためのインタプリンタ（*）を指定するための機能。<br>
*：コンパイラ方式（プログラムのソースコードを一度にすべて機械語に変換して実行する）ではなく、1行ずつ順番に読み取り、その都度実行していく仕組みを持つプログラム実行方式

### いくつかの非標準ライブラリ

> [!NOTE]
> `npm`と同じ要領でライブラリをインストールして使用するが、`Python`では`pip`/`pip3`（WindowsOs / MacOS | Linux）がその役割を果たす。<br>
> 後述する[仮想環境](#仮想環境の構築)を用いた管理を行うのがベター。

#### `NumPy`（ナムパイ）
**数値計算**でよく使われるライブラリ。主要な機能は、数値を格納するための配列と、配列に対する各種の演算。この配列はベクトルや行列として使用したり、CSVファイルから読み込んだ数値を格納したり、各種の統計量を求めたりもできる。他のライブラリ（`Pandas`や`Matplotlib`など）でも使用されている。
- 実装例や解説などは[検証ファイル](lib-test-venv/lib-numpy.py)を参照してください 

#### `Pandas`（パンダス）
**データ処理**でよく使われるライブラリ。データの読込、指定したデータの取得、統計量の計算などを簡単なプログラムで実現できる。<br>`Pandas`にはデータフレームという独自のオブジェクトがあるので、分かりやすくデータを表示したり、扱ったりしたい場合は`NumPy`より`Pandas`のほうが良い。
- 実装例や解説などは[検証ファイル](lib-test-venv/lib-pandas.py)を参照してください 

#### `Matplotlib`（マットプロットリブ）
**インフォグラフィック（可視化）** ライブラリ。`NumPy`の配列や`Pandas`のデータフレームなどから色々な種類の図を作成できる。データの分析やクラスタリング（入力データをいくつかのクラスターに分類すること）などのAIの手法を適用する際に相乗効果を発揮する可視化処理を行ってくれる。人間はインフォグラフィックを用いることで、より適切な仮説出しができたり、施策の効果検証を行ったりできる。  


#### `scikit-learn`（サイキットラーン）
機械学習ライブラリ。データに対して、分類、回帰、クラスタリング（入力データをいくつかのクラスターに分類すること）、次元削減といった機械学習に関する色々な手法を適用することができる。

#### `Pillow`（ピロー）
画像ファイルの入出力や編集でよく使われるライブラリ。例えば、矩形（くけい）や円といった図形をはじめ、画像の色数やサイズの変更も行える。<br>
※ライブラリ名は`Pillow`だがインストール後のパッケージ名は`PIL`となる。
- 実装例や解説などは[検証ファイル](lib-test-venv/lib-test.py)を参照してください 

#### `pypdf`
PDFファイルを扱う時に利用するライブラリ。
  - 参考記事：[【Python×PDF】PyPDF2はもう古い！PythonでPDFを扱うときにはpypdfを使おう](https://qiita.com/ryutarom128/items/6e5d36efb136f9595f07)

#### `openpyxl`（オープンパイエックスエル）
Excelファイルを扱う時に利用するライブラリの一つ。
- 実装例や解説などは[検証ファイル](lib-test-venv/handle-exfile.py)を参照してください 

#### `Requests`（リクエスツ）
webスクレイピング（webアクセス）用のライブラリ。標準ライブラリ`urllib`よりも簡潔なプログラミングで手軽にWebを扱える。

> [!NOTE]
> - webスクレイピングについて<br>
> webスクレイピングは、受けるサイトの負荷が大きく（程度によっては）犯罪にもなり得る危険な行為なので、第三者のサイトや自身と関係のサイトへ行うのは控えるべき。

#### [`BeautifulSoup`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)（ビューティフルスープ）
HTMLファイル構造を解析して必要なデータを抽出するためのライブラリ。要素の階層構造に基づいた処理が可能なので文字列のパターンマッチ（正規表現）よりも確実かつ容易にデータを取り出せる（可能性がある）
```py
スープ = BeautifulSoup(HTMLの文字列, 'html.parser')
```

<details>
<summary>Requests と BeautifulSoup を使った事例</summary>

```py
res = requests.get("取得したいサイトURL文字列")
res.encoding = res.apparent_encoding # エンコーディング処理

# BeautifulSoup で、取得したwebページの各コンテンツ（res.text）をHTML解析
soup = BeautifulSoup(res.text, "html.parser")
```

- 実装例
```py
# find メソッド： 該当する最初の要素を返す（存在しなければ None）
スープ.find(要素名)
# スープ.find("a")

スープ.find(要素名, 属性名=値, ...) # 属性名はオプショナル
# class 属性を指定する場合は Python の class と競合するため class_ と記述（指定）する
# スープ.find("span", class_="release-number")

# find_all メソッド： 該当する全ての要素を返す（存在しなければ None）
# 返り値はイテラブルなのでループ処理可能
スープ.find_all(要素名)
# スープ.find_all("li")

スープ.find_all(要素名, 属性名=値, ...) # 属性名はオプショナル
```

上記`html.parser`とは、Python標準のHTML用パーサー（構文解析器）のことで、サードパーティ制のHTMLパーサーを利用（指定）することも可能。使用するパーサーによって、HTMLの記述に対する柔軟性や処理の速度が異なる。

</details>

#### `schedule`
あらかじめ設定したスケジュールに基づいて、指定した処理（関数）を定期的に実行する非標準ライブラリ

<details>
<summary>schedule 実装例一覧表</summary>

`hours`や`minutes`といった複数形の部分は`hour`,`minute`など単数形でもok

- 基本的な間隔設定
  - `.seconds`: `schedule.every(10).seconds.do(関数)` ……… 10秒ごとに実行
  - `.minutes`: `schedule.every(30).minutes.do(関数)` ……… 30分ごとに実行
  - `.hours`: `schedule.every(2).hours.do(関数)` ……… 2時間ごとに実行
  - `.days`: `schedule.every(3).days.do(関数)` ……… 3日ごとに実行
  - `.weeks`: `schedule.every(2).weeks.do(関数)` ……… 2週間ごとに実行

- 特定時刻の設定
  - `.at()`: `schedule.every().day.at("10:30").do(関数)` ……… 毎日10:30に実行
  - `.hour.at()`: `schedule.every().hour.at(":00").do(関数)` ……… 毎時00分に実行

- 曜日指定
  - `.monday`: `schedule.every().monday.do(関数)` ……… 毎週月曜に実行
  - `.tuesday`: `schedule.every().tuesday.do(関数)` ……… 毎週火曜に実行
  - `.wednesday`: `schedule.every().wednesday.at("13:15").do(関数)` ……… 毎週水曜13:15に実行
  - `.thursday`: `schedule.every().thursday.do(関数)` ……… 毎週木曜に実行
  - `.friday`: `schedule.every().friday.do(関数)` ……… 毎週金曜に実行
  - `.saturday`: `schedule.every().saturday.do(関数)` ……… 毎週土曜に実行
  - `.sunday`: `schedule.every().sunday.do(関数)` ……… 毎週日曜に実行

- タグ付け管理
  - `.tag()`: `schedule.every().day.do(関数).tag('daily')` ……… タグ付けしてジョブを管理
  - `.clear()`: `schedule.clear('daily')` ……… 特定タグのジョブをキャンセル

- 引数付き関数
  - `.do()`: `schedule.every().day.do(greet, name="Alice")` ……… 関数に引数を渡して実行

- 条件付き実行
  - `CancelJob`: `return schedule.CancelJob` ……… 条件に応じて実行を停止

</details>

- `run_pending`関数<br>
所定のタイミングになったスケジュール（に登録した）関数を実行する
```py
# 1行ごとにスケジュールを（延々と）実行
while True:               # 無限ループ
  schedule.run_pending()  # スケジュール（指定した定期的な処理）を実行
  time.sleep(1)           # 1秒後に処理実行
```
