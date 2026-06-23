#!/usr/bin/env python3
"""
Email Address Extractor and Saver
--------------------------------
Author: Student Intern
Description: A Python automation script that reads an input text file,
             extracts all valid email addresses using regular expressions,
             deduplicates them, and saves the unique list to an output file.
             Includes detailed CLI logging and error handling.
"""

import argparse
import os
import re
import sys

# Define a robust, industry-standard Regular Expression pattern for email validation.
# Matches: local-part@domain-part.tld
# - Local part: letters, numbers, dots, underscores, percents, plus, hyphen
# - Domain part: alphanumeric and hyphens, separated by single dots
# - TLD (Top Level Domain): letters only, at least 2 characters long (e.g., .com, .org, .co.uk)
EMAIL_REGEX = re.compile(
    r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*\.[a-zA-Z]{2,}"
)

# Resolve default paths relative to the directory where this script is located.
# This prevents FileNotFoundError when executing the script from outside its folder.
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_INPUT_PATH = os.path.join(SCRIPT_DIR, "sample_input.txt")
DEFAULT_OUTPUT_PATH = os.path.join(SCRIPT_DIR, "extracted_emails.txt")


def print_banner():
    """
    Prints a professional ASCII banner to the terminal for the CLI interface.
    """
    banner = """
======================================================================
      EMAIL ADDRESS EXTRACTOR & SAVER (TASK AUTOMATION)
======================================================================
    """
    print(banner)


def read_file(file_path: str) -> str:
    """
    Reads the content of the specified text file.

    Parameters:
        file_path (str): The path to the file to be read.

    Returns:
        str: The raw content of the file.

    Raises:
        FileNotFoundError: If the file does not exist at the path.
        PermissionError: If the user lacks permissions to read the file.
        ValueError: If the file is empty or only contains whitespace.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The input file '{file_path}' does not exist.")

    # Check if the file is completely empty before opening
    if os.path.getsize(file_path) == 0:
        raise ValueError(f"The input file '{file_path}' is empty.")

    # Use a context manager to open and read the file safely
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    # Double check if content contains only whitespace
    if not content.strip():
        raise ValueError(f"The input file '{file_path}' contains only whitespace.")

    return content


def extract_emails(text: str) -> list:
    """
    Extracts all valid email addresses from the text using regular expressions.

    Parameters:
        text (str): The raw text to search.

    Returns:
        list: A list of extracted email addresses (strings).
    """
    # re.findall returns a list of all matches found in the text
    emails = EMAIL_REGEX.findall(text)
    return emails


def save_emails(emails: list, file_path: str) -> None:
    """
    Saves unique, sorted email addresses into the specified output file.

    Parameters:
        emails (list): List of extracted email addresses.
        file_path (str): Path to the output text file.

    Raises:
        PermissionError: If the script lacks permissions to write to the path.
    """
    # Normalize emails to lowercase to ensure case-insensitive uniqueness
    unique_emails = sorted(list({email.lower() for email in emails}))

    # Get the directory path for the output file
    output_dir = os.path.dirname(file_path)

    # Create directories if they do not exist (e.g. outputs/extracted.txt)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)

    # Use a context manager to write the results
    with open(file_path, "w", encoding="utf-8") as file:
        for email in unique_emails:
            file.write(email + "\n")


def parse_arguments():
    """
    Parses command-line arguments using the argparse library.

    Returns:
        argparse.Namespace: Object containing the parsed arguments.
    """
    parser = argparse.ArgumentParser(
        description="Extract and save valid email addresses from a text file."
    )
    parser.add_argument(
        "-i", "--input",
        default=DEFAULT_INPUT_PATH,
        help="Path to the input text file"
    )
    parser.add_argument(
        "-o", "--output",
        default=DEFAULT_OUTPUT_PATH,
        help="Path to the output text file"
    )
    return parser.parse_args()


def main():
    """
    The main execution coordinator for the script.
    """
    print_banner()

    # Parse arguments provided by the user
    args = parse_arguments()

    print(f"[*] Starting extraction process...")
    print(f"[*] Input File  : {args.input}")
    print(f"[*] Output File : {args.output}")
    print("-" * 70)

    try:
        # Step 1: Read the file content
        content = read_file(args.input)

        # Step 2: Extract email addresses
        all_emails = extract_emails(content)
        total_found = len(all_emails)

        if total_found == 0:
            print("[!] Warning: No email addresses were found in the file.")
            # Still write an empty output file or handle it clean
            save_emails([], args.output)
            print(f"[+] Output file '{args.output}' updated (0 emails found).")
            return

        # Deduplicate and sort emails for reporting
        unique_emails = sorted(list({email.lower() for email in all_emails}))
        unique_count = len(unique_emails)

        # Step 3: Save results to the output file
        save_emails(all_emails, args.output)

        # Print success report to user
        print(f"[+] Success! Extraction completed successfully.")
        print(f"[+] Total email addresses found: {total_found}")
        print(f"[+] Unique email addresses saved: {unique_count}")
        print("-" * 70)
        print("[*] Preview of extracted unique emails:")
        for idx, email in enumerate(unique_emails, 1):
            print(f"  {idx}. {email}")
        print("-" * 70)
        print(f"[+] All unique emails have been saved to: {args.output}")

    except FileNotFoundError as fnf_error:
        print(f"[ERROR] File Not Found: {fnf_error}", file=sys.stderr)
        sys.exit(1)
    except ValueError as val_error:
        print(f"[ERROR] Invalid File Content: {val_error}", file=sys.stderr)
        sys.exit(1)
    except PermissionError:
        print(
            f"[ERROR] Permission Denied: Lacking read/write access to "
            f"input/output paths.", file=sys.stderr
        )
        sys.exit(1)
    except Exception as exc:
        print(f"[ERROR] An unexpected error occurred: {exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
