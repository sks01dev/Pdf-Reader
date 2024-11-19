# 📖 PDF Reader & Word Counter

Welcome to the **PDF Reader & Word Counter** project! This tool helps you extract text from a PDF file and count the occurrences of each word, presenting the most frequently used words. It’s a great utility for text analysis, content parsing, and understanding patterns in your PDF documents.

---

## 🔧 Features
- **Extract Text**: Reads and extracts text from each page of a PDF.
- **Word Counting**: Counts word occurrences using regular expressions.
- **Top Word Analysis**: Displays the top 5 most frequent words with their counts.
- **Error Handling**: Handles basic file errors gracefully.

---

## 📂 Project Structure
```
├── pdf_reader.py      # Python script for reading PDFs and counting words
├── sample.pdf         # Sample PDF file for testing
└── README.md          # Project documentation
```

---

## 🚀 How to Use

### 1. **Prerequisites**
Make sure you have the following installed:
- Python 3.8 or later
- Required libraries: `PyPDF2`, `re`, and `collections`.

Install dependencies using pip:
```bash
pip install PyPDF2
```

### 2. **Run the Script**
1. Place your target PDF file (e.g., `sample.pdf`) in the same directory as `pdf_reader.py`.
2. Run the script:
   ```bash
   python pdf_reader.py
   ```
3. The program will display:
   - Total number of pages in the PDF.
   - Top 5 most frequent words in the text.

---

## 🧪 Sample Output
Running the script with `sample.pdf` yields:
```
Pages: 5
----------
Top 5 most common words:
python              : 6 times
data                : 5 times
science             : 4 times
open                : 4 times
source              : 3 times
```

---

## 📝 Sample PDF File
The provided `sample.pdf` contains sample chapters with meaningful content for testing:
1. **Chapter 1: The Basics of Python**
2. **Chapter 2: Understanding Regular Expressions**
3. **Chapter 3: Introduction to Data Science**
4. **Chapter 4: Exploring Machine Learning**
5. **Chapter 5: The Power of Open Source**

Feel free to replace `sample.pdf` with your own PDF file for analysis.

---

## 📂 Customization
You can modify the following in `pdf_reader.py`:
1. **Word Analysis**:
   - Adjust the regex pattern in `count_words` to include/exclude specific punctuation.
2. **Top Word Count**:
   - Change the number of most common words displayed by modifying this line in `main()`:
     ```python
     for word, mention in counter.most_common(5):
     ```

---


## 🤝 Contributions
We welcome contributions! To contribute:
1. Fork this repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a detailed description.
