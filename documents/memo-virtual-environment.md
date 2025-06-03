## 仮想環境の構築
仮想環境を用いることで、いろいろなバージョンの`Python`（プロジェクト）を同じPCの中で混在させて、プロジェクトによって使い分けられる。<br>つまり、各プロジェクトごとの設定やバージョンを個別に固定管理できるようになる。

> [!NOTE]
> 仮想環境の構築や修正、移行などで複雑な状況になってしまった場合は、**大人しく最初から作り直した方がスムーズ**なケースもある

### コマンド操作
#### 仮想環境関連
`python -m pip`または`pip`（macOS/Linuxの場合は`python3 -m pip`または`pip3`）で実行
```py
# `-m`： 指定したモジュールを起動するためのオプション（コマンド）
python -m モジュール
```

##### 仮想環境（`venv`）の構築例
※`GitHub`でプロジェクト管理していて不要なファイルなどは省かれている（`.gitignore`されている）状態を前提とする
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
source env/bin/activate   # WindowsOS の場合: 仮想環境名\Scripts\activate

# 4. アクティベートした状態で requirements.txt に定義されたパッケージをインストール
# ※ 既存の仮想環境ディレクトリ（及び requirements.txt ）がある場合は、アクティベート状態でコマンド移動（cd dir）してから下記コマンドにて各種ライブラリをインストールする
python -m pip install -r requirements.txt
```

- 【初期設定】`requirements.txt`からライブラリをインストール<br>
**仮想環境をアクティベートした状態**で以下コマンドを実行
```bash
# 1. 仮想環境を格納しているディレクトリへ移動（存在しない場合は上記を参照に新規作成）
# cd 仮想環境格納dir名

# 2. 仮想環境をアクティベート（Mac | Linux の場合は`source 仮想環境名/bin/activate`）
# ../プロジェクト名\仮想環境格納dir名> $ 仮想環境名\Scripts\activate

# 3. 仮想環境をアクティベートした状態で
#    パスを指定（※以下は`requirements.txt`をルートに置いている場合）して各種ライブラリをインストール
python -m pip install -r ../requirements.txt
```

- フルパス指定で仮想環境を閉じる<br>
仮想環境を格納しているディレクトリ（例：`venv`dir）で以下コマンドを実行
```bash
# フルパス指定で deactivate または venv\Scripts\deactivate.bat
venv\Scripts\deactivate
```

#### ライブラリの取り扱い関連
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

#### ライブラリをグローバルインストールしてしまった場合
以下コマンドを実行すれば`pip`以外全てのライブラリがリセット（削除）される
- Mac/Linux の場合
```bash
pip freeze | xargs pip uninstall -y
```

- windows の場合
```bash
for /f %i in ('pip freeze') do pip uninstall %i -y
```

---

### `venv`
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

#### `venv`で構築した仮想環境が`deactivate`しても、ターミナルを立ち上げる度に起動されている場合の対処法
1. VSCode の左下設定（歯車アイコンを押下）の`設定`項目を開く
2. 設定の検索で`Python > Terminal: Activate Environment`を入力
3. `ユーザー`欄の当該項目のチェックを外す

### `uv`
`venv`の仮想環境構築に加えて、パッケージ管理までも実現できる（2025年時点では比較的新しい）サードパーティライブラリ。パッケージ管理 + 仮想環境という機能を持ち合わせていながらも、`Rust`製による非常に高速なパフォーマンスを備えている。`venv`と`pip`の機能を統合し、より効率的なワークフローを提供しているのも特徴。
- 参考記事：[Pythonの開発用適当ツールの作成・実行はuvを使うのがオススメ](https://qiita.com/ssc-ksaitou/items/9da75058489ebe8c2009)

> uvはPythonパッケージだけでなくPythonのバージョン自体も管理することが可能なため、プロジェクトごとに異なるPythonバージョンや依存関係を管理するのに適したツールだと言える。...中略
> Anacondaは一定以上の規模の企業で利用する場合に、ライセンス料がかかってしまう点には注意したい。...中略
> uvはまだ歴史が浅く発展途上であるため、破壊的な変更が加えられる可能性も高い。開発期間が長いpyenvやpoetryなどのツールの方が安定した利用が見込め、そういった観点ではこちらの選択肢もまだあり得るだろう。

- 参照記事：[uv （pythonパッケージマネージャー）の使い方 簡易版](https://zenn.dev/tabayashi/articles/197205349d6935)
- 参照記事：[uv （pythonパッケージマネージャー）の使い方 詳細版](https://zenn.dev/tabayashi/articles/52389e0d6c353a)
- 参考記事：[Python Coding Best Practices for Researchers](https://cyberagentailab.github.io/BestPracticesForPythonCoding/#management-tools)
- 参考記事：[AIエージェントにも正しく使ってほしいPython環境管理ツール「uv」最新情報ガイド](https://qiita.com/ootakazuhiko/items/4fa2406534777d86f333)
- 参考記事：[Pythonパッケージ管理 [uv] 完全入門](https://speakerdeck.com/mickey_kubo/pythonpatukeziguan-li-uv-wan-quan-ru-men)
