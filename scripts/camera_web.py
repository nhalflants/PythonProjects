import streamlit as st
from grayscale_converter import convert_image

st.subheader("Color to Grayscale Converter")

# Create a file uploader component allowing the user to upload a file
uploaded_image = st.file_uploader("Upload Image")

with st.expander("Start Camera"):
    # Start the camera
    camera_image = st.camera_input("Camera")

if camera_image:
    gray_camera_image = convert_image(camera_image)
    # Render the grayscale image on the webpage
    st.image(gray_camera_image)

# Check if the image exists meaning the user has uploaded a file
if uploaded_image:
    gray_uploaded_image = convert_image(camera_image)
    st.image(gray_uploaded_image)