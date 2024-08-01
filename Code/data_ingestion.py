import os
import sys
from langchain_community.document_loaders import PyPDFLoader

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

# Call the function to load the PDF files
pdf_files = load_pdf_files(directory)
pdf_loader = []

# Print the list of PDF files and load them
for file in pdf_files:
    print(file)
    pdf_loader.extend(pdffload(file))
    print(len(pdf_loader))

########################################################################################################

from langchain_text_splitters import RecursiveCharacterTextSplitter
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splits = text_splitter.split_documents(pdf_loader)
print(splits)
print(len(splits))

