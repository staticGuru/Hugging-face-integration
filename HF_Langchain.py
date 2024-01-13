import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings, HuggingFaceInstructEmbeddings
from langchain.vectorstores import faiss
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain.llms.huggingface_hub import HuggingFaceHub
from frontend import css, bot_template, user_template

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
    
def get_vectorstore(text_chuncks):
    # embeddings=OpenAIEmbeddings() #for compatibility for Openai
    model_name = "hkunlp/instructor-large"
    model_kwargs = {'device': 'cpu'}
    encode_kwargs = {'normalize_embeddings': True}
    embeddings=HuggingFaceInstructEmbeddings(
    model_name=model_name,
    model_kwargs=model_kwargs,
    encode_kwargs=encode_kwargs
    )
    vectorstore=faiss.FAISS.from_texts(texts=text_chuncks,embedding=embeddings)
    return vectorstore   

def get_conversation_chain(vectorstore):
    # llm=ChatOpenAI()
    llm=HuggingFaceHub(repo_id="google/flan-t5-xxl",model_kwargs={'temperature':0.5, 'max_length':512})
    memory=ConversationBufferMemory(memory_key='chat_history',return_messages=True)
    conversation_chain= ConversationalRetrievalChain.from_llm(llm=llm,retriever=vectorstore.as_retriever(),memory=memory)
    return conversation_chain

def handle_question(user_question):
    response=st.session_state.conversation({'question':user_question})
    st.session_state.chat_history = response['chat_history']

    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)
    
    
def PDFbot():
    load_dotenv()
    
    if "conversation" not in st.session_state:
        st.session_state.conversation= None
    
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None
            
    st.title('I will answer your question from your\'s PDF')
    user_question=st.text_input('Ask me anythings!!!:')
    if user_question:
        handle_question(user_question)
    
    with st.sidebar:
        st.subheader('Your\'s Datasource(PDF)')
        pdf_docs= st.file_uploader('Upload your documents(PDF) here & tab the "Process"',accept_multiple_files=True)
        if st.button('Process'):
            with st.spinner('Processing...'):
                #get pdf text
                raw_text=get_pdf_content(pdf_docs)
                
                #get the text chuncks
                text_chuncks=get_text_chunks(raw_text)
                
                #create the vector store 
                vectorstore= get_vectorstore(text_chuncks)
                
                #create the conversation chain
                st.session_state.conversation= get_conversation_chain(vectorstore)  #it may change in every render, so, to stop it we use session_state
                
