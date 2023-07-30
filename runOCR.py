import os
import pytesseract
from pdf2image import convert_from_path
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
tessdata_dir_config = r'--tessdata-dir "C:\Program Files\Tesseract-OCR\tessdata"'

output_folder = 'output'
output2_folder = 'output2' 

if not os.path.exists(output2_folder):
    os.makedirs(output2_folder)
    
for pdf_name in os.listdir(output_folder):
    print('pdf_folder = ' + pdf_name)
    pdf_folder_path = os.path.join(output_folder, pdf_name)
    print('pdf_folder_path = ' + pdf_folder_path)
    output_dir = os.path.join(output2_folder, pdf_name)  
    print('output_dir = ' + output_dir)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for pdf in os.listdir(pdf_folder_path):
        print('pdf = ' + pdf)
        pdf_path = os.path.join(pdf_folder_path, pdf)
  
        images = convert_from_path(pdf_path)
        for i, image in enumerate(images):
            text = pytesseract.image_to_string(image, lang='por', config=tessdata_dir_config)
            page_name = os.path.splitext(pdf)[0]
            with open(os.path.join(output_dir, f'{page_name}.txt'), 'w') as f:
                f.write(text)
            
print('OCR complete!')
