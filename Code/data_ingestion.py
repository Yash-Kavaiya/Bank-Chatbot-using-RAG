import os
import sys
import time
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import google.generativeai as genai
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS

def load_pdf_files(directory):
    if not os.path.exists(directory):
        print(f"Error: The directory '{directory}' does not exist.")
        sys.exit(1)
    
    pdf_files = []
    for file in os.listdir(directory):
        if file.endswith(".pdf"):
            pdf_files.append(os.path.join(directory, file))
    return pdf_files

def pdffload(path):
    loader = PyPDFLoader(path)
    docs = loader.load()
    return docs

# Specify the directory where the PDF files are located
directory = "../Data"

# Measure the time for loading PDF files
start_time = time.time()
pdf_files = load_pdf_files(directory)
print(f"PDF files loaded: {pdf_files}")
load_time = time.time() - start_time
print(f"Time taken to load PDF files: {load_time:.2f} seconds")

# Load the PDF files
pdf_loader = []
for file in pdf_files:
    print(f"Loading file: {file}")
    pdf_loader.extend(pdffload(file))
    print(f"Total documents loaded: {len(pdf_loader)}")

# Split the documents into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
start_time = time.time()
splits = text_splitter.split_documents(pdf_loader)
split_time = time.time() - start_time
print(f"Documents split into {len(splits)} chunks")
print(f"Time taken to split documents: {split_time:.2f} seconds")

# Configure the Generative AI
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
model = genai.GenerativeModel('gemini-1.5-flash')
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

# Embed a query
start_time = time.time()
vector = embeddings.embed_query("hello, world!")
embed_query_time = time.time() - start_time
print(f"Query embedded: {vector}")
print(f"Time taken to embed query: {embed_query_time:.2f} seconds")

# Create the FAISS index
start_time = time.time()
db = FAISS.from_documents(splits, embeddings)
index_time = time.time() - start_time
print(f"FAISS index created with {db.index.ntotal} vectors")
print(f"Time taken to create FAISS index: {index_time:.2f} seconds")

# Perform a similarity search
query = "How can I login to Digital Lending Platform?"
retriever = db.as_retriever()
start_time = time.time()
docs = retriever.invoke(query)
search_time = time.time() - start_time
print(f"Documents retrieved: {docs}")
print(f"Time taken to retrieve documents: {search_time:.2f} seconds")

# Save and load the FAISS index
db.save_local("faiss_index")
new_db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
docs = new_db.similarity_search(query)
print(f"Retrieved document content: {docs[0].page_content}")
