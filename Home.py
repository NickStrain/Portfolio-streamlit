import streamlit as st

class AboutMe:
    def __init__(self, title, about, img):
        self.title = title
        self.about = about
        self.img = img

    def display(self):
        col1, col2 = st.columns(2)
        with col1:
            st.title(self.title)
            st.info(self.about)
            
            st.write('<a href="https://github.com/aalvaropc">💻 Github</a>', unsafe_allow_html=True)
            st.write('<a href="https://www.linkedin.com/in/aalvarop-pe/">🔗 LinkedIn</a>', unsafe_allow_html=True)
            st.write('<a href="mailto:aalvaropc@gmail.com">📨 Gmail</a>', unsafe_allow_html=True)
        with col2:
            st.image(self.img, width=560)
            
descripcion = """
I am deeply passionate about machine learning and deep learning. My interest in these areas began with my fascination for how machines could learn patterns from data and make decisions, mirroring human cognitive abilities. Over the years, I have immersed myself in understanding algorithms, from simple linear models to complex neural networks. I am particularly drawn to the potential of deep learning, with its ability to solve complex problems in image recognition, natural language processing, and beyond. Through personal projects, contributing to open-source communities, and leading machine learning initiatives in my college, I have honed my skills in building intelligent models. I am excited by the possibility of leveraging these technologies to tackle real-world problems and contribute to the advancement of AI.
"""
about = AboutMe("Shugavaneshwar ", descripcion, "img/profile/alvaro.jpg")
about.display()