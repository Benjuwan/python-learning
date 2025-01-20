# チャプター 4～xx 章まで

# 区切り（兼改行）用の文字列
duplicateCounter: int = 0
duplicateStr: str = "-+-"


# 区切り（兼改行）用の文字列を表示する関数
def duplicateCount(duplicateCounter: int):
    if duplicateCounter == 1:
        print(f"\n{str(duplicateCounter)} {duplicateStr * 20} \n")
    else:
        print(f"{str(duplicateCounter)} {duplicateStr * 20} \n")


duplicateCounter += 1
duplicateCount(duplicateCounter)

duplicateCounter += 1
duplicateCount(duplicateCounter)
