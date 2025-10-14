from utils.todo_lists_data import todo_lists
from utils.common_feat import echo_result


def post_todo() -> None:
    new_id_index = (
        len(todo_lists) + 1
        if len(todo_lists) == 0
        else int(todo_lists[len(todo_lists) - 1]["id"]) + 1
    )

    todo = input("タスクを入力：")

    new_todo_item: dict[str, int | str | bool] = {
        "id": new_id_index,
        "todo": todo,
        "is_edit": False,
    }

    todo_lists.append(new_todo_item)

    echo_result()

    return


if __name__ == "__main__":
    post_todo()
