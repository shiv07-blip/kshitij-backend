# Flask Project: Product Details Submission

This Flask application allows users to submit product details via a form and upload associated files. The submitted data and uploaded files are processed, and a PDF summarizing the details is generated.

---

## Features

1. **Form Data Submission**: Accepts product details via a form.
2. **File Uploads**: Handles file uploads and renames them with random filenames to avoid conflicts.
3. **PDF Generation**: Creates a PDF summarizing the submitted data and uploaded files.
4. **File Management**: Saves uploaded files and generated PDF in a dedicated directory.

---

## Project Structure

```
.
|-- app.py                # Main Flask application
|-- uploads/              # Directory to store uploaded files and generated PDFs
```

---

## Endpoints

### `/submit-data` (POST)
Processes form data and file uploads, then generates a PDF with the submitted details.

- **Request Parameters**:
  - Form Fields:
    - `productName`
    - `size`
    - `specification`
    - `quantity`
    - `unit`
    - `productComments`
    - `selectedVendor`
  - Files:
    - Accepts file uploads with dynamic keys.

- **Response**:
  - `message`: Status message.
  - `pdf_filename`: Name of the generated PDF file.
  - `uploaded_files`: List of uploaded files with their original and saved filenames.

---

## Prerequisites

1. Python 3.7 or higher
2. Virtual environment (optional but recommended)

---

## Installation

1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd <repository-folder>
    ```

2. Create a virtual environment (optional):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install flask fpdf
    ```

4. Create the `uploads` directory:
    ```bash
    mkdir uploads
    ```

---

## Running the Application

1. Start the Flask server:
    ```bash
    python app.py
    ```

2. Access the application at:
    ```
    http://127.0.0.1:5000
    ```

---

## Example Request

### cURL Example

```bash
curl -X POST http://127.0.0.1:5000/submit-data \
  -F "productName=Widget" \
  -F "size=Large" \
  -F "specification=High Quality" \
  -F "quantity=10" \
  -F "unit=pcs" \
  -F "productComments=Urgent order" \
  -F "selectedVendor=Vendor123" \
  -F "file1=@path/to/file1.txt" \
  -F "file2=@path/to/file2.png"
```

---

## Notes

- Uploaded files and the generated PDF will be saved in the `uploads` directory.
- Make sure the `uploads` folder has proper write permissions.
- Use the Flask `debug=True` mode for development but disable it in production.

---

## Dependencies

- Flask
- fpdf

Install all dependencies using:
```bash
pip install -r requirements.txt
```

To create a `requirements.txt` file:
```bash
pip freeze > requirements.txt
```

---

## License

This project is licensed under the MIT License. Feel free to use and modify it as needed.
