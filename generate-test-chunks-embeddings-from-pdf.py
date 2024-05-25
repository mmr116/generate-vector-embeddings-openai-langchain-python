import os
from openai import OpenAI  # Import the OpenAI class
from langchain.text_splitter import RecursiveCharacterTextSplitter
import PyPDF2

# Function to extract text from a PDF file using PyPDF2
def extract_text_from_pdf(pdf_path):
  text = ""
  with open(pdf_path, "rb") as file:
    reader = PyPDF2.PdfReader(file)
    for page_num in range(len(reader.pages)):
      page = reader.pages[page_num]
      text += page.extract_text()
  return text

# Function to split extracted text into smaller chunks using Recursive Character Text Splitter
def split_text_into_chunks(text, chunk_size=1000, chunk_overlap=200):
  splitter = RecursiveCharacterTextSplitter(
    chunk_size=chunk_size,
    chunk_overlap=chunk_overlap
  )
  chunks = splitter.split_text(text)
  return chunks

# Function to generate embeddings for each chunk using OpenAI API
def generate_embeddings(chunks):
  # Initialize OpenAI client with API key from environment variable
  client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

  embeddings = []
  for chunk in chunks:
    # Use client object to call the embeddings API
    response = client.embeddings.create(
      input=chunk,
      model="text-embedding-ada-002"  # Replace with your desired model
    )
    # Access embedding using the appropriate method (may vary with library version)
    embedding = response.data[0].embedding  # Assuming `data` is a list and `embedding` is a field within the first element
    embeddings.append(embedding)
  return embeddings

# Example usage
pdf_path = "/home/mrahman116/vector-embedding/embeddings-test.pdf"

# Step 1: Extract text from PDF
extracted_text = extract_text_from_pdf(pdf_path)
print("Extracted Text:", extracted_text)

# Step 2: Split extracted text into chunks
chunks = split_text_into_chunks(extracted_text)
print("Text Chunks:")
for i, chunk in enumerate(chunks):
  print(f"Chunk {i+1}:\n{chunk}\n")

# Step 3: Generate embeddings for each chunk
embeddings = generate_embeddings(chunks)
print("Embeddings:")
for i, embedding in enumerate(embeddings):
  print(f"Embedding {i+1}:\n{embedding}\n")
