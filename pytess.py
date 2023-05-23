import os, pytesseract
from PIL import Image
from config import tespath
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

pytesseract.pytesseract.tesseract_cmd = tespath

custom_config = '--oem 3 --psm 1'

async def get_cods(name):
    img = Image.open(f'Photo/{name}')

    promo = pytesseract.image_to_string(img, config=custom_config)
    promoSplit = promo.split()

    cods = []
    
    for word in promoSplit:
        if "KREED" in word or "BUSTER" in word:
            cods.append(word)

    return cods

