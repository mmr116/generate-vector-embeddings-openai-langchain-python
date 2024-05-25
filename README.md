# Vector Embedding - Code Repository

This repository contains Python code for generating and storing text embeddings from a PDF document. The code utilizes several technologies:

- OpenAI API: Used to generate numerical representations (embeddings) of text chunks.
- Pinecone: A vector database for storing and efficiently searching the generated embeddings.
- PyPDF2: A Python library to extract text from PDF files.
- langchain.text_splitter: A library for splitting text into smaller chunks.

# Installation

- Prerequisites: Ensure you have Python installed (version 3.6 or later recommended). Consider creating a virtual environment using tools like venv or virtualenv to isolate project dependencies and avoid conflicts with other Python installations.

Package Installation: Use pip to install the required Python packages within your activated virtual environment (if applicable):

pip install openai pinecone langchain PyPDF2

- Required Python Packages

&#8209; openai: Python library for interacting with the OpenAI API for generating embeddings.

&#8209; pinecone: Python library for managing data interactions with the Pinecone vector database.

&#8209; langchain: Python library that provides the RecursiveCharacterTextSplitter class for splitting text into chunks.

&#8209; PyPDF2: Python library for extracting text content from PDF files.

# Python Scripts

- 1-test-embeddings-openai.py

This script demonstrates how to generate an embedding for a given text sentence using the OpenAI API.

Functionality: Generates an embedding for the text "Hello world".
Technology: OpenAI API (Python library)
Language: Python

2-pinecone-embedding-store-test.py
  
This script showcases storing a sample embedding in a Pinecone index.

Functionality: Stores a sample embedding vector in a Pinecone index.
Technology: Pinecone (Python library)
Language: Python

3. 3-generate-text-chunks-embeddings-from-pdf.py

This script takes a PDF file, extracts the text content, splits it into chunks, generates embeddings for each chunk using OpenAI, and finally prints the results.

Functionality: Extracts text from PDF, splits into chunks, generates embeddings for each chunk, and prints them.
Technology: PyPDF2, langchain.text_splitter, OpenAI API (Python libraries)
Language: Python

4. 4-generate-text-chunks-embeddings-store-vectordb.py

This script builds upon the previous one by not only generating embeddings but also storing them in a Pinecone index along with the original text chunks as metadata.

Functionality: Extracts text from PDF, splits into chunks, generates embeddings, stores them with corresponding text in Pinecone.
Technology: PyPDF2, langchain.text_splitter, OpenAI API, Pinecone (Python libraries)
Language: Python
Running the Code

# Assumptions

Make sure you have Python installed (version 3.6 or later recommended).
Create a virtual environment (optional but recommended) to isolate project dependencies.
Install the required libraries using pip install openai langchain pypdf2 pinecone.
Set the OPENAI_API_KEY and PINECONE_API_KEY environment variables with your respective API keys.
You might need to adjust file paths and other parameters within the scripts.
Run each script from the command line: python 1-test-embeddings-openai.py etc.

# Additional Notes

Replace "text-embedding-ada-002" with your desired OpenAI model name for generating embeddings.
Error handling is included in some scripts (demonstrated) but can be further improved for production use.
