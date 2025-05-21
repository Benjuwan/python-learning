import schedule
import datetime
import requests
from bs4 import BeautifulSoup

"""
schedule ライブラリ
設定したスケジュールに基づいて、指定した処理を定期的に実行する非標準ライブラリ
"""

# python web-scraping-schedules.py


def get_release_info():
    """[関数の概要]
    Args:

    Returns:
        | None
    """
    py_official_dl_page = requests.get("https://www.python.org/downloads/")
    py_official_dl_page.encoding = py_official_dl_page.apparent_encoding
    py_official_dl_page_content = py_official_dl_page.text

    soup = BeautifulSoup(py_official_dl_page_content, "html.parser")

    list_row_containers = soup.find_all("ol", class_="list-row-container")
    if list_row_containers is None:
        return

    for list_row_container in list_row_containers:
        lists = list_row_container.find_all("li")
        if lists is None:
            continue

        print(lists)
        for list in lists:
            release_number = list.find("span", class_="release-number")
            if release_number is None:
                continue

            release_number_anchor = release_number.find("a")
            release_date = list.find("span", class_="release-date")
            print(f"No.{release_number.text} | {release_number_anchor.text} / data:{release_date.text}")


get_release_info()
