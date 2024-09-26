import streamlit as st

# Function to display PDF from URL
def display_pdf_from_url(pdf_url):
    pdf_display = f'<iframe src="{pdf_url}" width="900" height="1000" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

# Streamlit App
st.title("Resume")

# PDF hosted URL (replace with your actual URL)
pdf_url = "https://github.com/NickStrain/Portfolio-streamlit/blob/main/img/redes/shugavaneshwar_resume.pdf"  # Update with your PDF URL
display_pdf_from_url(pdf_url)
