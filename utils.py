from io import BytesIO
from PyPDF2 import PdfReader
import docx
import docx2txt
import pypandoc
import subprocess
import os
from tempfile import NamedTemporaryFile

def read_pdf(file: bytes) -> str:
    try:
        reader = PdfReader(BytesIO(file))
        full_text = []
        for page in reader.pages:
            full_text.append(page.extract_text())
        return '\n'.join(full_text)
    except Exception as e:
        raise ValueError(f"Failed to read PDF: {str(e)}")

"""
Create a temp/temp.docx file and place the path in temp_file_path in read_word_docx2txt
"""

def read_word_docx2txt(file: bytes) -> str:
    try:
        temp_file_path = r"C:\Users\AnandVarrier\Resume_parser\temp\temp.docx" 
        with open(temp_file_path, "wb") as f:
            f.write(file)

        text = docx2txt.process(temp_file_path)
        return text
    except Exception as e:
        raise ValueError(f"Failed to read DOCX: {str(e)}")

def read_word_doc(file: bytes) -> str:
    try:
        # Save the bytes to a temporary file
        with NamedTemporaryFile(delete=False, suffix=".doc") as temp_file:
            temp_file.write(file)
            temp_file_path = temp_file.name

        # Convert .doc to .docx using unoconv or libreoffice
        temp_docx_path = temp_file_path + "x"
        subprocess.run(['soffice', '--headless', '--convert-to', 'docx', '--outdir', os.path.dirname(temp_file_path), temp_file_path], check=True)

        # Read the .docx file
        text = read_word_docx(open(temp_docx_path, 'rb').read())

        # Clean up temporary files
        os.remove(temp_file_path)
        os.remove(temp_docx_path)

        return text
    except Exception as e:
        raise ValueError(f"Failed to read DOC: {str(e)}")

def read_word(file: bytes) -> str:
        if file.startswith(b'\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1'):
            return read_word_doc(file)

def read_txt(file_contents):
    try:
        text = file_contents.decode('utf-8')
        return text
    except Exception as e:
        raise ValueError(f"Failed to read TXT: {str(e)}")