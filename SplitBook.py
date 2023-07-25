import os
from PyPDF2 import PdfReader, PdfWriter

def split_pdf(file, output_directory):
    reader = PdfReader(file)
    num_pages = len(reader.pages)
    for start_page in range(0, num_pages, 10):
        end_page = min(start_page + 10, num_pages)
        writer = PdfWriter()

        for page_number in range(start_page, end_page):
            writer.add_page(reader.pages[page_number])

        output_filename = f"{os.path.splitext(os.path.basename(file))[0]}_pages_{start_page+1}_to_{end_page}.pdf"
        output_filepath = os.path.join(output_directory, output_filename)

        with open(output_filepath, 'wb') as output_pdf:
            writer.write(output_pdf)

def split_pdfs_in_directory(directory):
    output_directory = os.path.join(directory, 'output')
    os.makedirs(output_directory, exist_ok=True)

    for filename in os.listdir(directory):
        if filename.endswith(".pdf"):
            filepath = os.path.join(directory, filename)
            split_pdf(filepath, output_directory)

split_pdfs_in_directory(os.getcwd())
