# チャプター 11（応用編：ファイルの読み書き）

import csv
import json
import glob

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


# anothers フォルダに items.csv が無い場合は新規作成され、既にある場合は上書き保存される
# for_csv_txt_lists = [("hat", 2000), ("shirt", 1000), ("socks", 500)]
# with open("../anothers/items.csv", "w", encoding="utf-8", newline="") as csv_file:
#     csv_file_obj = csv.writer(csv_file)
#     csv_file_obj.writerows(for_csv_txt_lists)

with open("../anothers/items.csv", encoding="utf-8") as csv_file:
    csv_reader_obj = csv.reader(csv_file)
    # for item in csv_reader_obj:
    #     print(item)
    items = [tuple(item) for item in csv_reader_obj]
    print(items)
    # [('hat', '2000'), ('shirt', '1000'), ('socks', '500')]
    print(sorted(items, key=lambda item: int(item[1])))  # lambda 引数: （返却される）式
    # [('socks', '500'), ('shirt', '1000'), ('hat', '2000')]
    print(sorted(items, key=lambda item: int(item[1]), reverse=True))
    # [('hat', '2000'), ('shirt', '1000'), ('socks', '500')]

# anothers フォルダに items.json が無い場合は新規作成され、既にある場合は上書き保存される
# for_json_dict = [
#     {"name": "hat", "price": 2000},
#     {"name": "shirt", "price": 100},
#     {"name": "socks", "price": 500},
# ]
# with open("../anothers/items.json", "w", encoding="utf-8") as json_file:
#     json.dump(for_json_dict, json_file, indent=2)

with open("../anothers/items.json", encoding="utf-8") as json_file:
    print(json.load(json_file))
# [{'name': 'hat', 'price': 2000}, {'name': 'shirt', 'price': 100}, {'name': 'socks', 'price': 500}]

duplicate_counter += 1
duplicate_count(duplicate_counter)

# items というファイル名を持ったファイルまたはデータの一覧取得
for target in glob.glob("../anothers/items.*"):
    print(target)
    # ../anothers\items.csv
    # ../anothers\items.json

# yellow というファイル名を持ったファイルまたはデータの一覧取得
for target in glob.glob("../anothers/yellow.*"):
    print(target)
    # ../anothers\yellow.png

# random-color というファイル名を持ったファイルまたはデータの一覧取得
for target in glob.glob("../anothers/random-color.*"):
    print(target)
    # ../anothers\random-color.jpg
    # ../anothers\random-color.png
