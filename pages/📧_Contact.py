import streamlit as st

# Function to display contact details
def contact_page():
    st.title("Contact")

    st.write("Feel free to reach out to me through any of the following channels:")

    # Display your contact information
    st.subheader("Contact Information")
    st.write("📞 **Phone**: +91-7397191107")
    st.write("📧 **Email**: shugavaneshwar13@gmail.com")
    st.write("🔗 **LinkedIn**: [LinkedIn Profile](https://www.linkedin.com/in/shuga-vaneshwar-922603226/)")

    # You can add more social media links or information here
    st.write("💼 **GitHub**: [GitHub Profile](https://github.com/NickStrain)")
    st.write("📍 **Location**: Chennai, India")

# Streamlit App
if __name__ == "__main__":
    contact_page()
