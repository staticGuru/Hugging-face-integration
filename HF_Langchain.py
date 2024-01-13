import streamlit as st
from dotenv import load_dotenv

def PDFbot():
    load_dotenv()
    st.title('I will answer your question from your\'s PDF')
    st.text_input('Ask me anythings!!!:)')
    
    with st.sidebar:
        st.subheader('Your\'s Datasource(PDF)')
        pdf_docs= st.file_uploader('Upload your documents(PDF) here & tab the "Process"',accept_multiple_files=True)
        st.button('Process')

