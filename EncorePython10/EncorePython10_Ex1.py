from images import Image

image_smokey = Image("smokey.gif")


image_height = image_smokey.getHeight()/2
image_width = image_smokey.getWidth()

if image_smokey.getHeight() % 2 != 0:
    y = image_smokey.getHeight() + 1
    image_height = int(y/2)

for color in range(4):
    for x in range(image_width):
        image_smokey.setPixel(x, image_height, (255, 0, 0))
    image_height += 1

    for x in range(image_width):
        image_smokey.setPixel(x, image_height, (0, 255, 0))
    image_height += 1

    for x in range(image_width):
        image_smokey.setPixel(x, image_height, (0, 0, 255))
    image_height += 1


image_smokey.save("smokey_color")
image_smokey.draw()
