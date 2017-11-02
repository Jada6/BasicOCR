from PIL import Image, ImageDraw, ImageFont


def create_alphabet():
    for ascii in range(65, 91):
        create_letter(str(chr(ascii)))


def create_letter(char):
    letter_image = Image.new('1', (200, 200), 1)
    draw = ImageDraw.Draw(letter_image)

    #font = ImageFont.load("arial.ttf")
    font = ImageFont.truetype('data/arial.ttf', 200)
    draw.text((0, 0), char, font=font)

    letter_image.save("data/alphabet/" + char + ".jpg")
    #letter_image('sample-out.jpg')