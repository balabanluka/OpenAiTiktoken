import os
import PyPDF2
import tiktoken

# About 99% accuracy in determining how big a document is in tokens

# If we are going to use this, I will combine tiktoken and embeddings so that tiktoken splits the file into chunks depending
# on the tokens (splits the text every approximately 8192 tokens) and then we vectorize each chunk separately to speed up the process.

def extract_text_from_pdf(file_path: str) -> str:
    text = ""
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text

def extract_text_from_md(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()
    return text

def num_tokens_from_string(string: str, encoding_name: str) -> int:
    encoding = tiktoken.get_encoding(encoding_name)
    encoded = encoding.encode(string)
    num_tokens = len(encoded)
    return num_tokens

def count_tokens_in_files(folder_path: str, encoding_name: str) -> int:
    total_tokens = 0
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        text = ""
        if filename.endswith(".pdf"):
            print(f"Processing PDF file: {filename}")
            text = extract_text_from_pdf(file_path)
        elif filename.endswith(".md"):
            print(f"Processing Markdown file: {filename}")
            text = extract_text_from_md(file_path)

        if text:
            num_tokens = num_tokens_from_string(text, encoding_name)
            print(f"Number of tokens in {filename}: {num_tokens}")
            total_tokens += num_tokens

    print(f"Total number of tokens in all files: {total_tokens}")
    return total_tokens

# Folder path containing the files
folder_path = "input"

# Encoding name (e.g., for GPT-4)
encoding_name = "o200k_base"

# Count tokens in files
count_tokens_in_files(folder_path, encoding_name)