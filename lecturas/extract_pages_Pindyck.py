import PyPDF2

# Path to the PDF file
input_pdf_path = 'Microeconomía-Pindyck.pdf'
output_pdf_path = 'Pindyck -- Oferta y Demanda CH2.pdf'

# Create a PDF reader object
with open(input_pdf_path, 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    
    # Create a PDF writer object
    writer = PyPDF2.PdfWriter()

    # Extract pages 8, 9, and 10 (note that indexing starts at 0)
    pages_to_extract = list(range(50, 90))
    for page_number in pages_to_extract:
        writer.add_page(reader.pages[page_number])

    # Write the extracted pages to a new PDF
    with open(output_pdf_path, 'wb') as output_file:
        writer.write(output_file)

print(f'Extracted pages {pages_to_extract} to {output_pdf_path}')
