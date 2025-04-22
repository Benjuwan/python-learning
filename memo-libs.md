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

- `time`関数
現在時刻（エポックからの経過秒数）を返す
```py
import time
print(time.time())
```

- `gmtime`関数
UTCにおける現在時刻を取得できる
```py
import time
print(time.gmtime())
```

- `localtime`関数
使用している環境（地域）の設定に基づいた現在時刻を取得できる
```py
import time
local_time = time.localtime()
print(local_time)
print(f"{local_time.tm_year}年{local_time.tm_mon}月{local_time.tm_mday}日 {local_time.tm_hour}時{local_time.tm_min}分{local_time.tm_sec}秒")
```

---


`npm`と同じでインストールして使用するが、Pythonでは`pip`（※`uv`の場合は`uv`コマンドで諸々を実行する）がその役割を果たす。