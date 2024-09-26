import streamlit as st

# Streamlit App
st.title("Download Resume")

# PDF hosted URL (replace with your actual URL)
pdf_url = "img/redes/shugavaneshwar_resume.pdf"  # Update with your PDF URL

# Button to download the PDF
st.download_button(
    label="Download Resume",
    data=pdf_url,
    file_name="your_resume.pdf",  # Set the filename for the downloaded file
    mime="application/pdf"  # Set the MIME type for PDF
)
