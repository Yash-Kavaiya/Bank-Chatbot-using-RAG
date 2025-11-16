# Bank Chatbot using RAG (Retrieval-Augmented Generation)

A sophisticated AI-powered Question & Answer system for Bank of Baroda that leverages Retrieval-Augmented Generation (RAG) to provide accurate answers to banking-related queries by searching through official bank documents.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Data Sources](#data-sources)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project implements an intelligent chatbot for Bank of Baroda that uses Retrieval-Augmented Generation (RAG) to answer customer queries. The system ingests banking-related PDF documents, creates vector embeddings, and uses semantic search to retrieve relevant information, providing accurate and contextual responses to user questions.

### What is RAG?

RAG (Retrieval-Augmented Generation) is an AI framework that combines:
- **Retrieval**: Finding relevant information from a knowledge base
- **Generation**: Using AI to generate contextual answers based on retrieved information

This approach ensures that the chatbot provides accurate, up-to-date information directly from official bank documents rather than relying solely on pre-trained model knowledge.

## Features

- **Intelligent Document Search**: Efficiently searches through banking documents using semantic search
- **Vector-Based Retrieval**: Uses FAISS (Facebook AI Similarity Search) for fast and accurate similarity search
- **Generative AI Integration**: Powered by Google's Gemini AI for embeddings
- **User-Friendly Interface**: Built with Streamlit for an intuitive web interface
- **Dynamic Theming**: Supports both light and dark modes
- **Real-time Responses**: Instant answers to banking queries
- **PDF Processing**: Automatically processes and indexes multiple PDF documents
- **Persistent Index**: Saves vector database locally for quick subsequent queries
- **Performance Metrics**: Tracks processing times for optimization

## Architecture

```
┌─────────────────┐
│   PDF Documents │
└────────┬────────┘
         │
         ▼
┌─────────────────────────┐
│  Document Ingestion     │
│  - Load PDFs            │
│  - Text Splitting       │
│  - Chunk Creation       │
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│  Embedding Generation   │
│  (Google Gemini API)    │
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│  FAISS Vector Store     │
│  - Index Creation       │
│  - Similarity Search    │
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│  Streamlit Interface    │
│  - Query Input          │
│  - Answer Display       │
└─────────────────────────┘
```

## Technology Stack

### Core Technologies
- **Python 3.x**: Primary programming language
- **LangChain**: Framework for building LLM-powered applications
- **FAISS**: Vector database for similarity search
- **Google Generative AI (Gemini)**: Embedding model and AI capabilities
- **Streamlit**: Web application framework for the user interface

### Key Libraries
- `langchain-community`: Community integrations for LangChain
- `langchain-google-genai`: Google Generative AI integration
- `pypdf`: PDF document processing
- `google-generativeai`: Google AI SDK
- `streamlit`: Interactive web UI

## Project Structure

```
Bank-Chatbot-using-RAG/
│
├── Code/
│   ├── data_ingestion.py      # PDF processing and index creation
│   ├── QandA.py                # Streamlit Q&A interface
│   └── faiss_index/            # Stored vector database
│       ├── index.faiss         # FAISS index file
│       └── index.pkl           # Serialized index metadata
│
├── Data/                       # Source PDF documents
│   ├── BRSD-Manual-Final-08-12.pdf
│   ├── FAQ-and-Dos-Donts-for-Digital-Loans.pdf
│   ├── UK.pdf
│   └── corporate-performance-q3fy24-21feb2024-22-14.pdf
│
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

## Installation

### Prerequisites
- Python 3.8 or higher
- Google API Key for Generative AI
- pip (Python package manager)

### Step-by-Step Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/Bank-Chatbot-using-RAG.git
   cd Bank-Chatbot-using-RAG
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv

   # On Windows
   venv\Scripts\activate

   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install required dependencies**
   ```bash
   pip install pypdf langchain_community langchain-google-genai streamlit faiss-cpu
   ```

   Or install from requirements.txt:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up Google API Key**

   Obtain a Google API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

   Set the environment variable:
   ```bash
   # On Windows
   set GOOGLE_API_KEY=your_api_key_here

   # On macOS/Linux
   export GOOGLE_API_KEY=your_api_key_here
   ```

   Or create a `.env` file:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

## Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GOOGLE_API_KEY` | Google Generative AI API key | Yes |

### Document Configuration

To add new documents:
1. Place PDF files in the `Data/` directory
2. Run the data ingestion script to rebuild the index

### Embedding Model Configuration

The project uses Google's `models/embedding-001` by default. To change:
- Edit `Code/data_ingestion.py` line 54
- Edit `Code/QandA.py` line 11

## Usage

### Step 1: Data Ingestion (First Time Setup)

Navigate to the Code directory and run the data ingestion script:

```bash
cd Code
python data_ingestion.py
```

This will:
- Load all PDF files from the `Data/` directory
- Split documents into manageable chunks
- Generate embeddings using Google's Gemini AI
- Create and save a FAISS index

**Expected Output:**
```
PDF files loaded: ['../Data/BRSD-Manual-Final-08-12.pdf', ...]
Loading file: ../Data/BRSD-Manual-Final-08-12.pdf
Total documents loaded: X
Documents split into Y chunks
Time taken to split documents: Z seconds
FAISS index created with N vectors
```

### Step 2: Launch the Q&A Interface

Run the Streamlit application:

```bash
streamlit run QandA.py
```

The application will open in your default web browser at `http://localhost:8501`

### Step 3: Ask Questions

1. Enter your banking-related query in the text input field
2. Click "Get Answer"
3. The system will retrieve the most relevant information from the document database
4. View the answer displayed on the screen

### Example Queries

- "How can I login to Digital Lending Platform?"
- "What are the dos and don'ts for digital loans?"
- "What is the corporate performance for Q3 FY24?"
- "What are the requirements for opening a bank account?"

## How It Works

### 1. Document Processing
- **PDF Loading**: The system loads PDF files using PyPDFLoader
- **Text Splitting**: Documents are split into chunks of 1000 characters with 200-character overlap using RecursiveCharacterTextSplitter
- **Chunking Strategy**: Overlap ensures context is maintained across chunk boundaries

### 2. Embedding Generation
- Each text chunk is converted into a vector embedding using Google's `embedding-001` model
- Embeddings capture semantic meaning of the text
- Dimension: 768-dimensional vectors

### 3. Vector Storage
- FAISS (Facebook AI Similarity Search) indexes all embeddings
- Enables fast similarity search across thousands of document chunks
- Index is saved locally for persistence

### 4. Query Processing
- User query is converted to an embedding using the same model
- FAISS performs similarity search to find most relevant chunks
- Top matching chunks are retrieved based on cosine similarity

### 5. Answer Retrieval
- The most relevant document chunk is returned as the answer
- System provides direct excerpts from official bank documents

## Data Sources

The chatbot is trained on the following Bank of Baroda documents:

1. **BRSD-Manual-Final-08-12.pdf**: Banking regulations and service delivery manual
2. **FAQ-and-Dos-Donts-for-Digital-Loans.pdf**: Digital lending guidelines and FAQs
3. **UK.pdf**: Banking documentation
4. **corporate-performance-q3fy24-21feb2024-22-14.pdf**: Corporate performance report

### Adding New Documents

To add new knowledge sources:
1. Place PDF files in the `Data/` directory
2. Re-run the data ingestion script:
   ```bash
   cd Code
   python data_ingestion.py
   ```
3. The system will rebuild the index with all documents

## Performance Metrics

The system tracks performance for optimization:

- **PDF Loading Time**: Time to load documents
- **Document Splitting Time**: Time to chunk documents
- **Embedding Generation Time**: Time to create vector embeddings
- **Index Creation Time**: Time to build FAISS index
- **Query Response Time**: Time to retrieve relevant documents

## Future Enhancements

### Planned Features
- [ ] **Conversational AI**: Integrate with Gemini for generating natural language responses
- [ ] **Multi-turn Conversations**: Support follow-up questions with context
- [ ] **Query History**: Save and display previous queries
- [ ] **Answer Sources**: Show which document the answer came from
- [ ] **Advanced Filtering**: Filter by document type, date, or category
- [ ] **Multi-language Support**: Support for regional Indian languages
- [ ] **Voice Interface**: Add speech-to-text for voice queries
- [ ] **Admin Dashboard**: Monitor usage, popular queries, and performance

### Technical Improvements
- [ ] Implement caching for faster repeat queries
- [ ] Add error handling and logging
- [ ] Optimize chunk size and overlap parameters
- [ ] Implement hybrid search (keyword + semantic)
- [ ] Add document versioning
- [ ] Deploy to cloud platform (AWS, GCP, or Azure)
- [ ] Add authentication and user management
- [ ] Implement rate limiting

## Troubleshooting

### Common Issues

**Issue: "GOOGLE_API_KEY not found"**
- Solution: Ensure you've set the environment variable correctly
  ```bash
  export GOOGLE_API_KEY=your_api_key_here
  ```

**Issue: "Module not found"**
- Solution: Install missing dependencies
  ```bash
  pip install -r requirements.txt
  ```

**Issue: "FAISS index not found"**
- Solution: Run data_ingestion.py first to create the index
  ```bash
  cd Code
  python data_ingestion.py
  ```

**Issue: Slow performance**
- Solution: Ensure FAISS index is saved locally and being loaded (not recreated each time)
- Check your internet connection for API calls

## Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Commit your changes**
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. **Push to the branch**
   ```bash
   git push origin feature/AmazingFeature
   ```
5. **Open a Pull Request**

### Contribution Guidelines
- Follow PEP 8 style guidelines for Python code
- Add comments and documentation for new features
- Test your changes thoroughly
- Update README.md if needed

## Best Practices

1. **Security**: Never commit your API keys to version control
2. **Data Privacy**: Ensure banking documents are properly secured
3. **Regular Updates**: Keep dependencies updated for security patches
4. **Testing**: Test with various queries before deployment
5. **Monitoring**: Track system performance and user queries

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- **LangChain**: For the excellent framework for building LLM applications
- **Google AI**: For providing the Generative AI API and embedding models
- **FAISS**: For the efficient similarity search library
- **Streamlit**: For the intuitive web framework
- **Bank of Baroda**: For the use case and domain

## Contact

For questions, suggestions, or issues:
- Open an issue on GitHub
- Email: your.email@example.com
- LinkedIn: [Your Profile](https://linkedin.com/in/yourprofile)

## Disclaimer

This is a demonstration project. For production use in banking environments:
- Implement proper authentication and authorization
- Ensure compliance with banking regulations
- Add comprehensive error handling and logging
- Conduct security audits
- Implement data encryption
- Follow GDPR/data privacy regulations

---

**Built with ❤️ using LangChain, Google Gemini AI, and FAISS**
