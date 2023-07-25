import os
from PyPDF2 import PdfReader
import re

def split_pdf_to_text(filepath, output_directory):
    reader = PdfReader(filepath)
    filename = os.path.splitext(os.path.basename(filepath))[0]
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    chunks = re.split(r'(?<=[.!?])\s+', text)
    chunk_text = ""
    chunk_count = 1
    for chunk in chunks:
        if len(chunk_text + chunk) > 64000:
            with open(f"{output_directory}/{filename}_chunk_{chunk_count}.md", "w", encoding="utf-8") as f:
                f.write(chunk_text)
            chunk_text = chunk
            chunk_count += 1
        else:
            chunk_text += " " + chunk
    if chunk_text:
        with open(f"{output_directory}/{filename}_chunk_{chunk_count}.md", "w", encoding="utf-8") as f:
            f.write(chunk_text)

def split_pdfs_in_directory(directory, output_directory):
    for filename in os.listdir(directory):
        if filename.endswith(".pdf"):
            pdf_output_directory = os.path.join(output_directory, os.path.splitext(filename)[0])
            if not os.path.exists(pdf_output_directory):
                os.makedirs(pdf_output_directory)
            split_pdf_to_text(os.path.join(directory, filename), pdf_output_directory)

split_pdfs_in_directory(os.getcwd(), "output")
