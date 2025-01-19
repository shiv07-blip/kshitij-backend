import os
import random
import string
from flask import Flask, request, jsonify, send_file
from fpdf import FPDF

app = Flask(__name__)

# Configure upload folder
app.config['UPLOAD_FOLDER'] = './uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Helper function to generate random filenames
def generate_random_filename(filename):
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    ext = os.path.splitext(filename)[1]  # Extract file extension
    return f"{random_string}{ext}"

# Endpoint to handle form submission and PDF generation
@app.route('/submit-data', methods=['POST'])
def submit_data():
    try:
        # Initialize response data
        response_data = {}
        fields = ['productName', 'size', 'specification', 'quantity', 'unit', 'productComments', 'selectedVendor']

        # Process form fields
        form_data = {field: request.form.get(field, '') for field in fields}
        response_data['form_data'] = form_data

        # Process file uploads
        uploaded_files = []
        for file_key in request.files.keys():
            file = request.files[file_key]
            if file:
                # Rename the file with a random name
                new_filename = generate_random_filename(file.filename)
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], new_filename)
                file.save(filepath)

                # Add to the uploaded files list
                uploaded_files.append({"original_name": file.filename, "saved_as": new_filename})

        response_data['uploaded_files'] = uploaded_files

        # Generate PDF
        pdf_filename = generate_pdf(form_data, uploaded_files)

        return jsonify({
            "message": "Data processed successfully and PDF generated.",
            "pdf_filename": pdf_filename,
            "uploaded_files": uploaded_files
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Helper function to generate PDF
def generate_pdf(form_data, uploaded_files):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Add a heading
    pdf.set_font("Arial", style="B", size=14)
    pdf.cell(200, 10, txt="Product Details Submission", ln=True, align='C')
    pdf.ln(10)

    # Add table-like structure for form fields
    pdf.set_font("Arial", size=12)
    pdf.cell(60, 10, txt="Field", border=1, align='C')
    pdf.cell(130, 10, txt="Value", border=1, align='C')
    pdf.ln()
    for key, value in form_data.items():
        pdf.cell(60, 10, txt=key, border=1)
        pdf.cell(130, 10, txt=value, border=1)
        pdf.ln()

    # Add table for uploaded files
    pdf.ln(10)
    pdf.cell(60, 10, txt="Uploaded Files", border=1, align='C')
    pdf.cell(130, 10, txt="Saved As", border=1, align='C')
    pdf.ln()
    for file in uploaded_files:
        pdf.cell(60, 10, txt=file["original_name"], border=1)
        pdf.cell(130, 10, txt=file["saved_as"], border=1)
        pdf.ln()

    # Save PDF to the server
    pdf_filename = "product_submission.pdf"
    pdf_filepath = os.path.join(app.config['UPLOAD_FOLDER'], pdf_filename)
    pdf.output(pdf_filepath)

    return pdf_filename

if __name__ == '__main__':
    app.run(debug=True)
