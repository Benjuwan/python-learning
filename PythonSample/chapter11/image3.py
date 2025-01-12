from PIL import Image
image = Image.open('gradation.png')
print(image.format, image.width, image.height)
