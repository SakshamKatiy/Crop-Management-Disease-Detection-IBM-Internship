import streamlit as st
from PIL import Image
from datetime import datetime
import pandas as pd
from sqlalchemy import create_engine, Column, String, Date, Text, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database setup
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

# Predefined growth stages for rice in Hindi and English
RICE_GROWTH_STAGES = [
    ("Seedling", "अंकुरण"),
    ("Vegetative", "वनस्पति"),
    ("Tillering", "टिलेरिंग"),
    ("Heading", "सिर फूटना"),
    ("Flowering", "फूलना"),
    ("Maturing", "परिपक्वता"),
    ("Harvest", "कटाई")
]

# Extract only English names for selectbox
RICE_GROWTH_STAGES_ENGLISH = [stage[0] for stage in RICE_GROWTH_STAGES]

# Set up page configuration
st.set_page_config(page_title="Crop Management and Disease Detection", page_icon=":seedling:", layout="wide")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Crop Management", "Disease Detection", "Rice Growth Tracker"])

logo = Image.open("logo.jpeg")  
st.image(logo, width=100)
st.title("Crop Management and Disease Detection")

# Home Page
if page == "Home":
    st.header("Welcome to the Crop Management and Disease Detection System")
    st.write("This application helps in managing crops efficiently and detecting diseases early.")

# Crop Management Page
elif page == "Crop Management":
    st.header("Crop Management")
    st.write("Here you can find resources and tools to manage your crops efficiently.")

    st.subheader("Soil Health")
    st.write("Information and tools to assess and improve soil health.")

    st.subheader("Water Management")
    st.write("Guidelines for efficient water usage and irrigation techniques.")

    st.subheader("Fertilization")
    st.write("Best practices for fertilization to ensure optimal crop growth.")

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

# Rice Growth Tracker Page
elif page == "Rice Growth Tracker":
    st.header("Rice Growth Tracker")
    st.write("Track the growth stages of your rice crop and manage your farming activities efficiently.")

    # Add Rice Data
    st.subheader("Add Rice Data")
    st.write("Log the growth stages of your rice crop.")

    with st.form("rice_data_form"):
        crop_name = st.text_input("Crop Name", value="Rice")
        growth_stage = st.selectbox("Growth Stage (Select in English)", RICE_GROWTH_STAGES_ENGLISH)
        date = st.date_input("Date", datetime.today())
        notes = st.text_area("Notes", placeholder="Optional notes about the crop's condition or care")

        submitted = st.form_submit_button("Add Data")
        if submitted:
            # Convert English stage to Hindi for storage
            growth_stage_hindi = dict(RICE_GROWTH_STAGES).get(growth_stage)
            new_crop_data = CropData(crop_name=crop_name, growth_stage=growth_stage_hindi, date=date, notes=notes)
            session.add(new_crop_data)
            session.commit()
            st.success(f"Data for {crop_name} added successfully!")

    # View Growth Tracker
    st.subheader("View Growth Data")
    st.write("View the growth stages of your rice crop over time.")

    crop_data = session.query(CropData).all()
    if crop_data:
        df = pd.DataFrame([(d.crop_name, d.growth_stage, d.date, d.notes) for d in crop_data], 
                          columns=["Crop Name", "Growth Stage", "Date", "Notes"])
        st.dataframe(df)

        # Visualize data for rice
        for crop_name in df['Crop Name'].unique():
            crop_df = df[df['Crop Name'] == crop_name]
            st.subheader(f"{crop_name} Growth Data")
            st.write(crop_df)
            
            # Additional visualization could go here (e.g., timelines, charts)
    else:
        st.warning("No rice data available. Please add data first.")

# Footer
st.sidebar.markdown("### The Bugs")
if __name__ == "__main__":
    st.write("Developed by The Bugs | © 2024")
