# modal.py
import streamlit as st
import base64


def show_pdf(file_path: str, download_name: str = "resume.pdf"):

    """


    Display a PDF file in Streamlit with a close button and a download button.

    Args:
        file_path (str): Path to the local PDF file.
        download_name (str): Name of the file when downloaded.
       

    """
    # Read and encode the PDF file
    with open(file_path, "rb") as file:
        pdf_data = file.read()

    # Show PDF Preview only if the state is set
    if "show_pdf" not in st.session_state:
        st.session_state["show_pdf"] = True

    # Close & Download UI
    if st.session_state["show_pdf"]:
        col1, col2 = st.columns([15,1])  # Two buttons side-by-side

        # Close Button
        with col1:
            if st.button("✖ Close Resume", key="close"):
                st.session_state["show_pdf"] = False
                st.rerun()  # Rerun app to hide the iframe

        # Download Button
        with col2:
            # Streamlit's built-in download button
            if st.download_button(
                label="",
                icon = ":material/download:",
                data=pdf_data,
                file_name=download_name,
                mime="application/pdf",
            ):
                st.success("PDF download started!")

        # PDF Viewer Section
        st.markdown("### Resume Preview 📄")
        st.markdown(
            f"""
                    <div class="section-box">

            <iframe src="data:application/pdf;base64,{base64.b64encode(pdf_data).decode('utf-8')}" 
            width="100%" height="600px" style="border: none;"></iframe>
                    </div>

            """,
            unsafe_allow_html=True,
        )
