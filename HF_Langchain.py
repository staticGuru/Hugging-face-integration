import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader


def get_pdf_content(pdf_docs):
    text=""
    for pdf in pdf_docs:
        pdf_reader= PdfReader(pdf)
        for page in Pdf_reader.pages():
            text=text+page.extractText()
    return text


def PDFbot():
    load_dotenv()
    st.title('I will answer your question from your\'s PDF')
    st.text_input('Ask me anythings!!!:)')
    
    with st.sidebar:
        st.subheader('Your\'s Datasource(PDF)')
        pdf_docs= st.file_uploader('Upload your documents(PDF) here & tab the "Process"',accept_multiple_files=True)
        if st.button('Process'):
            with st.spinner('Processing...'):
                raw_text=get_pdf_content(pdf_docs)
                #get pdf text
                
                
                #get the text chuncks
                
                
                #create the vector store 

