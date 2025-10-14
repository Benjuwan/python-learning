from utils.todo_lists_data import todo_lists
from features.read_get import get_todo
from utils.common_feat import input_id, echo_result


def put_todo() -> None:
    # このスコープ内（ローカルスコープ）での`todo_lists`として扱われてしまうので`global`でグローバル変数として認識してもらう
    global todo_lists

    get_todo()

    id = input_id("更新")

    if id is None:
        print("id がありません。処理終了します")
        return

    is_exist_target_item = len([item for item in todo_lists if item["id"] == id]) == 0
    if is_exist_target_item:
        print(f"指定したID:{id} は存在しません")
        return

    todo = input("タスクを入力：")

    # 対象Todo要素のtodoを更新内容に変換
    def _update_item(item: dict[str, int | str | bool]):
        if item["id"] == id:
            # 新規Todo内容に更新（辞書のキーはブラケット記法でアクセス）
            item["todo"] = todo
            return item
        else:
            return item

    # `_update_item`関数で**辞書オブジェクトを直接変更している**ため、`todo_lists`内の該当する辞書（Todoアイテム）の内容が更新される
    list(map(_update_item, todo_lists))

    echo_result()

    return


if __name__ == "__main__":
    put_todo()
