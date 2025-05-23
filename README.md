# python-learning
書籍[『Python［完全］入門』](https://www.sbcr.jp/product/4815607647/)の学習用途リポジトリ

- [サンプルファイルのダウンロード](https://www.sbcr.jp/support/4815602893/)
- [『Python［完全］入門』正誤情報](https://www.sbcr.jp/support/4815607384/)

## Python
- [公式ダウンロードページ](https://www.python.org/downloads/)
- [公式チュートリアル](https://docs.python.org/ja/3/tutorial/)

### 必須及び便利な VSCode 拡張機能
- `Python`（必須）
  - `Python`をインストールしたら付随されてきた拡張機能たち<br>
  `Pylance`, `Python Debugger`

- `Ruff`<br>
`Rust`制の動作が高速な`Linter`+`Formatter`機能。<br>プロジェクトにおける詳細な設定は[【令和6年最新版】初心者でも、チーム開発でも美しく！Python開発環境構築のすすめ](https://qiita.com/musutafakemaru/items/332bd0193828aa66461d#ruff%E3%82%AA%E3%82%B9%E3%82%B9%E3%83%A1%E3%81%AE%E5%88%9D%E6%9C%9F%E8%A8%AD%E5%AE%9A)を参照。

- `Mypy Type Checker`（`mypy`）<br>
動的型付け言語の`Python`に型を付けてくれる。

## 参照
- [【令和6年最新版】初心者でも、チーム開発でも美しく！Python開発環境構築のすすめ](https://qiita.com/musutafakemaru/items/332bd0193828aa66461d)

---

## プロジェクトごとに仮想環境を設けるべき
ライブラリなど**各種プログラムのバージョンの違いや競合による動作不良を防ぐには仮想環境の利用が大切**となる。<br>
[仮想環境構築の詳細はこちら](/memo-libs-command.md#仮想環境の構築)に記載している。

## ライブラリやフレームワーク関連
- [Django実践開発入門](https://qiita.com/Syoitu/items/d3a28b2a7acdf90fbccd)<br>
`Django`（ジャンゴ）で簡易的なスクール学生管理システムをハンズオンしていく内容。ファイル構成案や各種情報、Tipsなど色々と参考になる。

- [DjangoとuWSGI、Nginxの関係を理解したい](https://qiita.com/yuzu_ponz007/items/74cedd21e49ff81d20b1)

- [【図解】Djangoチュートリアル備忘録 - プロジェクト構造とデータフローについて](https://qiita.com/gonzaemon/items/54cca866b337a4912d28)<br>
「**`Python`プログラムにおけるページ表示までのデータフロー**」や「**リクエスト処理サイクル**」、以下引用の「**`Django`のメリット**」など、`Django`の処理フローをはじめ包括的な概要理解がしやすい内容で参考になる。
> `Django`のメリット
> - 必要な機能が最初から揃っている
> - モデル定義さえすれば管理画面が自動生成される
> - セキュリティが高い
> - データベースの操作が容易（ORM）
> - スケーラビリティに優れた設計

- [streamlitを使ったお手軽Webアプリ開発](https://qiita.com/sypn/items/80962d84126be4092d3c)<br>
`Python`で簡単にWebアプリケーションを作成できるオープンソースのライブラリ`streamlit`の紹介及び実用例を交えた内容。ブラウザで`Python`を実行できるフレームワークなので「`Python`でフロントエンド開発」ということもできそう。

- [Streamlitで複数画面構成を実現するページ分割機能の実装方法](https://qiita.com/Tadataka_Takahashi/items/12b9120477e5a3617917)<br>
`streamlit`でのページネーション機能の実装方法を紹介している記事

## Python での非同期処理について
- [Python の async/await を徹底解説！コルーチンの仕組み](https://qiita.com/Leapcell/items/95dde75832c5ee4df0e7)<br>
`Python`での非同期処理について説明している内容。`JavaScript`と似ていて、`async / await`を用いて非同期処理を実現するが、`await asyncio`, `asyncio.run(非同期関数)`という独特な記法が求められる。

```py
# def hello():
#     print("hello leapcell")

# hello()
# 上記は、通常の（同期処理な）関数の記法

# 下記は、非同期処理の記法
import asyncio

async def hello():
    await asyncio.sleep(1)
    print("hello leapcell")

h = hello()     # コルーチンオブジェクトの返却
asyncio.run(h)  # 非同期関数の実行
```

## Tips
- [Pythonでのデバッグ、print()からic()に置き換えよう！](https://qiita.com/ryosuke_ohori/items/11b2ad43f1ae50f25cf5)