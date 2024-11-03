import streamlit as st
from PIL import Image

def main():
    st.title("Methodology")
# Load and display the local image from the "images" folder
    image = Image.open('images/methodology.png')  # Ensure the image is in the correct directory
    st.image(image, use_column_width=True)

if __name__ == "__main__":
    main()
