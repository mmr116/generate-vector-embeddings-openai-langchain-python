import os
from pinecone import Pinecone

# Retrieve the Pinecone API key and host from environment variables
pinecone_api_key = os.getenv("PINECONE_API_KEY")
pinecone_host = os.getenv("PINECONE_HOST")

# Error handling (optional): Check if the environment variables are set
if not pinecone_api_key:
    raise ValueError("PINECONE_API_KEY environment variable not set!")
if not pinecone_host:
    raise ValueError("PINECONE_HOST environment variable not set!")

# Initialize Pinecone instance
pinecone = Pinecone(api_key=pinecone_api_key, environment=pinecone_host)

# Define index name and dimension
index_name = "document-embeddings"
embedding_dimension = 1536  # Dimension based on your provided information

# Connect to the index
index = pinecone.Index(index_name)

# Define a sample embedding
sample_embedding = [0.1] * embedding_dimension  # Example embedding, replace with actual data if available

# Upsert the sample embedding into the Pinecone index
index.upsert(vectors=[{"id": "sample_embedding_1", "values": sample_embedding}])

print("Successfully stored sample embedding")
