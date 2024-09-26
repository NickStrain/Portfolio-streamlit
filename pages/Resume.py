import streamlit as st

# Function to display a download button for the PDF
def display_pdf_download(pdf_file_path):
    with open(pdf_file_path, "rb") as pdf_file:
        pdf_bytes = pdf_file.read()

    st.download_button(
        label="Download PDF",
        data=pdf_bytes,
        file_name="resume.pdf",
        mime="application/pdf"
    )

# Streamlit App
st.title("Download Resume")

pdf_file_path = "img/redes/shugavaneshwar_resume.pdf"  # Ensure the file is in the correct path
display_pdf_download(pdf_file_path)
