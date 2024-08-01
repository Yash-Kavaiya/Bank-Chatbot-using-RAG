import streamlit as st
import google.generativeai as genai
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS

# Configure the Generative AI API
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

# Load the FAISS index
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
new_db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)

def get_answer(query):
    docs = new_db.similarity_search(query)
    return docs[0].page_content if docs else "No relevant documents found."

# Custom CSS for Bank of Baroda theme
st.markdown("""
    <style>
        :root {
            --primary-color: #ea4335;
            --secondary-color: #fbbc04;
            --tertiary-color: #34a853;
            --quaternary-color: #4285f4;
            --light-background: #e8eaed;
            --dark-background: #202124;
            --text-light: #202124;
            --text-dark: #e8eaed;
        }

        /* Light Mode */
        .light-mode {
            background-color: var(--light-background);
            color: var(--text-light);
        }

        /* Dark Mode */
        .dark-mode {
            background-color: var(--dark-background);
            color: var(--text-dark);
        }

        /* Buttons */
        .stButton>button {
            background-color: var(--primary-color);
            color: white;
        }

        /* Input Field */
        .stTextInput>div>div>input {
            background-color: var(--light-background);
            color: var(--text-light);
        }

        /* Titles */
        h1, h2, h3, h4, h5, h6 {
            color: var(--primary-color);
        }
    </style>
    """, unsafe_allow_html=True)

# Apply theme mode based on Streamlit's theme
theme_mode = "light-mode" if st.get_option("theme.base") == "light" else "dark-mode"
st.markdown(f'<div class="{theme_mode}">', unsafe_allow_html=True)

# Streamlit app
st.title("Bank of Baroda Q&A System")

# Description
st.write("""
## Description
Welcome to the Bank of Baroda Q&A System. This application leverages advanced AI to answer your queries about the Bank of Baroda services by searching through relevant documents.
""")

# Features
st.write("""
## Features
- **Document Search:** Efficiently searches through a collection of documents to find relevant information.
- **Generative AI:** Utilizes state-of-the-art generative AI models to provide accurate and concise answers.
- **Easy to Use:** Simply enter your query and get instant answers.
- **Dynamic Theme:** Adapts to both light and dark modes for better user experience.
""")

# Use Cases
st.write("""
## Use Cases
- **Customer Support:** Quickly find answers to common banking questions.
- **Employee Assistance:** Help bank employees find information about procedures and policies.
- **General Inquiry:** Provide customers with quick answers to their queries about banking services.
""")

# User input
st.write("## Ask a Question")
query = st.text_input("Enter your query:", "How can I login to Digital Lending Platform?")

# Display the result
if st.button("Get Answer"):
    with st.spinner("Searching..."):
        answer = get_answer(query)
    st.write("### Answer:")
    st.write(answer)

# Close the themed div
st.markdown("</div>", unsafe_allow_html=True)
