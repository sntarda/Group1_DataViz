import streamlit as st
from pdf2image import convert_from_path
import os

def main(st, iframe_style):
    st.title('PDF Viewer App')

    # Path to your PDF file
    pdf_file = 'example.pdf'

    if os.path.exists(pdf_file):
        # Convert PDF to list of images
        images = convert_from_path(pdf_file, 200)  # 200 dpi

        # Display images
        for i, image in enumerate(images):
            st.image(image, caption=f'Page {i+1}')
    else:
        st.error("File not found!")

if __name__ == "__main__":
    main()
