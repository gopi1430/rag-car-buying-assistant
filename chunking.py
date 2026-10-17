
def create_chunks(text, chunk_size, overlap):
    if chunk_size <= 0:
        print("Chunk size must be greater than 0")
        return []

    if overlap < 0 or overlap >= chunk_size:
        print("Overlap must be smaller than chunk size")
        return []

    words = text.split()
    chunks = []
    start = 0

    while start < len(words):
        end = start + chunk_size
        chunk = words[start:end]

        chunks.append(" ".join(chunk))

        start = end - overlap

    return chunks
