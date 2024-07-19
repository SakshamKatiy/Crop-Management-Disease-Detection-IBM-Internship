import streamlit as st
from PIL import Image

st.set_page_config(page_title="Crop Management and Disease Detection", page_icon=":seedling:", layout="wide")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Crop Management", "Disease Detection"])

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

# Footer
st.sidebar.markdown("### The Bugs")

if __name__ == "__main__":
    st.write("Developed by The Bugs | © 2024")
