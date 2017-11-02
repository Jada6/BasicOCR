from PIL import Image
import math

image = None
SPLIT_NUMBER = 4
sub_images = [[[] for _ in range(SPLIT_NUMBER)] for __ in range(SPLIT_NUMBER)]
sub_images_proportion = [[0 for _ in range(SPLIT_NUMBER)] for __ in range(SPLIT_NUMBER)]
# actual_picture_coords


def create_image(name="letter.png", width=20, height=20):
    im = Image.new('1', (width, height), 0)

    '''
    for x in range(width):
        for y in range(height):
            im.putpixel((x, y), (0, 0, 0))
    '''

    im.save(name)


def read_file(name="letter.png"):
    global image
    image = Image.open(name)
    image = image.convert("1", ) # todo: 1, L, ??
    return read(image)


def read(image):
    result = {'white': 0, 'black': 0}
    width, height = image.size
    for x in range(width - 1):
        for y in range(height - 1):
            r = image.getpixel((x, y))
            result['white' if r == 255 else 'black'] += 1
            # result.append(r)
    #image.show()
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


def split_image():
    global image
    global sub_images

    width = image.size[0]
    height = image.size[1]

    for x in range(SPLIT_NUMBER):
        for y in range(SPLIT_NUMBER):
            coords = (((width / SPLIT_NUMBER) * x), ((height / SPLIT_NUMBER) * y),
                      ((width / SPLIT_NUMBER) * (x + 1)), ((height / SPLIT_NUMBER) * (y + 1)))
            sub_images[x][y] = image.crop(coords)
            list = read(sub_images[x][y])
            sub_images_proportion[x][y] = list['black']/list['white']

    print()


create_image()
list = read_file("test.png")

print("white:", list['white'])
print("black:", list['black'])
print(find_actual_coords())
crop_image()
image.show()

split_image()

for y in range(SPLIT_NUMBER):
    for x in range(SPLIT_NUMBER):
        list = read(sub_images[x][y])

        print(list['white'] + list['black'])

        pass
        # sub_images[x][y].show()


#for _ in range(len(sub_images))

