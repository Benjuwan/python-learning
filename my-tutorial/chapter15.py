# チャプター 15（応用編：データベースとWebプログラミング）
# ※ チャプター13～14 までの内容はライブラリ関連のフォルダ（`lib-test-venv`）に

import sqlite3
import sys

# データベースへの接続
connection = sqlite3.connect("../anothers/sample-sqlite.db")

# データベース操作を行うカーソルオブジェクトを用意
cursor_obj = connection.cursor()

# SQLを発行・実行する
cursor_obj.execute(
    "DROP TABLE IF EXISTS account_table"
)  # `account_table`テーブルが存在する場合は削除する
cursor_obj.execute(
    "CREATE TABLE account_table (user TEXT PRIMARY KEY, password TEXT)"
)  # `account_table`テーブルを作成し、user列とpassword列を追加する

user_lists = [("suzuki", "abc123"), ("satou", "def456"), ("tanaka", "ghi789")]
cursor_obj.executemany(
    "INSERT INTO account_table VALUES (?, ?)", user_lists
)  # テーブルに行（左?：user, 右?：password）を追加

# 変更を保存
connection.commit()

# データベースからデータを取得（今回の事例では変更確認）
cursor_obj.execute("SELECT * FROM account_table")  # account_table から全ての行を取得

for user, pw in cursor_obj:
    print(f"name:{user:8}, pw:{pw}")

## ログイン機能 ------------------------------------------------


# def login_failed():
#     print("Failed（失敗）")
#     return


# entry_user = input("ユーザー名を入力")
# for user, pw in cursor_obj:
#     is_user_exist = entry_user in user

#     if is_user_exist is False:
#         continue

#     if is_user_exist:
#         entry_pw = input("パスワードを入力")
#         is_pw_exist = entry_pw in pw
#         is_login = is_user_exist and is_pw_exist

#         print("Welcome!（ようこそ）") if is_login else login_failed()

## ログイン機能 ------------------------------------------------

# print(len(sys.argv))  # 1, 2, 3
# if len(sys.argv) != 3:
#     # （コマンドライン引数が3つ無い場合は）引数に指定した文字列を表示して処理終了
#     this_filename = sys.argv[0]
#     sys.exit(f"Usage Python {this_filename} user(arg1) password(arg2)")

# except_filename_args = sys.argv[1:]  # 最初以外の全ての引数
# print(except_filename_args)  # ['suzuki', 'abc123']
# cursor_obj.execute(
#     # user=? には except_filename_args のユーザー名が、
#     # password=? には except_filename_args のパスワードが入る
#     "SELECT * FROM account_table WHERE user=? AND password=?",
#     except_filename_args,
# ) # account_table テーブルから、user列と password列が指定した値（コマンドライン引数の内容）に等しい行を取得する

# print("Welcome!" if len(list(cursor_obj)) > 0 else "Failed.")

## ------------------------------------------------

update_user = "suzuki"
update_password = "HOGE-FOO"
cursor_obj.execute(
    "UPDATE account_table SET password=? WHERE user=?", (update_password, update_user)
)  # user列に指定した値と等しい行の password 列の値を変更（更新）する

cursor_obj.execute("SELECT * FROM account_table")  # account_table から全ての行を取得
for user, pw in cursor_obj:
    print(f"name:{user:8}, pw:{pw}")

# 接続終了
connection.close()
