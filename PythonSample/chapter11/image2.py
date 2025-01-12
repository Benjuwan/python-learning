from PIL import Image
W, H = 640, 480
image = Image.new('RGB', (W, H), (0, 0, 0))
for x in range(W):
    for y in range(H):
        image.putpixel((x, y),
                       (x*255//W, y*255//H, 
                        ((W+H)-(x+y))*255//(W+H)))
image.save('gradation.png')
