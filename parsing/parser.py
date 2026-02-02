import pdfplumber
from docx import Document
from pathlib import Path


def parse_pdf(file_path: str) -> str:
    """
    Extract text from a PDF file.
    """
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text.strip()


def parse_docx(file_path: str) -> str:
    """
    Extract text from a DOCX file.
    """
    doc = Document(file_path)
    return "\n".join(paragraph.text for paragraph in doc.paragraphs).strip()


def parse_file(file_path: str) -> str:
    """
    Detect file type and extract text accordingly.
    Supported formats: PDF, DOCX
    """
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    if path.suffix.lower() == ".pdf":
        return parse_pdf(file_path)

    if path.suffix.lower() == ".docx":
        return parse_docx(file_path)

    raise ValueError("Unsupported file format. Use PDF or DOCX.")
