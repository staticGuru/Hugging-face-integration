import os
# from apikey import apikey
from dotenv import load_dotenv
from HF_Langchain import PDFbot

import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.memory import ConversationBufferMemory
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import WikipediaQueryRun

load_dotenv()

# # os.environ['OPENAI_API_KEY'] = os.getenv("API_KEY")

# #App framework
# st.title("First GPT creations")
# prompt=st.text_input("Enter your prompt name");

# title_template = PromptTemplate(
#     input_variables=['topic'],
#     template='write me a blog post title about {topic}'
# )
# script_template = PromptTemplate(
#     input_variables=['title','wikipedia_research'],
#     template='write me a blog post based on the given title TITTLE:{title} and while leveraging this wikipedia research: {wikipedia_research}'
# )

# #Memory
# title_memory= ConversationBufferMemory(input_key='topic', memory_key='chat_history')
# script_memory= ConversationBufferMemory(input_key='title', memory_key='chat_history')


#  #load the LLMS
# llm =OpenAI(temperature=0.9)
# title_chain=LLMChain(llm=llm,prompt=title_template,verbose=True,output_key='title',memory=title_memory)
# script_chain=LLMChain(llm=llm,prompt=script_template,verbose=True,output_key='script',memory=script_memory)

# # sequential_chain=SequentialChain(chains=[title_chain,script_chain],input_variables=['topic'],output_variables=['topic','script'],verbos=True)

# wiki= WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper());

# #Render the output
# if prompt:
#     # response = sequential_chain({'topic':prompt})
#     title=title_chain.run(prompt)
#     wiki_research= wiki.run(prompt)
#     script=script_chain.run(title=title,wikipedia_research=wiki_research)
#     st.write(title)
#     st.write(script)
    
    
#     with st.expander('Title History'):
#         st.info(title_memory.buffer)
        
#     with st.expander('Script History'):
#         st.info(script_memory.buffer)
        
#     with st.expander('Wikipedia Research'):
#         st.info(wiki_research)
        

if __name__ == "__main__":
    PDFbot()        