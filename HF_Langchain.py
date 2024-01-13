import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter


def get_pdf_content(pdf_docs):
    text=""
    for pdf in pdf_docs:
        pdf_reader= PdfReader(pdf)
        for page in pdf_reader.pages:
            text=text+page.extract_text()
    return text

def get_text_chunks(raw_text):
    text_splitter=CharacterTextSplitter(
      separator='\n',
      chunk_overlap=200,
      chunk_size=1000,
      length_function=len  
    )
    chunks=text_splitter.split_text(raw_text)
    return chunks
    
    

def PDFbot():
    load_dotenv()
    st.title('I will answer your question from your\'s PDF')
    st.text_input('Ask me anythings!!!:)')
    
    with st.sidebar:
        st.subheader('Your\'s Datasource(PDF)')
        pdf_docs= st.file_uploader('Upload your documents(PDF) here & tab the "Process"',accept_multiple_files=True)
        if st.button('Process'):
            with st.spinner('Processing...'):
                #get pdf text
                raw_text=get_pdf_content(pdf_docs)
                
                #get the text chuncks
                text_chuncks=get_text_chunks(raw_text)
                st.write(text_chuncks)
                
                #create the vector store 

