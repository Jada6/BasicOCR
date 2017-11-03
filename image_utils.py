from PIL import Image

SPLIT_NUMBER = 3


def histogram(image):
    """ Return histogram of the image as dictionary representing number of black and white pixels """
    result = {'white': 1, 'black': 0}  # white = 1, because it will be divided later
    width, height = image.size

    for x in range(width):
        for y in range(height):
            r = image.getpixel((x, y))
            result['white' if r == 255 else 'black'] += 1
    return result


def find_actual_coords(image):
    """ Return dictionary of min/max coordinates with black pixels """
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


def crop_image(image):
    """ Crop white edges from image. Return the cropped image """
    extremes = find_actual_coords(image)
    return image.crop((extremes['left'], extremes['top'], extremes['right'], extremes['bot']))


def split_image(image):
    """" Return SPLIT_NUMBER ^ 2 subimages """
    sub_images = [[[] for _ in range(SPLIT_NUMBER)] for __ in range(SPLIT_NUMBER)]

    width = image.size[0]
    height = image.size[1]

    for x in range(SPLIT_NUMBER):
        for y in range(SPLIT_NUMBER):
            coords = (((width / SPLIT_NUMBER) * x), ((height / SPLIT_NUMBER) * y),
                      ((width / SPLIT_NUMBER) * (x + 1)), ((height / SPLIT_NUMBER) * (y + 1)))
            sub_images[x][y] = image.crop(coords)
    return sub_images


def load_file(name):
    image = Image.open(name)
    return image.convert("1")


def save_letter_as_image(image, letter):
    image.save("data/alphabet/" + letter + ".jpg")


def load_letter_as_image(letter):
    return load_file("Data/Alphabet/" + str(chr(letter)) + ".jpg")
