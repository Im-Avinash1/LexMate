import fitz  # PyMuPDF
import docx

def parse_document(file):
    if file.type == "application/pdf":
        return parse_pdf(file)
    elif file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        return parse_docx(file)
    else:
        return "Unsupported file format"

def parse_pdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    text = "\n".join(page.get_text() for page in doc)
    return text

def parse_docx(file):
    doc = docx.Document(file)
    text = "\n".join(p.text for p in doc.paragraphs)
    return text