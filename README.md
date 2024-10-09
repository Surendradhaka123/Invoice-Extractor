# Invoice Extraction App

The **Invoice Extraction App** is a Streamlit-based application that processes various types of invoice files (PDF, DOCX, TXT, and images) and extracts structured data, returning the output in a standardized JSON format. This app uses **Groq AI** for processing and extracting invoice details.

## Features

- Extracts key details such as **Customer Details**, **Products**, and **Total Amount** from invoices.
- Supports multiple file types, including PDF, DOCX, TXT, PNG, JPEG, and JPG.
- Leverages **Groq AI** and **easyOCR** for text extraction and processing.
- Outputs the invoice details in a valid JSON format that adheres to a defined schema.

## Technologies Used

- **Python**: Core language for the project.
- **Streamlit**: Web app framework for user interface.
- **Groq API**: Used for processing the extracted invoice text.
- **Pydantic**: Ensures data validation and type enforcement for structured output.
- **EasyOCR**: Used for reading text from image-based invoices.
- **File Handling**: Supports PDF, DOCX, TXT, and image files (PNG, JPEG, JPG).

## Live Demo
You can access the live Streamlit app here[https://invoice-extractor-hgkrz4zvsebeeuv9gtgbnk.streamlit.app].

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/invoice-extraction-app.git
   cd invoice-extraction-app
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up the **Groq API Key** in your Streamlit secrets. Add the following to `.streamlit/secrets.toml`:

   ```toml
   [api_key]
   key = "your-groq-api-key"
   ```

4. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

## Usage

1. Open the app in your browser (http://localhost:8501).
2. Upload an invoice in one of the supported formats: PDF, DOCX, TXT, PNG, JPEG, JPG.
3. Click on the **Extract Invoice** button.
4. The app will process the invoice and return the extracted details in JSON format.

### Example Output

```json
{
    "Customer_details": {
        "name": "John Doe",
        "address": "123 Invoice St, Invoice City"
    },
    "Products": [
        "Product A",
        "Product B"
    ],
    "Total_amount": 199.99
}
```

## Project Structure

```bash
.
├── app.py                 # Main application entry point
├── invoice_details.py      # Handles extraction logic and Groq API interaction
├── utils.py               # Contains helper functions for file reading
├── requirements.txt       # Required Python packages
└── README.md              # Project documentation
```

## File Type Support

- **PDF**: Extracts text using `read_pdf`.
- **DOCX**: Extracts text using `read_word_docx2txt`.
- **TXT**: Extracts text using `read_txt`.
- **Images (PNG, JPEG, JPG)**: Extracts text using `easyOCR`.

## Error Handling

If an unsupported file type is uploaded, or if there are any issues processing the invoice, an appropriate error message will be shown on the UI.

## Future Improvements

- Improve OCR accuracy for complex invoice images.
- Support additional file formats (e.g., CSV).
- Add advanced error handling for better user experience.
  
## Contributing

Feel free to open an issue or submit a pull request if you'd like to contribute to the project.
