
from pypdf import PdfReader
from docx import Document


def read_document(file_path):
    if file_path.endswith(".txt"):
        file = open(file_path, "r", encoding="utf-8")
        text = file.read()
        file.close()

    elif file_path.endswith(".pdf"):
        reader = PdfReader(file_path)
        text = ""

        for page in reader.pages:
            text = text + (page.extract_text() or "") + "\n"

    elif file_path.endswith(".docx"):
        document = Document(file_path)
        text = ""

        for paragraph in document.paragraphs:
            text = text + paragraph.text + "\n"

    else:
        print("Unsupported file format")
        return ""

    return text
text = read_document("documents/sample.txt")
print(text)