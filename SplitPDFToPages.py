import os
from PyPDF2 import PdfReader, PdfWriter  

input_folder = '.'
output_folder = 'output'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    if filename.endswith('.pdf'):
        pdf = PdfReader(open(os.path.join(input_folder, filename), 'rb')) 
        output_dir = os.path.join(output_folder, os.path.splitext(filename)[0])
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        for page_num in range(len(pdf.pages)):
            pdf_writer = PdfWriter()
            pdf_writer.add_page(pdf.pages[page_num])
            
            with open(os.path.join(output_dir, f'{page_num}.pdf'), 'wb') as out:
                pdf_writer.write(out)

print('Done!')
