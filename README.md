# HTML to DOCX and Quizlet Flashcard Converter

This repository contains two Python scripts that automate processing HTML files saved from the `rezidentiat.com` website. These scripts help users extract and reformat data into more usable formats, such as `.docx` files for reports and `.txt` files for Quizlet flashcards.

## Important Note

These scripts were developed for the `rezidentiat.com` website as it existed in 2024. Future updates or changes to the website's structure may affect the functionality of the scripts.

## Scripts Overview

### 1. **grile.py**

A script designed to extract questions and correct answers from an HTML page saved from the `rezidentiat.com` website's reports section. The script outputs the data in a `.docx` file for easier review and printing.

#### Usage

Run the script with the following command:

```bash
python3 grile.py [source]
```

- **`[source]`**: The file path to the saved HTML page (e.g., `./simulare1_rezidentiat_com.html`).

#### Output

The script generates a `.docx` file with the same name as the input file, but with the `.docx` extension. The file contains:

- Questions
- Correct answers displayed below each question

#### Example

```bash
python3 grile.py ./simulare1_rezidentiat_com.html
```
This generates `simulare1_rezidentiat_com.docx` in the same directory.

---

### 2. **flashcard.py**

A script that processes flashcard HTML pages saved from the `rezidentiat.com` website and groups 50 flashcards into a format compatible with Quizlet's import feature.

#### Usage

Run the script with the following command:

```bash
python3 flashcard.py [source]
```

- **`[source]`**: The file path to the saved HTML page (e.g., `./flashcards_rezidentiat_com.html`).

#### Output

The script generates a `.txt` file with the same name as the input file, but with the `.txt` extension. The file contains:

- Flashcards formatted as required by Quizlet:
  - **Term** `tab` **Definition**
- Each file groups up to 50 flashcards for easy import into Quizlet.

#### Example

```bash
python3 flashcard.py ./flashcards_rezidentiat_com.html
```
This generates `flashcards_rezidentiat_com.txt` in the same directory.

---

## Prerequisites

- Python 3.x
- Required Python libraries:
  - `python-docx` (for `.docx` generation)
  - `BeautifulSoup` (for parsing HTML files)

Install dependencies with:

```bash/powershell/cmd
pip install python-docx beautifulsoup4
```

---

## How to Save HTML Pages from `rezidentiat.com`

1. Open the relevant page on the `rezidentiat.com` website.
2. Use your browser's **Save As** feature (e.g., `Ctrl+S` or `Cmd+S`) to save the page as an HTML file.
3. Use the saved HTML file as input for the scripts.

---

## License

This repository is licensed under the MIT License:

```
MIT License

Copyright (c) 2024 ac999

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## Contribution

Feel free to open issues or submit pull requests if you have suggestions for improvements or encounter any bugs.

---

## Contact

If you have any questions, feel free to reach out or open an issue in the repository.
