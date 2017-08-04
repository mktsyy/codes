import Image

img = Image.open('2222.jpg')

region = (40,5,50,20)

cropImg = img.crop(region)

cropImg.save("temp.jpg")