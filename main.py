
from document_reader import read_document
from chunking import create_chunks

file_path = "documents/sample.txt"

text = read_document(file_path)

chunks = create_chunks(text, 30, 5)

print("Total Chunks:", len(chunks))

for chunk in chunks:
    print("\nChunk:")
    print(chunk)
    print("----------------")


