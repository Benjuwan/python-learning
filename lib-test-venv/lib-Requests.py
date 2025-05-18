# チャプター14 Webスクレイピング

from urllib.request import urlopen
import requests

"""
urllib：標準ライブラリ
"""

"""
urllib.request モジュールの urlopen 関数
URLで指定したWeb上のファイル（html）を開き、このファイルを読み込むためのオブジェクトを返す
```py
with urlopen(URL) as 変数名（オブジェクト）:
    # 処理...
```
ファイルを開く open 関数と同様に with 文を使用するのが無難

オブジェクトはイテラブルなのでループ処理が可能
```py
for 変数 in 変数名（オブジェクト）:
    # 処理...
```
"""

with urlopen("http://www.kokusaig.co.jp/") as kokusaihd_site:
    for content in kokusaihd_site:
        # このままではバイト列で表示される
        # print(content)

        # str でバイト列を utf-8 文字列に変換
        # print(str(content, encoding="utf-8"), end="")

        pass

"""
取得したWebページをローカルファイルに保存
（※レイアウト崩れや画像が欠けていたりする）
"""

with urlopen("http://www.kokusaig.co.jp/") as kokusaihd_site:
    # wb（write binary）バイナリファイルの書き込み
    with open("../anothers/dl-local-site.html", "wb") as local_site_file:
        # kokusaihd_site：対象サイト（ページ）の全体 を read で読み込んで
        # local_site_file：ローカルファイルオブジェクト の write メソッドで保存する
        local_site_file.write(kokusaihd_site.read())


print("-" * 90)

"""
Requests：非標準ライブラリ
"""

