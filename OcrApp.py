from cv2 import cv2
import pytesseract
import os
from tqdm import tqdm

path_file = 'D:\\Cloud\\Pictures\\OCR\\'
path_tess = 'C:\\Program Files\\Tesseract-OCR\\'

pytesseract.pytesseract.tesseract_cmd = path_tess+'tesseract.exe'

def ocr_img(img):
    ocr_text = pytesseract.image_to_string(img, lang='rus+eng+ukr')
    return ocr_text

def write_text(ocr_text, name_file):
    ocr_file = open(path_file + name_file + '.txt', 'w')
    for j in ocr_text:
        ocr_file.write(j)
    print()
    ocr_file.close()

dir_ocr = os.listdir(path_file)
print(dir_ocr)

for i in range(len(dir_ocr)):
    name_file = dir_ocr[i].split('.')[0]
    ext_file = dir_ocr[i].split('.')[1]
    if ext_file == 'jpg':
        img = cv2.imread(path_file + dir_ocr[i])
        print('Распознаем текст в файле ' + dir_ocr[i])
        ocr_text = ocr_img(img)
        print('Записываем в файл ' + name_file + '.txt')
        write_text(ocr_text, name_file)



# #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# # cv2.imshow('Result', img)
# # cv2.waitKey(0)

# #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# # cv2.imshow('Result', img)
# # cv2.waitKey(0)
