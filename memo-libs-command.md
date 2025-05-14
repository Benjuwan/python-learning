## ライブラリ
Pythonのライブラリは`モジュール`と`パッケージ`の構成になっている。
- モジュール：特定機能を持ったプログラムの構成部品（`.pyファイル`）
  - `React`でいう**単一責務や関心の分離**にあたるか
- パッケージ：複数のモジュールをひとまとめにしたもの（モジュールの詰め合わせ）
  - [`Atomicデザイン`](https://zenn.dev/bizlink/articles/b5c8985af8407a)でいう **`Organisms`（`Atoms`と`Molecules`で構成）** など下層パーツの組み合わせ例にあたるか

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

### いくつかの非標準ライブラリ

> [!NOTE]
> `npm`と同じ要領でライブラリをインストールして使用するが、`Python`では`pip`/`pip3`（WindowsOs / MacOS | Linux）がその役割を果たす。<br>
> 後述する[仮想環境](#仮想環境の構築)を用いた管理を行うのがベター。

- `NumPy`（ナムパイ）<br>
**数値計算**でよく使われるライブラリ。主要な機能は、数値を格納するための配列と、配列に対する各種の演算。この配列はベクトルや行列として使用したり、CSVファイルから読み込んだ数値を格納したり、各種の統計量を求めたりもできる。他のライブラリ（`Pandas`や`Matplotlib`など）でも使用されている。
- 実装例や解説などは[検証ファイル](lib-test-venv/lib-numpy.py)を参照してください 

- `Pandas`（パンダス）<br>
**データ処理**でよく使われるライブラリ。データの読込、指定したデータの取得、統計量の計算などを簡単なプログラムで実現できる。<br>`Pandas`にはデータフレームという独自のオブジェクトがあるので、分かりやすくデータを表示したり、扱ったりしたい場合は`NumPy`より`Pandas`のほうが良い。
- 実装例や解説などは[検証ファイル](lib-test-venv/lib-pandas.py)を参照してください 

- `Matplotlib`（マットプロットリブ）<br>
**インフォグラフィック（可視化）**ライブラリ。`NumPy`の配列や`Pandas`のデータフレームなどから色々な種類の図を作成できる。データの分析やクラスタリング（入力データをいくつかのクラスターに分類すること）などのAIの手法を適用する際に相乗効果を発揮する可視化処理を行ってくれる。人間はインフォグラフィックを用いることで、より適切な仮説出しができたり、施策の効果検証を行ったりできる。  
  - `scikit-learn`（サイキットラーン）<br>
  機械学習ライブラリ。データに対して、分類、回帰、クラスタリング（入力データをいくつかのクラスターに分類すること）、次元削減といった機械学習に関する色々な手法を適用することができる。

- `Pillow`（ピロー）<br>
画像ファイルの入出力や編集でよく使われるライブラリ。例えば、矩形（くけい）や円といった図形をはじめ、画像の色数やサイズの変更も行える。<br>
※ライブラリ名は`Pillow`だがインストール後のパッケージ名は`PIL`となる。
- 実装例や解説などは[検証ファイル](lib-test-venv/lib-test.py)を参照してください 

- `pypdf`<br>
PDFファイルを扱う時に利用するライブラリ。
  - 参考記事：[【Python×PDF】PyPDF2はもう古い！PythonでPDFを扱うときにはpypdfを使おう](https://qiita.com/ryutarom128/items/6e5d36efb136f9595f07)

- `openpyxl`（オープンパイエックスエル）<br>
Excelファイルを扱う時に利用するライブラリの一つ。
- 実装例や解説などは[検証ファイル](lib-test-venv/handle-exfile.py)を参照してください 

#### 仮想環境の構築
仮想環境を用いることで、いろいろなバージョンの`Python`（プロジェクト）を同じPCの中で混在させて、プロジェクトによって使い分けられる。<br>つまり、各プロジェクトごとの設定やバージョンを個別に固定管理できるようになる。

##### コマンド操作
`python -m pip`または`pip`（macOS/Linuxの場合は`python3 -m pip`または`pip3`）で実行

- 仮想環境（`venv`）の構築例<br>
※`GitHub`でプロジェクト管理していて不要なファイルなどは省かれている状態を前提とする
```bash
mkdir my-venv-env # my-venv-env ディレクトリ（仮想環境フォルダ）を作成
cd my-venv-env    # 作成した仮想環境フォルダへ移動

# 新しい仮想環境を作成してアクティベート
python -m venv env        # env{は仮想環境名}
source env/bin/activate   # WindowsOS の場合: 仮想環境名\Scripts\activate

# ※「既存の仮想環境をアクティベートする場合」は、当該仮想環境ディレクトリの「一つ前の階層」でアクティベートコマンドを実行しないと起動できない
source env/bin/activate   # WindowsOS の場合: 仮想環境名\Scripts\activate

# アクティベートした状態で希望するライブラリをインストール
python -m pip install ライブラリ

# 依存関係を`requirements.txt`に保存
# ※ 既存の仮想環境ディレクトリ（及び requirements.txt ）がある場合は、アクティベート状態でコマンド移動（cd dir）してから下記コマンドで requirements.txt に上書き保存する 
python -m pip freeze > requirements.txt

# 仮想環境から抜ける
deactivate

# 別の環境に反映する時
# 1. 当該仮想環境フォルダに移動（`cd my-venv-env`）
# 2. 新しい仮想環境を作成
python -m venv env
# 3. 仮想環境をアクティベート
source env/bin/activate   # WindowsOS の場合: env\Scripts\activate

# 4. アクティベートした状態で requirements.txt に定義されたパッケージをインストール
# ※ 既存の仮想環境ディレクトリ（及び requirements.txt ）がある場合は、アクティベート状態でコマンド移動（cd dir）してから下記コマンドにて各種ライブラリをインストールする
python -m pip install -r requirements.txt
```

##### `venv`
仮想環境を作成する`Python`のデファクトスタンダードな標準ライブラリ。
- 参考記事：[Python仮想環境ツール多すぎ！ 一番ベーシックな「venv」から再入門しよう](https://qiita.com/minorun365/items/94bdb12eb42581850315)

> [!NOTE]
> 記事内における「仮想環境の`activate`」の部分について補足
> - 仮想環境を`activate`するには以下のコマンドを入力する
>   - Windowsの場合：   `.\仮想環境名\Scripts\activate`
>   - Mac/Linuxの場合： `source ./仮想環境名/bin/activate`<br>
> パスの先頭に(仮想環境名)が表示されていれば成功

※注意事項として`venv`は、プロジェクトが以下のような複雑さを持つ場合に課題が生じるので、このような場合は`Pipenv`や`Poetry`などの高度なツールがより適切となる。
- 大規模プロジェクト
- 複雑な依存関係を持つ場合
- 開発環境と本番環境で異なる設定が必要な場合
- 厳密なバージョン管理が必要な場合

###### `venv`で構築した仮想環境が`deactivate`しても、ターミナルを立ち上げる度に起動されている場合の対処法
1. VSCodeの左下設定（歯車アイコンを押下）の`設定`項目を開く
2. 設定の検索で`Python > Terminal: Activate Environment`を入力
3. `ユーザー`欄の当該項目のチェックを外す

##### `uv`
`venv`の仮想環境構築に加えて、パッケージ管理までも実現できる（2025年時点では比較的新しい）サードパーティライブラリ。パッケージ管理 + 仮想環境という機能を持ち合わせていながらも、`Rust`製による非常に高速なパフォーマンスを備えている。`venv`と`pip`の機能を統合し、より効率的なワークフローを提供しているのも特徴。
- 参考記事：[Pythonの開発用適当ツールの作成・実行はuvを使うのがオススメ](https://qiita.com/ssc-ksaitou/items/9da75058489ebe8c2009)

> uvはPythonパッケージだけでなくPythonのバージョン自体も管理することが可能なため、プロジェクトごとに異なるPythonバージョンや依存関係を管理するのに適したツールだと言える。...中略
> Anacondaは一定以上の規模の企業で利用する場合に、ライセンス料がかかってしまう点には注意したい。...中略
> uvはまだ歴史が浅く発展途上であるため、破壊的な変更が加えられる可能性も高い。開発期間が長いpyenvやpoetryなどのツールの方が安定した利用が見込め、そういった観点ではこちらの選択肢もまだあり得るだろう。

- 参照記事：[uv （pythonパッケージマネージャー）の使い方 簡易版](https://zenn.dev/tabayashi/articles/197205349d6935)
- 参照記事：[uv （pythonパッケージマネージャー）の使い方 詳細版](https://zenn.dev/tabayashi/articles/52389e0d6c353a)
- 参考記事：[Python Coding Best Practices for Researchers](https://cyberagentailab.github.io/BestPracticesForPythonCoding/#management-tools)
- 参考記事：[AIエージェントにも正しく使ってほしいPython環境管理ツール「uv」最新情報ガイド](https://qiita.com/ootakazuhiko/items/4fa2406534777d86f333)

#### ライブラリの扱いに関するコマンドたち
- インストール<br>
```bash
pip install ライブラリ名
# または python -m pip install ライブラリ名
```

- アンインストール<br>
```bash
pip uninstall -y ライブラリ名
# または python -m pip uninstall -y ライブラリ名
```

- アップグレード<br>
```bash
pip install --upgrade（または-U） ライブラリ名
# または python -m pip install --upgrade（または-U） ライブラリ名
```

- `pip`のアップグレード<br>
```bash
python -m pip install --upgrade pip
```

- ライブラリの情報を確認<br>
```bash
pip show ライブラリ名
# または python -m pip show ライブラリ名
```

- ライブラリの一覧を確認<br>
```bash
pip list
# または python -m pip list
```

## コマンドライン引数
コマンドプロンプトやターミナルでコマンド入力する際に**コマンドに対して与える引数**のこと。<br>
これにより、**コマンドラインから特定処理の実行（計算やファイル編集、操作など）が可能**となる。

```bash
コマンド 引数
```

### `Python`ファイルに対するコマンドライン引数の実行
```bash
python hoge.py 引数
```

コマンドライン引数を受け取るには、標準ライブラリ`sys`（シス）モジュールを使用する。`sys`モジュールの`argv`（アーグブイ）属性がプログラム名とコマンドライン引数のリストとなる。
```py
import sys

# プログラム名と引数のリストを取得
# 取得したリスト[0]にはプログラム名が入り、以降のインデックスには引数が続く
sys.argv # 属性なので()は無し

# 指定した位置（インデックス）の値を取得
sys.argv[0] # プログラム名
sys.argv[1] # 第一引数
sys.argv[2] # 第二引数

# プログラム名と引数の個数を取得
len(sys.argv)
```

#### 具体例
```py
# python chapter11.py 1 2 3
print(sys.argv)
# 結果：['chapter11.py', '1', '2', '3']

print(len(sys.argv))    # 4
print(sys.argv[0])      # chapter11.py
print(sys.argv[-1])     # 3
```