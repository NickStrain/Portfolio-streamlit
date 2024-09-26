import streamlit as st
import base64

# Function to display the PDF
def display_pdf(pdf_file):
    with open(pdf_file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="900" height="1000" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

# Streamlit App
st.title("Resume")

pdf_file_path = "img/redes/shugavaneshwar_resume.pdf"  # Replace with your PDF file path
display_pdf(pdf_file_path)
