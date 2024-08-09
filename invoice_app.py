import re
from invoice_details import get_invoice
from utils import read_pdf, read_word_docx2txt, read_word_doc, read_txt
import easyocr
import streamlit as st
import pytesseract

# Specify the path to the Tesseract executable if necessary
pytesseract.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract'


reader = easyocr.Reader(['en'])

def main():
    st.title("Invoice Extraction App")
    file = st.file_uploader("Upload a single Invoice")
    
    if file is not None:
        try:
            contents = file.read()
            if file.name.endswith(".pdf"):
                invoice_text = read_pdf(contents)
            elif file.name.endswith(".docx"):
                invoice_text = read_word_docx2txt(contents)
            elif file.name.endswith(".txt"):
                invoice_text = read_txt(contents)
            elif file.name.endswith((".png", ".jpeg", ".jpg")):
                with open("temp_image", "wb") as temp_file:
                    temp_file.write(contents)
                result = reader.readtext("temp_image", detail=0)
                invoice_text = " ".join(result)
            else:
                st.error(f"Unsupported file type: {file.name}")
                return
            
            if st.button("Extract Invoice"):
                with st.spinner("Processing invoice..."):
                    invoice = get_invoice(invoice_text)
                    st.json(invoice)
            
        except Exception as e:
            st.error(f"There was an error processing the file {file.name}: {str(e)}")
            return
   
    else:
        st.write("No input provided. Please upload a file or provide text.")
        return

    

if __name__ == "__main__":
    main()
