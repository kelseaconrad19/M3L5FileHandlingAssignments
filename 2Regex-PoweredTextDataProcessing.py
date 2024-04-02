"""
Task 1:
    - Problem Statement:
        - Write a Python script to extract all email addresses from a given text file (contacts.txt). The file contains a mix of text and email addresses.
    - Expected Outcome:
        - The script should output a list of all unique email addresses found in the file. Utilize regex to accurately identify email addresses amidst other text.
"""
import re


def extract_emails(filename):
    with open(filename, 'r') as file:
        emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", file.read())
        email_list = list(set(emails))
        print(email_list)


if __name__ == "__main__":
    extract_emails('contacts.txt')
