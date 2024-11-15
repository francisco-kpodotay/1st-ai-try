# Step 1: Load the book
def load_book(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()
        return text
    except Exception as e:
        print(f"Error loading file: {e}")
        return None

# Step 2: Split into manageable chunks
def split_into_chunks(text, max_length=512):
    """
    Splits text into chunks with a maximum length of `max_length` characters.
    """
    sentences = text.split(". ")  # Split by sentences
    chunks = []
    current_chunk = ""

    for sentence in sentences:
        if len(current_chunk) + len(sentence) + 1 <= max_length:
            current_chunk += sentence + ". "
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence + ". "

    if current_chunk:  # Add the last chunk
        chunks.append(current_chunk.strip())

    return chunks

# Step 3: Preprocess the book
def preprocess_book(file_path, max_chunk_length=512):
    text = load_book(file_path)
    if text:
        chunks = split_into_chunks(text, max_chunk_length)
        print(f"Book split into {len(chunks)} chunks.")
        return chunks
    return []

# Usage
file_path = "./book.txt"
chunks = preprocess_book(file_path)

# Save the chunks if needed
with open("book_chunks.txt", "w", encoding="utf-8") as file:
    for chunk in chunks:
        file.write(chunk + "\n\n")
