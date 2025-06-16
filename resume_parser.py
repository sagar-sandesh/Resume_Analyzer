from pdfminer.high_level import extract_text

def extract_text_from_pdf(file_storage):
    return extract_text(file_storage.stream)
