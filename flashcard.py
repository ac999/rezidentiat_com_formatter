# from bs4 import BeautifulSoup
# import sys
# import os
#
#
# def extract_flashcards_from_html(html_content, output_file_name):
#     soup = BeautifulSoup(html_content, 'lxml')
#
#     # List to hold each flashcard's question and answer
#     flashcards = []
#
#     # Extract each flashcard
#     for flashcard in soup.find_all('div', class_="flashCenter"):
#         # Extract flashcard question (front side of card)
#         question_section = flashcard.find('div', class_="front")
#         question_text = question_section.get_text(strip=True) if question_section else "No question found"
#
#         # Extract flashcard answer (back side of card)
#         answer_section = flashcard.find('div', class_="back")
#         answer_text = answer_section.get_text(strip=True) if answer_section else "No answer found"
#
#         # Append question and answer in the specified format
#         flashcards.append(f"{question_text},{answer_text}")
#
#     # Join all flashcards with semicolons
#     output_text = ";".join(flashcards)
#
#     # Save the output to a .txt file
#     with open(f"{output_file_name}.txt", "w", encoding="utf-8") as file:
#         file.write(output_text)
#
#     print(f"Text file saved as {output_file_name}.txt")
#
#
# # Example usage:
# if __name__ == '__main__':
#     if len(sys.argv) != 2:
#         print(f"Usage: python {sys.argv[0]} <file_path>")
#         sys.exit(1)
#
#     html_file = sys.argv[1]
#     try:
#         with open(html_file, 'r', encoding='utf-8') as file:
#             html_content = file.read()
#
#         # Extract flashcards and format the output
#         output_file_name = os.path.splitext(os.path.basename(html_file))[0]
#         extract_flashcards_from_html(html_content, output_file_name)
#
#     except Exception as e:
#         print(f"Error processing file: {e}")

from bs4 import BeautifulSoup
import sys
import os


def extract_flashcards_from_html(html_content, output_file_name):
    soup = BeautifulSoup(html_content, 'lxml')

    # List to hold each flashcard's question and answer
    flashcards = []

    # Extract each flashcard
    for flashcard in soup.find_all('div', class_="flashCenter"):
        # Extract flashcard question (front side of card)
        question_section = flashcard.find('div', class_="front")
        question_text = question_section.get_text(strip=True) if question_section else "No question found"

        # Extract flashcard answer (back side of card)
        answer_section = flashcard.find('div', class_="back")
        answer_text = answer_section.get_text(strip=True) if answer_section else "No answer found"

        # Append question and answer in the specified format with [tab] as separator
        flashcards.append(f"{question_text}\t{answer_text}")

    # Group the flashcards into sets of 50
    grouped_flashcards = [flashcards[i:i + 50] for i in range(0, len(flashcards), 50)]

    # Create the final output text
    output_text = ""
    group_id = 1;
    for group in grouped_flashcards:
        output_text += "Group " + str(group_id) + '\n\n' + "\n".join(group) + "\n\n-------\n\n"  # Separate groups by [new_line]
        group_id += 1

    # Save the output to a .txt file
    with open(f"{output_file_name}.txt", "w", encoding="utf-8") as file:
        file.write(output_text)

    print(f"Text file saved as {output_file_name}.txt")


# Example usage:
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <file_path>")
        sys.exit(1)

    html_file = sys.argv[1]
    try:
        with open(html_file, 'r', encoding='utf-8') as file:
            html_content = file.read()

        # Extract flashcards and format the output
        output_file_name = os.path.splitext(os.path.basename(html_file))[0]
        extract_flashcards_from_html(html_content, output_file_name)

    except Exception as e:
        print(f"Error processing file: {e}")
