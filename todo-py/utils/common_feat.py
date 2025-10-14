from utils.todo_lists_data import todo_lists


def echo_result():
    print("ただいま更新したToDOリストは以下です")
    for i, item in enumerate(todo_lists):
        if i == len(todo_lists) - 1:
            print(f"{item}\n")
        else:
            print(item)


def input_id(task_label: str) -> int | None:
    id_str = input(f"{task_label}したいリストIDを入力：")

    try:
        id_num = int(id_str)  # 文字列を整数に変換
    except ValueError:
        print("IDは数値で入力してください")
        return None

    return id_num


if __name__ == "__main__":
    echo_result()
    input_id("")
