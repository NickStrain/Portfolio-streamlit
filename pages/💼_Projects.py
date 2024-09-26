import streamlit as st

class Projects:
    def __init__(self, title, projects):
        self.title = title
        self.projects = projects

    def display(self):
        st.title(self.title) 
        col1, _, col2 = st.columns([1.5, 0.5, 1.5])
        col = col1
        for project, details in self.projects.items():
            with col:
                st.subheader(project)
                st.image(details["img"], caption=project, use_column_width=True)
                st.markdown("[Source code]({})".format(details["link"]))
            col = col2 if col == col1 else col1
        
projects = Projects("Proyectos", {
                "Neural Machine Translation for tamil": {"img": "img\proyectos\\neuralmachinetranslation.png", "link": "https://github.com/NickStrain/Machine-Translation.git"},
                "Image Captioning": {"img": "img\proyectos\imagecaption.png", "link": "https://github.com/NickStrain/Image-Captioning.git"},
                "image-segmentation-using-UNet": {"img": 'img\proyectos\\net.png', "link": "https://github.com/NickStrain/image-segmentation-using-UNet.git"},
                "Satellite-image-segmentation": {"img": "img\proyectos\image_seg.png", "link": "https://github.com/NickStrain/Satellite-image-segmentation.git"},
                "Tamil-Sentiment-Analysis": {"img": "img\proyectos\\tamilsent.png", "link": "https://github.com/NickStrain/Tamil-Sentiment-Analysis.git"},
                "Stock-market-prediction": {"img": "img\proyectos\stock.png", "link": "https://github.com/NickStrain/Stock-market-prediction.git"},
                })
projects.display()