from PIL import Image, ImageDraw, ImageFont
from bidi.algorithm import get_display
import arabic_reshaper

def get_text():
    global bidi_text, englist, urlist
    englist = []
    urlist = []
    for no in range(1):
        print()
        englisttext = input(f"{no+1}. Enter English word: ")
        englist.append(englisttext)
        urdutext = input("Enter its meaning: ")
        text_to_be_reshaped = urdutext
        reshaped_text = arabic_reshaper.reshape(text_to_be_reshaped)
        bidi_text = get_display(reshaped_text)
        urlist.append(bidi_text)

get_text()

enfont = ImageFont.truetype('andlso.ttf', 120)
urfont = ImageFont.truetype('calibri.ttf', 110)

image = Image.open('BW.jpg')

image_draw = ImageDraw.Draw(image)
# # (330,1000, +200)
eng_init_pos = 970
ur_init_pos = 1010

for (en,ur) in zip(englist, urlist):
    image_draw.text((330,eng_init_pos), en, fill=(0,0,0,0), font=enfont)
    image_draw.text((1700,ur_init_pos), ur, fill=(0,0,0,0), font=urfont)
    eng_init_pos+=200
    ur_init_pos+=200

image.save(f'{englist[0]}.jpg')
image.show()

# For more details on PIL.Image and PIL.ImageDraw check the documentation
# See http://pillow.readthedocs.io/en/5.1.x/reference/ImageDraw.html?#PIL.ImageDraw.PIL.ImageDraw.Draw.text