
from PIL import Image, ImageDraw, ImageFont

IMAGE_LOC = 'me.jpg'
FONT_LOC  = "/Users/adammcmurchie/amu/amu_0.0.3/assets/font/roboto/Roboto-Bold.ttf"


img = Image.open(IMAGE_LOC)
# img.show()
WIDTH, HEIGHT = img.size

font = ImageFont.truetype(FONT_LOC, 10)
cell_width, cell_height = 10, 10

img = img.resize((int(WIDTH / cell_width), int(HEIGHT / cell_height)), Image.NEAREST)
new_width, new_height = img.size
img = img.load()

new_img = Image.new('RGB', (WIDTH, HEIGHT), (0, 0, 0))
d = ImageDraw.Draw(new_img)

for i in range(new_height):
    for j in range(new_width):
        r, g, b,a = img[j, i]
        k = int((r + g + b) / 3)
        if k < 128:
            text = "1"
        else:
            text = "0"
        d.text((j * cell_width, i * cell_height), text=text, font=font, fill=(0, g, 0))

# new_img.show()
new_img.save("me_0_1.jpg")
new_img.show()

