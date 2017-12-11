import os
import json
from PIL import Image, ImageDraw, ImageFont

import image_utils

ASCII_A = ord('A')


def generate_reference_data():
    """ Create letters, analyze them and save them """
    print("Creating letters...")
    create_alphabet()
    print("Cropping letters...")
    crop_whole_alphabet()
    print("Analyzing alphabet...")
    analyzed = analyze_whole_alphabet()
    print("Saving as reference_propotions.json...")
    save_analyzed_data(analyzed)
    print("Done")


def create_alphabet(dir="Data/Alphabet/", source='Data/arial.ttf'):
    """ Create and save images of every letter of english alphabet """
    if not os.path.exists(dir):
        os.makedirs(dir)
    for ascii in range(26):
        ascii += ASCII_A
        create_letter(str(chr(ascii)), dir, source)


def create_comic():
    create_alphabet("Data/Comic/", "Data/comic.ttf")
    crop_whole_alphabet("Data/Comic/")


def create_letter(letter, dir, source):
    """ Create image of letter and save it """
    letter_image = Image.new('1', (300, 300), 1)
    draw = ImageDraw.Draw(letter_image)

    font = ImageFont.truetype(source, 200)
    draw.text((0, 0), letter, font=font)

    image_utils.save_letter_as_image(dir, letter_image, letter)


def crop_whole_alphabet(dir="Data/Alphabet/"):
    """ Crop image of every letter """
    for ascii in range(26):
        ascii += ASCII_A
        image = image_utils.load_letter_as_image(ascii, dir)
        image = image_utils.crop_image(image)
        image_utils.save_letter_as_image(dir, image, chr(ascii))


def analyze_whole_alphabet():
    """ Return list of 26 dictionaries with keys:
    letter, proportion, subproportions """
    result = [{'letter': '',
               'proportion': 0,
               'subproportions': [[0 for _ in range(image_utils.SPLIT_NUMBER)]
                                  for _ in range(image_utils.SPLIT_NUMBER)]}
              for letter in range(26)]

    for letter_index in range(26):
        ascii = letter_index + ASCII_A
        result[letter_index]['letter'] = chr(ascii)

        image = image_utils.load_letter_as_image(ascii, "Data/Alphabet/")
        analyzed = image_utils.analyze_image(image)

        result[letter_index]['proportion'] = analyzed['proportion']
        result[letter_index]['subproportions'] = analyzed['subproportions']

    return result


def save_analyzed_data(data):
    with open("Data/reference_proportions.json", "w") as json_file:
        json.dump(data, json_file)


def load_reference_proportions():
    with open("Data/reference_proportions.json") as json_file:
        data = json.load(json_file)

    return data
