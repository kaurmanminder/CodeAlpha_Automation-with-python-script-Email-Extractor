# Email Address Extractor and Saver

A robust, terminal-based task automation tool written in Python that parses files, extracts valid email addresses using regular expressions, deduplicates them, and saves the unique entries to a sorted output file.

Developed as part of a **Python Task Automation Internship Project**.

---

## 1. Project Overview
In modern business environments, handling large volumes of unstructured text—such as raw system logs, email archives, customer inquiries, or contact forms—is a common administrative challenge. Manually extracting email addresses from these documents is tedious and prone to errors.

This project automates the extraction workflow. It parses text files of any size, isolates valid email addresses based on international formatting standards, removes any duplicates, sorts them alphabetically, and writes the clean list into an output file. It features a professional command-line interface (CLI) with clean logging and comprehensive error handling.

---

## 2. Features
* **Regular Expression (Regex) Matching**: Uses a highly precise regex pattern to ensure only correctly formatted emails are extracted, ignoring incomplete or malformed strings.
* **Auto-Deduplication & Sorting**: Normalizes all matched emails to lowercase and removes duplicates, saving them in alphabetical order.
* **Robust File & Error Handling**: Gracefully handles missing files, permission errors, and empty/whitespace-only input documents, providing clear feedback instead of system tracebacks.
* **Flexible CLI Interface**: Accepts command-line arguments to specify custom input and output file paths, fallback-defaulting to local files.
* **No External Dependencies**: Built entirely using Python's standard libraries, making it fully portable and instant to set up.

---

## 3. Technologies Used
* **Language**: Python 3.10+
* **Dependencies**: None (Uses built-in standard libraries)

---

## 4. Python Concepts Used

This project applies core beginner-to-intermediate Python concepts widely used in corporate scripting and task automation:

### A. Regular Expressions (`re` module)
* **Usage Location**: `main.py` -> `extract_emails()` function.
* **Explanation**: The regex pattern `[a-zA-Z0-9._%+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*\.[a-zA-Z]{2,}` parses the document. It matches characters representing local usernames, followed by `@`, one or more subdomain labels, and a terminal TLD (Top-Level Domain) of at least 2 characters.

### B. File System Manipulation (`os` module)
* **Usage Location**: `main.py` -> `read_file()` and `save_emails()` functions.
* **Explanation**: Used `os.path.exists()` to check if the target input file is present before reading, `os.path.getsize()` to test for empty files, and `os.makedirs()` to auto-create directory paths if the user specifies a custom folder for saving outputs.

### C. File Handling (`open`, `read`, `write`)
* **Usage Location**: `main.py` -> `read_file()` and `save_emails()` functions.
* **Explanation**: Used Python's context managers (`with open(...)`) to ensure files are safely opened and closed, preventing file handle leaks and ensuring file resources are released even if a runtime exception occurs.

### D. Collection Types & Set Deduplication
* **Usage Location**: `main.py` -> `save_emails()` function.
* **Explanation**: Set comprehension (`{email.lower() for email in emails}`) is used to cast all emails to lowercase and filter out duplicates. A `sorted()` function then converts the set back into an ordered list for saving and previewing.

### E. CLI Argument Parsing (`argparse` module)
* **Usage Location**: `main.py` -> `parse_arguments()` function.
* **Explanation**: Allows professional parameter passing (e.g. `--input` / `-i` and `--output` / `-o`) with auto-generated `--help` documentation.

### F. Exception Handling (`try-except`)
* **Usage Location**: `main.py` -> `main()` coordinator function.
* **Explanation**: Captures `FileNotFoundError`, `PermissionError`, and `ValueError` to output meaningful, colored logs for the operator instead of exposing raw traceback dumps.

---

## 5. Installation Steps
Since the project runs strictly on the standard Python distribution, the installation is straightforward:

1. **Clone or Download the Project**:
   Ensure you have the `Email-Extractor` directory on your machine.

2. **Verify Python Installation**:
   Open your terminal/command prompt and verify Python is installed:
   ```bash
   python --version
   ```
   *(Note: Python 3.10 or higher is recommended).*

3. **Install Dependencies**:
   This project does not require external installations. You can view the `requirements.txt` file to verify:
   ```bash
   cat requirements.txt
   ```

---

## 6. How to Run the Project
Open a command terminal, navigate to the project directory, and execute the script.

### Option A: Running with Default Files
By default, the script looks for `sample_input.txt` in its directory and outputs to `extracted_emails.txt`:
```bash
python main.py
```

### Option B: Specifying Custom Input & Output Paths
You can pass custom files using `--input` (`-i`) and `--output` (`-o`) arguments:
```bash
python main.py -i my_input_logs.txt -o my_output_emails.txt
```

### Option C: Viewing Help Documentation
To view the command-line usage manual:
```bash
python main.py --help
```

---

## 7. Sample Input and Output

### Sample Input (`sample_input.txt`)
```text
========================================================================
             PROJECT COMMUNICATIONS AND STAFF DIRECTORY
========================================================================
Author: Admin Department (admin@company-hub.org)
Please email us directly at support@company-hub.org.
- Alice Carter: alice.carter@engineering.tech-hub.io
- Bob Jenkins: bob_jenkins123@hub-net.com
Invalid emails to ignore: user@missingdomain, error@domain..com
========================================================================
```

### CLI Terminal Output
```text
======================================================================
      EMAIL ADDRESS EXTRACTOR & SAVER (TASK AUTOMATION)
======================================================================
    
[*] Starting extraction process...
[*] Input File  : sample_input.txt
[*] Output File : extracted_emails.txt
----------------------------------------------------------------------
[+] Success! Extraction completed successfully.
[+] Total email addresses found: 15
[+] Unique email addresses saved: 13
----------------------------------------------------------------------
[*] Preview of extracted unique emails:
  1. admin@company-hub.org
  2. alice.carter@engineering.tech-hub.io
  3. bob_jenkins123@hub-net.com
  ...
----------------------------------------------------------------------
[+] All unique emails have been saved to: extracted_emails.txt
```

### Sample Output (`extracted_emails.txt`)
```text
admin@company-hub.org
alice.carter@engineering.tech-hub.io
bob_jenkins123@hub-net.com
...
```

---

## 8. Folder Structure
```text
Email-Extractor/
│
├── main.py                  # Main Python automation script
├── sample_input.txt         # Realistic input text containing email addresses
├── extracted_emails.txt     # Generated output file with unique email addresses
├── README.md                # Comprehensive project documentation
├── requirements.txt         # Dependencies checklist (Standard library)
└── screenshots/             # Mockups and execution evidence
    └── output.png           # Screenshot of terminal output execution
```

---

## 9. Future Improvements
* **Direct Web Extraction**: Extend capabilities to extract email addresses directly from a live URL or web page using `urllib` or `requests`.
* **Support for PDF and Word Documents**: Add parsers for binary documents (`.pdf`, `.docx`) using external libraries like `PyPDF2` or `python-docx`.
* **Export to CSV/Excel**: Enhance the save utility to export emails to structured sheets alongside domain analysis.
* **Email Domain Grouping**: Group extracted emails by domain name (e.g., Gmail, Outlook, company domain) and export metrics.

---

## 10. Author Section
* **Developer**: Python Automation Intern
* **Internship Track**: Task Automation with Python Scripts
* **Submission Date**: June 23, 2026
* **Organization**: Internship College Portfolio
