from fpdf import FPDF

# Create a PDF object
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Set title
pdf.set_font("Arial", size=16, style='B')
pdf.cell(200, 10, txt="Test Answers", ln=True, align="C")

# Set content
pdf.ln(10)  # Line break
pdf.set_font("Arial", size=12)

# Define the array of answers
answers = [
    'c', 'a', 'a', 'b', 'b', 'b', 'c', 'a', 'b', 'c',
    'a', 'c', 'b', 'b', 'c', 'b', 'c', 'a', 'c', 'b',
    'c', 'a', 'c', 'b', 'b', 'c', 'c', 'b', 'a', 'a',
    'b', 'd', 'c', 'c', 'b', 'a', 'c', 'b', 'b', 'a',
    'c', 'c', 'c', 'b', 'b', 'c', 'a', 'd', 'b', 'a'
]

# Write answers to the PDF
for idx, answer in enumerate(answers, 1):
    pdf.cell(200, 10, txt=f"Question {idx}: Answer: {answer}", ln=True)

# Output PDF
output_path = r"C:\Users\Beboy\Desktop\ddos\output.pdf"



pdf.output(output_path)

output_path
