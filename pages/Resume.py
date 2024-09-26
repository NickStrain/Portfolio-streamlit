import streamlit as st

# Function to read the PDF file
def load_pdf(pdf_file_path):
    with open(pdf_file_path, "rb") as f:
        return f.read()

# Streamlit App
st.title("Download Resume")

# Path to your PDF file (ensure it's in the correct location)
pdf_file_path = "img/redes/shugavaneshwar_resume.pdf"  # Replace with your local PDF path

# Load the PDF content
pdf_data = load_pdf(pdf_file_path)

# Button to download the PDF
st.download_button(
    label="Download Resume",
    data=pdf_data,
    file_name="your_resume.pdf",
    mime="application/pdf"
)
