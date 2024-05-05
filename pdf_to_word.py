import os
import docx
from PyPDF2 import PdfReader

def pdf_to_word(pdf_path, output_path):
    try:
        doc = docx.Document()
        with open(pdf_path, 'rb') as file:
            reader = PdfReader(file)
            for page in reader.pages:
                text = page.extract_text()
                doc.add_paragraph(text)

        doc.save(output_path)
        print(f"PDF converted to Word document: {output_path}")
    except FileNotFoundError:
        print(f"Error: PDF file '{pdf_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    pdf_path = "Resume_Checklist.pdf"  # Replace with the actual path to your PDF file
    output_path = "output.docx"  # Replace with the desired output path for the Word document
    pdf_to_word(pdf_path, output_path)
