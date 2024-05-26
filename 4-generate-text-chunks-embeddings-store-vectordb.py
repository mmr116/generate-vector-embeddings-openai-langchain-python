import os
from openai import OpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
import PyPDF2
from pinecone import Pinecone

# Retrieve the Pinecone API key and host from environment variables
pinecone_api_key = os.getenv("PINECONE_API_KEY")
pinecone_host = os.getenv("PINECONE_HOST")

# Error handling (optional): Check if the environment variables are set
if not pinecone_api_key:
    raise ValueError("PINECONE_API_KEY environment variable not set!")
if not pinecone_host:
    raise ValueError("PINECONE_HOST environment variable not set!")

# Retrieve the OpenAI API key from environment variable (assuming separate variable)
openai_api_key = os.getenv("OPENAI_API_KEY")

# Error handling (optional): Check if the environment variable is set
if not openai_api_key:
    raise ValueError("OPENAI_API_KEY environment variable not set!")

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
    client = OpenAI(api_key=openai_api_key)

    embeddings = []
    for chunk in chunks:
        # Use client object to call the embeddings API
        response = client.embeddings.create(
            input=chunk,
            model="text-embedding-ada-002"  # Replace with your desired model
        )
        embedding = response.data[0].embedding  # Access the attribute of the response object
        embeddings.append(embedding)
    return embeddings

# Function to store embeddings in Pinecone
def store_embeddings_in_pinecone(embeddings, chunks):
    # Replace with the dimension of your embeddings (e.g., 768 for text-embedding-ada-002)
    embedding_dimension = 1536  # Update based on your OpenAI model or experiment

    # Print retrieved API key for verification (optional)
    # print(f"Retrieved Pinecone API key: {pinecone_api_key}")

    # Initialize Pinecone instance
    pinecone = Pinecone(api_key=pinecone_api_key, environment=pinecone_host)

    # Connect to the existing index
    index_name = "replace your pinecone index name here"
    index = pinecone.Index(index_name)

    # Create a list of dictionaries, where each dictionary represents a data point
    data_points = []
    for i, (chunk, embedding) in enumerate(zip(chunks, embeddings)):
        data_point = {
            "id": f"chunk_{i+1}",
            "values": embedding,
            "metadata": {"text": chunk}
        }
        data_points.append(data_point)

    # Store the data points in the index
    index.upsert(data_points)
    print(f"Successfully stored {len(data_points)} data points in Pinecone")

# Example usage
pdf_path = "/replace_with_your_pdf_filepath/embeddings-test.pdf"

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
    print(f"Embedding {i+1}:\n{embedding[:20]}\n")  # Print only first 20 elements for brevity

# Step 4: Store embeddings in Pinecone
store_embeddings_in_pinecone(embeddings, chunks)
