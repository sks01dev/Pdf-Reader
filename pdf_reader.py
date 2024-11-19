import re
from collections import Counter
from PyPDF2 import PdfReader

# Function to extract text from all pages of a given PDF file
def extract_text_from_pdf(pdf_file: str) -> list[str]:
    """
    Extracts text from all pages of a PDF file.

    Args:
    - pdf_file (str): The path to the PDF file.

    Returns:
    - list[str]: A list of strings, where each string contains the text of one page.
    """
    with open(pdf_file, 'rb') as pdf:  # Open the PDF file in binary read mode
        reader = PdfReader(pdf)  # Initialize PdfReader to read the PDF

        # Print the number of pages for debugging
        print('Pages:', len(reader.pages))
        print('-' * 10)  # Divider for better readability in output

        # Extract text from each page and return as a list
        pdf_text: list[str] = [page.extract_text() for page in reader.pages]
        return pdf_text
    

# Function to count word occurrences in the extracted text
def count_words(text_list: list[str]) -> Counter:
    """
    Counts the frequency of each word in the provided text list.

    Args:
    - text_list (list[str]): A list of text strings (e.g., pages from a PDF).

    Returns:
    - Counter: A dictionary-like object mapping words to their frequency.
    """
    all_words: list[str] = []  # Initialize a list to hold all words
    for text in text_list:
        # Split the text into words using regex, removing punctuation and whitespace
        split_text: list[str] = re.split(r'\s+|[,;?!.-]\s*', text.lower())
        
        # Filter out empty strings and accumulate valid words
        all_words += [word for word in split_text if word]

    # Return a Counter object to count occurrences of each word
    return Counter(all_words)

# Main function to run the process
def main():
    """
    Main function to extract text from a PDF, count word frequencies, and display the most common words.
    """
    # Provide the PDF file path
    pdf_file = 'sample.pdf'

    # Extract text from the PDF
    extracted_text: list[str] = extract_text_from_pdf(pdf_file)

    # Count word occurrences in the extracted text
    counter: Counter = count_words(text_list=extracted_text)

    # Print the top 5 most common words with their frequencies
    print("Top 5 most common words:")
    for word, mention in counter.most_common(5):
        print(f'{word:20}: {mention} times')

# Entry point of the script
if __name__ == '__main__':
    main()
