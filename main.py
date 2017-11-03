import alphabet_generator
import image_utils


def OCR(path):
    """ Return the most similar letters (sorted) """
    image = image_utils.load_file(path)
    image = image_utils.crop_image(image)
    test_data = image_utils.analyze_image(image)
    alphabet_data = alphabet_generator.load_data()

    difference = [{'letter': '', 'diff': 0} for letter in range(26)]

    for letter in alphabet_data:
        index_letter = ord(letter['letter']) - alphabet_generator.ASCII_A
        temp_diff = 0

        for x in range(image_utils.SPLIT_NUMBER):
            for y in range(image_utils.SPLIT_NUMBER):
                data_letter = alphabet_data[index_letter]
                temp_diff += pow((test_data['subproportions'][x][y] * data_letter['proportion']
                                  - data_letter['subproportions'][x][y] * test_data['proportion']), 2)

        difference[index_letter]['letter'] = letter['letter']
        difference[index_letter]['diff'] = temp_diff

    return sorted(difference, key=lambda letter: letter['diff'])


def test_all_letters():
    for letter in range(26):
        letter += alphabet_generator.ASCII_A
        print(chr(letter), OCR("Data/Comic/" + chr(letter) + ".jpg")[0]['letter'])


def read_sentence(length):
    for letter in range(length):
        print(OCR("Data/Sentence/" + str(letter) + ".jpg")[0]['letter'], end="")


#alphabet_generator.create_comic()
#alphabet_generator.generate_data()
#test_all_letters()

#read_sentence(30)

#print(OCR("a.jpg")[0]['letter'])

'''
list_letters = OCR("A.jpg")
print([list_letters[i]['letter'] for i in range(3)])
'''

