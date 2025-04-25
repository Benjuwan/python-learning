# チャプター 11（応用編：ファイルの読み書き）

# 区切り（兼改行）用の文字列
duplicate_counter: int = 0
duplicate_str: str = "-+-"


# 区切り（兼改行）用の文字列を表示する関数
def duplicate_count(duplicate_counter: int):
    if duplicate_counter == 1:
        print(f"\n{str(duplicate_counter)} {duplicate_str * 20} \n")
    else:
        print(f"{str(duplicate_counter)} {duplicate_str * 20} \n")


duplicate_counter += 1
duplicate_count(duplicate_counter)

# anothers フォルダに message.txt が無い場合は新規作成され、既にある場合は上書き保存される
# with open("../anothers/message.txt", "w", encoding="utf-8") as message_txt_file:
#     message_txt_file.write("Hello\n")
#     message_txt_file.write("Python\n")
#     message_txt_file.write("World\n")

# 第二引数を省略して`r`（読み込み）操作を実施
with open("../anothers/message.txt", encoding="utf-8") as message_txt_file:
    # print(message_txt_file.read().replace("\n", " "))
    for count, txt in enumerate(message_txt_file, 1):
        print(f"{count}: {txt}", end="")
