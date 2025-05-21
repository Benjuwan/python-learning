# チャプター14 Webスクレイピング

from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup

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

# web上のファイルを取得する`get`関数
# 返り値はレスポンス（webサーバーからの応答）オブジェクト
r = requests.get("http://www.kokusaig.co.jp/")

# 推奨：requestsが自動判別したエンコーディングを使用
r.encoding = r.apparent_encoding

# web上のファイルから中身を取得するための text 属性
# print(r.text)

# （取得したweb上のファイルの中身を）ローカルファイルに保存
with open("../anothers/dl-local-site.html", "wb") as local_site_file_:
    # content 属性：ファイルの中身をバイト文字列として取得する
    local_site_file_.write(
        r.content
    )  # ファイルの中身（バイト文字列）をローカルファイルに保存（上書き）


print("-" * 90)


"""
webページから目的の情報を取得する方法
1. 標準ライブラリ`re`モジュールを使った「正規表現」を用いる方法
2. 非標準ライブラリ`beautifulsoup4`を使った「DOM要素」を用いる方法

2. のほうがシンプルで使いやすそうなので以下からは beautifulsoup4 を用いた方法で記述
"""

try:
    res = requests.get("https://www.python.org/downloads/")
    res.encoding = res.apparent_encoding
    res.raise_for_status()  # HTTPエラーを検出
except requests.RequestException as e:
    print(f"エラーが発生しました: {e}")
    exit("RequestException done.")

# （処理最後に）出力確認するためのリストを用意
release = []

# BeautifulSoup で、取得したwebページの各コンテンツをHTML解析
soup = BeautifulSoup(res.text, "html.parser")

# webページ内の全ての li タグを取得（存在しなければ None）
for li in soup.find_all("li"):
    # 各 li タグの中にある span.release-number 要素を取得（存在しなければ None）
    release_num = li.find("span", class_="release-number")
    if release_num is None:
        continue

    # 各 li タグの中にある span.release-number の中にある a 要素を取得（存在しなければ None）
    version_link = release_num.find("a")
    if version_link is None:
        continue

    # 各 li タグの中にある span.release-date 要素を取得（存在しなければ None）
    release_date = li.find("span", class_="release-date")
    if release_date is None:
        continue

    # タプル形式で「a タグと span.release-date の文字列」を release に格納
    release.append((version_link.text, release_date.text))


def sort_ver(ver_name):
    # ver 番号
    ver_str = ver_name[0].split(" ")[1]
    # return int(ver_str)

    # ドット区切りで分割して数値のタプルに変換 ("3.12.1" -> (3, 12, 1))
    # タプル内の各値ごとに比較していく
    # (3, 9, 0) と (3, 10, 0) の比較: 3と3を比較 -> 同じなので次へ -> 9と10を比較 -> 9 < 10 なのでTrue -> これ以上の比較は不要
    return tuple(map(int, ver_str.split(".")))


# a タグと span.release-date の文字列をソート
# release.sort(key=sort_ver)
release.sort()
for name, data in release:
    # name は15桁（文字）スペースを取った形で表示
    # print(f"{name:15}{data}")
    pass

print("-" * 90)

k2hd_boards = []
with urlopen("http://www.kokusaig.co.jp/") as k2site:
    for content in k2site:
        k2site_soup = BeautifulSoup(str(content, encoding="utf-8"), "html.parser")
        # print(k2site_soup)

        lists = k2site_soup.find_all("li")
        for li in lists:
            if li is None:
                continue

            if len(li.text) > 0 and li.text.count("役") > 0:
                # print(li)
                k2hd_boards.append(li.text)

        target_blank_anchor = k2site_soup.find_all("a", target="_blank")
        if target_blank_anchor is None:
            continue

        for anchor in target_blank_anchor:
            if len(anchor.text) > 1:
                print(anchor.text)

        div_elm = k2site_soup.find("div", class_="HoverEffect")
        if div_elm is None:
            continue

        # print(div_elm)

print(k2hd_boards)
# print(sorted(k2hd_boards))
