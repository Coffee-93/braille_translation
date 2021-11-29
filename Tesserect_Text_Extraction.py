from PIL import Image
import pytesseract

import re
import cv2
from spellchecker import SpellChecker


def get_text(IMAGE_PATH):
    # If you don't have tesseract executable in your PATH, include the following:
    #pytesseract.pytesseract.tesseract_cmd = r'<full_path_to_your_tesseract_executable>'
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

    #Getting the text for the unaltered image
    unaltered_image = Image.open(IMAGE_PATH)
    tesserect_text = pytesseract.image_to_string(unaltered_image)
    
    spell = SpellChecker()
    unaltered_text = tesserect_text.split(' ')
    corrected_words = []
    for word in unaltered_text:
        corrected_words.append(spell.correction(word))
    unaltered_corrected_text = ' '.join(corrected_words)

    #Getting text from altering the image with cv2
    Read_Image = cv2.imread(IMAGE_PATH)
    #edges = cv2.Canny(Read_Image, 100, 200)
    gray = cv2.cvtColor(Read_Image, cv2.COLOR_BGR2GRAY)

    pillow_image = Image.fromarray(gray)
    cv2_text = pytesseract.image_to_string(pillow_image)
    
    cv2_words = cv2_text.split(' ')
    corrected_words = []
    for word in cv2_words:
        corrected_words.append(spell.correction(word))
    corrected_cv2_text = ' '.join(corrected_words)
    
    return tesserect_text, unaltered_corrected_text, cv2_text, corrected_cv2_text
