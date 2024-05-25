import os
from openai import OpenAI  # Import the OpenAI class

# Replace with your OpenAI API key (ensure it's set in the environment variable)
api_key = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

# Sentence to generate embedding for
text = "Hello world"

try:
  # Call the embeddings API
  response = client.embeddings.create(
    input=text,
    model="text-embedding-ada-002"  # Replace with your desired model if needed
  )
  # Access embedding using the appropriate method (may vary with library version)
  embedding = response.data[0].embedding  # Assuming `data` is a list and `embedding` is a field within the first element
  print("Embedding for 'Hello world':")
  print(embedding)
except openai.OpenAIError as e:
  print(f"Error: {e}")
