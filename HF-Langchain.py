from streamlit import st


def main():
    st.title('I will answer your question from your\'s PDF')
    st.text_input('Ask me anythings!!!:)')
    
    with st.sidebar:
        st.subHeader('Your\'s Datasource(PDF)')
        st.file_uploader('Upload your documents(PDF) here & tab the "Process"')
        st.button('Process')
        
if __name__ == '__main__':
    main()
