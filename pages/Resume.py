import streamlit as st

# Function to display a PDF from a URL
def display_pdf_from_url(pdf_url):
    pdf_display = f'<iframe src="{pdf_url}" width="900" height="1000" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

# Streamlit App
st.title("Resume")

# PDF hosted on a URL (replace with the actual URL of your PDF file)
pdf_url = "img\redes\shugavaneshwar_resume.pdf"
display_pdf_from_url(pdf_url)
