import streamlit as st
from PIL import Image
from datetime import datetime
import pandas as pd
from sqlalchemy import create_engine, Column, String, Date, Text, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///crop_management.db')
Base = declarative_base()

class CropData(Base):
    __tablename__ = 'crop_data'
    id = Column(Integer, primary_key=True, autoincrement=True)
    crop_name = Column(String)
    growth_stage = Column(String)
    date = Column(Date)
    notes = Column(Text)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

st.set_page_config(page_title="Crop Disease Detection", page_icon=":seedling:", layout="wide")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Disease Detection"])

logo = Image.open("logo.jpeg")  
st.image(logo, width=100)
st.title("Crop Disease Detection")

# Home Page
if page == "Home":
    st.header("Welcome to the Crop Disease Detection System")
    st.write("This application helps in detecting diseases early.")

# Disease Detection Page
elif page == "Disease Detection":
    st.header("Disease Detection")
    st.write("Upload an image of the crop to detect potential diseases.")

    uploaded_file = st.file_uploader("Choose an image...", type="jpg")

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image.', use_column_width=True)
        st.write("")
        st.write("Classifying...")

        st.success("The crop appears to be healthy!")

# Footer
st.sidebar.markdown("### The Bugs")
if __name__ == "__main__":
    st.write("Developed by The Bugs | © 2024")
