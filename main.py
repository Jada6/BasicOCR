from PIL import Image

image = None
sub_images = [None for _ in range(16)]
# actual_picture_coords


def create_image(name="letter.png", width=20, height=20):
    im = Image.new('1', (width, height), 0)

    '''
    for x in range(width):
        for y in range(height):
            im.putpixel((x, y), (0, 0, 0))
    '''

    im.save(name)


def read(name="letter.png"):
    result = {'white': 0, 'black': 0}
    global image
    image = Image.open(name)
    image = image.convert("L", ) # todo: 1, L, ??
    width, height = image.size
    for x in range(width - 1):
        for y in range(height - 1):
            r = image.getpixel((x, y))
            result['white' if r == 255 else 'black'] += 1
            # result.append(r)
    image.show()
    return result


def find_actual_coords():
    global image
    # return image.size

    extremes = {'left': image.size[0], 'right': 0, 'top': image.size[1], 'bot': 0}

    for x in range(image.size[0]):
        for y in range(image.size[1]):
            # todo: general color?
            if image.getpixel((x, y)) != 0:
                continue

            if x < extremes['left']:
                extremes['left'] = x
            if x > extremes['right']:
                extremes['right'] = x
            if y < extremes['top']:
                extremes['top'] = y
            if y > extremes['bot']:
                extremes['bot'] = y

    return extremes

    # return image.histogram()[0]


def crop_image():
    global image

    extremes = find_actual_coords()
    image = image.crop((extremes['left'], extremes['top'], extremes['right'], extremes['bot']))


create_image()
list = read("test.png")

print(list['white'])
print(list['black'])
print(find_actual_coords())
crop_image()
image.show()
