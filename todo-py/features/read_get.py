from utils.todo_lists_data import todo_lists


def get_todo() -> None:
    print("今のToDOリストは以下です")
    for i, item in enumerate(todo_lists):
        if i == len(todo_lists) - 1:
            print(f"{item}\n")
        else:
            print(item)

    return


if __name__ == "__main__":
    get_todo()
