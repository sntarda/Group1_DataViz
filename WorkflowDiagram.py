import streamlit as st

def main():
    st.title('PDF Viewer App')

    # File uploader allows user to add file
    uploaded_file = st.file_uploader("Choose a file")

    if uploaded_file is not None:
        # To read file as bytes:
        bytes_data = uploaded_file.getvalue()
        st.write("Filename:", uploaded_file.name)

        # Use the download button to download the PDF
        st.download_button(
            label="Download PDF",
            data=bytes_data,
            file_name=uploaded_file.name,
            mime='application/octet-stream'
        )

        # If you have an external URL and want to embed the PDF, you can use this code:
        # pdf_url = "https://www.example.com/your-pdf.pdf"
        # st.markdown(f'<iframe src="{pdf_url}" width="700" height="1000" type="application/pdf"></iframe>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
