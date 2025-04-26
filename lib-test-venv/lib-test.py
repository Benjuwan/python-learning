# Pil.Imageモジュールをインポート
from PIL import Image

import random

# ## 新規画像作成
# the_Image = Image.new("モード", (幅, 高さ), 背景色)

# ### モードには以下の三種類がある。
# モード1. "L"（8ビットグレースケール）
# モード2. "RGB"（Red, Green, Blue、各8ビット）
# モード3. "RGBA"（Red, Green, Blue, alpha：不透明度、各8ビット）

# #### サンプル
# the_Image = Image.new("RGB", (幅, 高さ), (R成分, G成分, B成分))

# ## 作成した画像の保存
# 指定したファイル名が存在しない場合は新規作成されて、既にある場合は上書き保存される
# the_Image.save(ファイル名.拡張子)

the_Image_gold = Image.new("RGB", (640, 480), "gold")
the_Image_gold.save("../anothers/gold.jpg")

the_Image_yellow = Image.new("RGB", (640, 480), (255, 255, 0))
the_Image_yellow.save("../anothers/yellow.png")

the_Image_yellow.putalpha(128)  # 不透明度の指定（0～255）
the_Image_yellow.save("../anothers/yellow-opacity.png")

the_Image_random = Image.new(
    "RGB",
    (640, 480),
    (
        0,
        0,
        0,
    ),
)
for x in range(255):
    for y in range(255):
        R = x * 255 // 640
        G = y * 255 // 480
        B = random.randint(0, x * y)
        # print(R, G, B)
        the_Image_random.putpixel((x, y), (R, G, B))
the_Image_random.save("../anothers/random-color.jpg")

# ## 画像ファイルの読み込み
# open(ファイル名)関数は画像のオブジェクトを返す
the_Image_random_obj = Image.open("../anothers/random-color.jpg")
get_Image_type = the_Image_random_obj.format
get_Image_size = the_Image_random_obj.size
get_Image_w = the_Image_random_obj.width
get_Image_h = the_Image_random_obj.height
print(get_Image_type, get_Image_size, get_Image_w, get_Image_h)
# JPEG (640, 480) 640 480

# ## jpg から png に画像ファイル拡張子を変更
the_Image_random.save("../anothers/random-color.png")
the_Image_random_obj_xai = Image.open("../anothers/random-color.png")
print(the_Image_random_obj_xai.format, the_Image_random_obj_xai.size)
# PNG (640, 480)
