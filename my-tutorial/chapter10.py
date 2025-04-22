# チャプター 10 （応用編）

import random
from urllib.parse import urlparse
import time

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

url_parse_result = urlparse("https://github.com/Benjuwan/python-learning")
print(url_parse_result)

duplicate_counter += 1
duplicate_count(duplicate_counter)

print(random.random())
print(random.randint(1, 10))
target_list = ["Morning", "Afternoon", "Evening", "Night"]
print(random.choice(target_list))
random.shuffle(target_list)
print(target_list)

duplicate_counter += 1
duplicate_count(duplicate_counter)

print(time.time())
print(time.gmtime())
local_time = time.localtime()
print(local_time)
print(
    f"{local_time.tm_year}年{local_time.tm_mon}月{local_time.tm_mday}日 {local_time.tm_hour}時{local_time.tm_min}分{local_time.tm_sec}秒"
)
