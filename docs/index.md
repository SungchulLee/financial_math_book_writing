

# Quantitative Finance with Python

Welcome! This book is written in Markdown and published using **MkDocs** with the **Material for MkDocs** theme.

Much of the foundational material in this book was developed through conversations with AI assistants, based on my lecture notes and additional resources, particularly GitHub. While I have reviewed and revised parts of the content, time constraints have prevented a complete line-by-line verification. I sincerely welcome contributions—especially corrections and suggestions—via GitHub pull requests or email.

**GitHub:** [https://github.com/SungchulLee/financial_math_book_writing](https://github.com/SungchulLee/financial_math_book_writing)

**Email:** [sungchul@yonsei.ac.kr](mailto:sungchul@yonsei.ac.kr)

---

## 1. Running the Python Code Examples

To run the code examples in this book, install the following packages that are **not included in the standard Anaconda distribution**:

```python
!pip install beautifulsoup4 cvxpy lxml mplfinance pandas_datareader requests selenium webdriver-manager yfinance
```

---

## 2. Installing MkDocs (For Building the Book Locally)

If you would like to build or modify this book locally, install MkDocs and the Material theme:

```bash
pip install mkdocs mkdocs-material
```

If your project uses additional MkDocs plugins, install them as well (example):

```bash
pip install mkdocs-mermaid2-plugin mkdocs-jupyter mkdocs-git-revision-date-localized-plugin
```

---

## 3. Serving the Book Locally

After installation, navigate to the root directory of the repository:

```bash
cd financial_math_book_writing
```

Start the local development server:

```bash
mkdocs serve
```

Then open your browser at:

```
http://127.0.0.1:8000
```

The page will automatically reload when you modify Markdown files.

---

## 4. Building the Static Site

To generate the static site files:

```bash
mkdocs build
```

The compiled site will be created in the `site/` directory.

---

## 5. Recommended: Using requirements.txt

For convenience, you may install all required packages at once using:

```bash
pip install -r requirements.txt
```

---

**Sungchul Lee**

Department of Mathematics, College of Science

Yonsei University

Seoul, South Korea





