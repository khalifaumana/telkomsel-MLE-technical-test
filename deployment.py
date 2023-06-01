import os
import streamlit as st
import numpy as np
from PIL import  Image

from multipage import MultiPage
from PrototypePages import predictPage, about

app = MultiPage()


st.title("Image categorization")
st.text("This prototype is to simulate the on-demand process to categorize an image")


app.add_page("Classification ", predictPage.app)
app.add_page("About", about.app)

app.run()