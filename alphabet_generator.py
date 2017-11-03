from PIL import Image, ImageDraw, ImageFont

import image_utils


def generate_data():
    """ Create letters, analyze them and save them """
    create_alphabet()
    crop_whole_alphabet()

    analyzed = analyze_whole_alphabet()
    save_analyzed_data(analyzed)


def create_alphabet():
    """ Create and save images of every letter of english alphabet """
    for ascii in range(26):
        ascii += 65
        create_letter(str(chr(ascii)))


def create_letter(letter):
    """ Create image of letter and save it """
    letter_image = Image.new('1', (200, 200), 1)
    draw = ImageDraw.Draw(letter_image)

    font = ImageFont.truetype('data/arial.ttf', 200)
    draw.text((0, 0), letter, font=font)

    image_utils.save_letter_as_image(letter_image, letter)


def crop_whole_alphabet():
    """ Crop image of every letter """
    for ascii in range(26):
        ascii += 65
        image = image_utils.load_letter_as_image(ascii)
        image = image_utils.crop_image(image)
        image_utils.save_letter_as_image(image, str(chr(ascii)))


def split_whole_alphabet():
    """ Return 26 lists containing splitted images """
    splitted = []
    for ascii in range(26):
        ascii += 65
        image = image_utils.load_letter_as_image(ascii)
        splitted.append(image_utils.split_image(image))
    return splitted


def analyze_whole_alphabet():
    """ Return list of 26 dictionaries with keys: letter, proportion, subproportions """
    sub_images = split_whole_alphabet()
    result = [{'letter': '',
               'proportion': 0,
               'subproportions': [[0 for _ in range(image_utils.SPLIT_NUMBER)] for _ in range(image_utils.SPLIT_NUMBER)]}
              for letter in range(26)]

    for letter_index in range(26):
        ascii = letter_index + 65

        result[letter_index]['letter'] = str(chr(ascii))

        image = image_utils.load_letter_as_image(ascii)
        hist = image_utils.histogram(image)
        result[letter_index]['proportion'] = hist['black']/(image.size[0] * image.size[1])

        for x in range(image_utils.SPLIT_NUMBER):
            for y in range(image_utils.SPLIT_NUMBER):

                hist = image_utils.histogram(sub_images[letter_index][x][y])
                result[letter_index]['subproportions'][x][y] = hist['black']/hist['white']

    return result


def save_analyzed_data(data):
    pass


def load_analyzed_data():
    pass
