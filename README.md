# Token Calculation Tool :books:

This program is designed to calculate the number of tokens required for text input in the OpenAI environment. It can extract text from PDF files and determine the token count, which is useful for estimating costs when interacting with OpenAI's language models. Additionally, the program provides an option to generate a new PDF file where each token from the original text is color-coded.

## Table of Contents

- [What are Tokens in OpenAI?](#what-are-tokens-in-openai)
- [How the Program Works](#how-the-program-works)
- [Dependencies](#dependencies)
- [Installation](#installation)
- [Usage](#usage)
    - [Counting Tokens in PDFs](#counting-tokens-in-pdfs)
    - [Generating Colored Token PDFs](#generating-colored-token-pdfs)
- [License](#license)

## What are Tokens in OpenAI?

Tokens are the individual units that language models use to process text. In the context of OpenAI, a token can be as short as one character or as long as one word. For example:
- The word "chatGPT" is a single token.
- The phrase "Hello, world!" is split into multiple tokens.

Knowing the number of tokens in a text is important because OpenAI's models have token limits, and pricing is often based on the number of tokens processed.

## How the Program Works

### Counting Tokens

1. **Extract Text from PDF:** The program uses `PyPDF2` to read and extract text from PDF files.
2. **Tokenization:** It uses the `tiktoken` library to tokenize the extracted text based on the specified model's encoding.
3. **Token Count:** The program calculates the total number of tokens in each PDF and provides an overall token count for all files in the specified folder.

### Generating Colored Token PDFs

1. **Token Extraction:** The text from a PDF file is tokenized.
2. **Color-Coding:** Each token is assigned a random color.
3. **PDF Creation:** A new PDF file is generated where each token is displayed in its assigned color.

## Dependencies

- `os`: For file and folder operations.
- `PyPDF2`: For reading and extracting text from PDF files.
- `tiktoken`: For tokenizing text based on OpenAI's model encoding.
- `FPDF`: For creating the new PDF file with colored tokens (used in the token distribution section).

## Installation

Install the required libraries using pip:

```bash
pip install os PyPDF2 tiktoken fpdf
```

## Usage

### Counting Tokens in PDFs
1. Set the path to the folder containing your PDF files.
2. Set the encoding name, such as "o200k_base" for the GPT-4 model.
3. Run the count_tokens_in_pdfs function to process the files and get the token count.

Example usage in code:
```python
folder_path = "path/to/pdf/folder"
encoding_name = "o200k_base"  # For GPT-4
count_tokens_in_pdfs(folder_path, encoding_name)
```

### Generating Colored Token PDFs
1. Set the folder path containing the PDF files. 
2. Specify the model name, for example, "gpt-4o". 
3. Run the process_pdf_and_generate_colored_pdf function to generate new PDFs with color-coded tokens.

Example usage in code:
```python
folder_path = "input"
model_name = "gpt-4o"
process_pdf_and_generate_colored_pdf(folder_path, model_name)
```
