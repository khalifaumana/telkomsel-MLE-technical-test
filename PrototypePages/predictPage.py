import streamlit as st
from PIL import Image
from PrototypePages.classify import machine_classification

def app():
    st.divider()
    st.subheader("Classficiation page")

    uploaded_file = st.file_uploader("Choose an image ...", type="jpg")

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Image Uploaded', use_column_width=True)
        st.write("")
        st.write("Classifying...")
        label_index = machine_classification(image, 'image_classifier.h5')
        
        label_list = ['Architecure', 'Art and Culture', 'Food and Drinks', 'Travel and Adventure']
        
        st.write(label_list[label_index])