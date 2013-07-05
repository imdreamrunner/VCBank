import Image, ImageDraw, ImageFont, cStringIO, random

# Edited from http://kzar.co.uk/blog/2009/07/14/web.py-captcha/

def getCaptcha():
    im = Image.new("RGB", (100, 50))
    draw = ImageDraw.Draw(im)

    for x in range(0, 100):
        for y in range(0, 50):
            draw.point((x, y), (255, 255, 255))

    font = ImageFont.truetype('fonts/Lekton.ttf', 50)

    alphabet = 'abcdefghijkmnpqrstuvwxyz23456789'

    word = ''.join(random.choice(alphabet) for x in range(4))\

    draw.text((0, 0), word, font=font, fill=(0, 0, 0))

    f = cStringIO.StringIO()
    im.save(f, "PNG")
    f.seek(0)
    return word, f