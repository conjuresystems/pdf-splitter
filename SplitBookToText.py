import os
import pdfplumber

def convert_pdf_to_text(file, output_directory):
    MAX_SIZE = 16 * 1024 * 1024  # 16MB
    current_size = 0
    file_count = 0
    output_file = None

    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            text = text.encode('utf-8')  # Convert to bytes to get accurate size

            if current_size + len(text) > MAX_SIZE or output_file is None:
                if output_file is not None:
                    output_file.close()

                output_filename = f"{os.path.splitext(os.path.basename(file))[0]}_chunk_{file_count}.txt"
                output_filepath = os.path.join(output_directory, output_filename)
                output_file = open(output_filepath, 'wb')

                current_size = 0
                file_count += 1

            output_file.write(text)
            current_size += len(text)

        if output_file is not None:
            output_file.close()

def convert_pdfs_in_directory(directory):
    output_directory = os.path.join(directory, 'output2')
    os.makedirs(output_directory, exist_ok=True)

    for filename in os.listdir(directory):
        if filename.endswith(".pdf"):
            filepath = os.path.join(directory, filename)
            convert_pdf_to_text(filepath, output_directory)

convert_pdfs_in_directory(os.getcwd())
