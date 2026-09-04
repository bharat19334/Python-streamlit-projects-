import streamlit as st
from PyPDF2 import PdfMerger
import io

st.set_page_config(page_title="PDF Merger", page_icon="📄")

st.title("📄 PDF Merger App")

uploaded_files = st.file_uploader(
    "Upload PDF files",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:
    st.write(f"{len(uploaded_files)} PDFs selected")

    if st.button("Merge PDFs"):
        merger = PdfMerger()

        for pdf in uploaded_files:
            merger.append(pdf)

        output = io.BytesIO()
        merger.write(output)
        merger.close()

        output.seek(0)

        st.success("PDFs merged successfully!")

        st.download_button(
            label="Download Merged PDF",
            data=output.getvalue(),
            file_name="merged_pdf.pdf",
            mime="application/pdf"
        )