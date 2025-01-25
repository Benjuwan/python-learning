# チャプター 5

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

lot_numbers = 123456


# def checkLotNumbers(targetNumbers: int):
def checkLotNumbers(targetNumbers):
    if targetNumbers == 123456:
        print(f"{targetNumbers} is Special Prize")
    elif type(targetNumbers) is not int:
        print("we are accept only Number")
    else:
        print(f"{targetNumbers} is no Prize")


checkLotNumbers(123456)
checkLotNumbers(159753)
checkLotNumbers("123456")
