# HTML to DOCX and Quizlet Flashcard Converter

This repository contains two Python scripts that automate processing HTML files saved from the `rezidentiat.com` website. These scripts help users extract and reformat data into more usable formats, such as `.docx` files for reports and `.txt` files for Quizlet flashcards.

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
  - **Term**	**Definition**
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

This repository is licensed under the [MIT License](LICENSE).

---

## Contribution

Feel free to open issues or submit pull requests if you have suggestions for improvements or encounter any bugs.

---

## Contact

If you have any questions, feel free to reach out or open an issue in the repository.
