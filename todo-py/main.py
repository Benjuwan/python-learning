from utils.todo_lists_data import todo_lists
from features.read_get import get_todo
from features.create_post import post_todo
from features.update_put import put_todo
from features.delete import delete_todo


def run() -> None:
    while len(todo_lists) <= 10:
        order = input("""
実行したい内容を入力してください：
`get`: リスト確認
`post`: リスト追加
`update`: リスト更新
`delete`: リスト削除

""")

        if order == "get":
            get_todo()
        elif order == "post":
            post_todo()
        elif order == "update":
            put_todo()
        elif order == "delete":
            delete_todo()
        else:
            print("指定したコマンドでタスクを実行してください")


if __name__ == "__main__":
    run()
