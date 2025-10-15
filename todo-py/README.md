# todo-py
Pythonでの簡易なTodoリスト。学習用途で作成

- 以下コマンドで実行<br>
※このリポジトリ内で実行したい場合はディレクトリ移動（`cd todo-py`）した上で実行する
```py
python main.py
```

## 概要
### `utils\todo_lists_data.py`
プロジェクト全体で利用するTodoリスト。`list[dict[str, int | str | bool]]`という辞書データの配列データ形式になっている

### `utils\common_feat.py`
各種Todo機能で用いるユーティリティ関数（モジュール）

---

以下はTodoのコア機能モジュールたち

- `features\create_post.py`：Todo投稿・新規登録
- `features\delete.py`：Todo削除（※`todo_lists`をグローバル変数として認識させる処理を実施している）
- `features\read_get.py`：Todoリスト表示
- `features\update_put.py`：Todo更新（※`todo_lists`をグローバル変数として認識させる処理を実施している）

## 学習メモ部分
### 循環インポートエラー：
2つ以上のモジュールが**互いにインポートし合うことで発生するエラー**。例えば、モジュールAがモジュールBをインポートし、モジュールBもモジュールAをインポートしている場合、Pythonが**どちらを先に読み込むべきか判断できずエラー**となる。

#### 例：
- module_a.py が`from module_b import something`
- module_b.py が`from module_a import something`

#### 対策：
- モジュール間の依存関係を一方向にする
- 必要に応じて関数内でインポートする
- 共通の依存を別モジュールに分離する

### 絶対インポートの推奨：
相対インポート（`from . import モジュール名`）よりも、絶対インポート（`from ディレクトリ名.ファイル名 import モジュール名`）を使用する方がインポート元が明確でコードの可読性と保守性が向上する。

### `__init__.py`：
ディレクトリをPythonパッケージとして認識させるためのファイル。Python3.3以降は必須ではないが**配置することで確実にパッケージとして認識**される。**空ファイルでも機能する**が、パッケージの初期化コードや`__all__`によるエクスポート制御も記述できる。
