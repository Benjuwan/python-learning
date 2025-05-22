import schedule
import datetime
import time
import requests
from bs4 import BeautifulSoup

"""
schedule ライブラリ
設定したスケジュールに基づいて、指定した処理を定期的に実行する非標準ライブラリ
"""


def get_release_info():
    py_official_dl_page = requests.get("https://www.python.org/downloads/")
    py_official_dl_page.encoding = py_official_dl_page.apparent_encoding
    py_official_dl_page_content = py_official_dl_page.text

    soup = BeautifulSoup(py_official_dl_page_content, "html.parser")

    release_info = []

    list_row_containers = soup.find_all("ol", class_="list-row-container")
    if list_row_containers is None:
        return

    for list_row_container in list_row_containers:
        lists = list_row_container.find_all("li")
        if lists is None:
            continue

        for list in lists:
            release_number = list.find("span", class_="release-number")
            if release_number is None:
                continue

            release_date = list.find("span", class_="release-date")
            # print(f"No.{release_number.text} / data:{release_date.text}")
            release_info.append(
                (release_number.text, release_date.text)
            )  # タプルで push

    currtime = f"{str(datetime.datetime.now().date()).replace('-', '/')}_{datetime.datetime.now().hour}:{datetime.datetime.now().minute}:{datetime.datetime.now().second}"
    print(f"実行時刻：{currtime}")

    for i, (ver, data) in enumerate(sorted(release_info)):
        # 先頭5行のみ表示
        if i == 5:
            break
        print(f"{ver:15} | {data}")  # ver は15文字スペースを取って表示レイアウト調整


# get_release_info()
schedule.every(10).seconds.do(get_release_info)  # 10秒ごとに実行

# 1行ごとにスケジュールを（延々と）実行
while True:  # 無限ループ
    schedule.run_pending()  # スケジュール（指定した定期的な処理）を実行
    time.sleep(1)  # 1秒後に処理実行
