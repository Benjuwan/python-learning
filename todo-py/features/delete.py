from utils.todo_lists_data import todo_lists
from features.read_get import get_todo
from utils.common_feat import input_id, echo_result


def delete_todo() -> None:
    # このスコープ内（ローカルスコープ）での`todo_lists`として扱われてしまうので`global`でグローバル変数として認識してもらう
    global todo_lists

    get_todo()

    id = input_id("削除")

    if id is None:
        print("id がありません。処理終了します")
        return

    is_exist_target_item = len([item for item in todo_lists if item["id"] == id]) == 0
    if is_exist_target_item:
        print(f"指定したID:{id} は存在しません")
        return

    # 渡ってきたIDと異なるTodo要素を排除
    def _delete_item(item: dict[str, int | str | bool]):
        # 辞書のキーはブラケット記法でアクセス
        if item["id"] != id:
            return item
        else:
            return None

    # `()`を付与して関数宣言する場合は引数指定が必要となるので`lambda`で引数を用意する
    # lambda 引数: 式
    deleted_todo_lists = list(filter(lambda item: _delete_item(item), todo_lists))

    # 既存リストを更新：`todo-py\features\update_put.py`で行っている処理（Todoリスト内の辞書データ書き換え）と違って、ここでは条件に応じた結果（Todoリスト）を返しているだけなので以下の代入処理が必要となる
    # `[:]`で`todo_lists`の中身を一度空にしてから削除処理した内容（`deleted_todo_lists`）を反映させる
    todo_lists[:] = deleted_todo_lists

    echo_result()

    return
