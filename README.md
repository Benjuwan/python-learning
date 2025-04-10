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

- `Mypy Type Checker`（`mypy`）<br>動的型付け言語の`Python`に型を付けてくれる。

## 参照
- [【令和6年最新版】初心者でも、チーム開発でも美しく！Python開発環境構築のすすめ](https://qiita.com/musutafakemaru/items/332bd0193828aa66461d)
- [DjangoとuWSGI、Nginxの関係を理解したい](https://qiita.com/yuzu_ponz007/items/74cedd21e49ff81d20b1)

### 仮想環境の構築
仮想環境を用いることで、いろいろなバージョンの`Python`（プロジェクト）を同じPCの中で混在させて、プロジェクトによって使い分けられる。<br>つまり、各プロジェクトごとの設定やバージョンを個別に固定管理できるようになる。

#### `venv`
仮想環境を作成する`Python`のデファクトスタンダードな標準ライブラリ。
- 参考記事：[Python仮想環境ツール多すぎ！ 一番ベーシックな「venv」から再入門しよう](https://qiita.com/minorun365/items/94bdb12eb42581850315)

> [!NOTE]
> 記事内における「仮想環境の`activate`」の部分について補足
> - 仮想環境を`activate`するには以下のコマンドを入力する
>   - Windowsの場合：   `.\仮想環境名\Scripts\activate`
>   - Mac/Linuxの場合： `source ./仮想環境名/bin/activate`<br>
> パスの先頭に(仮想環境名)が表示されていれば成功

#### `uv`
`venv`の仮想環境構築に加えて、パッケージ管理までも実現できる（2025年時点では比較的新しい）サードパーティライブラリ。パッケージ管理 + 仮想環境という機能を持ち合わせていながらも、`Rust`製による非常に高速なパフォーマンスを備えている。`venv`と`pip`の機能を統合し、より効率的なワークフローを提供しているのも特徴。
- 参考記事：[Pythonの開発用適当ツールの作成・実行はuvを使うのがオススメ](https://qiita.com/ssc-ksaitou/items/9da75058489ebe8c2009)

### ライブラリやフレームワーク関連
- [Django実践開発入門](https://qiita.com/Syoitu/items/d3a28b2a7acdf90fbccd)<br>
`Django`（ジャンゴ）で簡易的なスクール学生管理システムをハンズオンしていく内容。ファイル構成案や各種情報、Tipsなど色々と参考になる。

- [streamlitを使ったお手軽Webアプリ開発](https://qiita.com/sypn/items/80962d84126be4092d3c)<br>
`Python`で簡単にWebアプリケーションを作成できるオープンソースのライブラリ`streamlit`の紹介及び実用例を交えた内容。ブラウザで`Python`を実行できるフレームワークなので「`Python`でフロントエンド開発」ということもできそう。

### Python での非同期処理について
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

### Tips
- [Pythonでのデバッグ、print()からic()に置き換えよう！](https://qiita.com/ryosuke_ohori/items/11b2ad43f1ae50f25cf5)
