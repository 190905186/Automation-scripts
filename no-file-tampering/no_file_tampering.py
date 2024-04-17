"""
This script verifies the integrity of a file by
comparing its calculated SHA-256 checksum with
an expected checksum.

It prompts the user for the file path and
expected checksum, then calculates the actual
checksum and compares them.
"""

import hashlib
import os


def calculate_sha256():
    """Calculates the SHA-256 checksum of a file.

    Returns:
        str: The SHA-256 checksum of the file in hexadecimal format.
    """

    sha256 = hashlib.sha256()
    with open(file_path, 'rb') as file:
        for chunk in iter(lambda: file.read(4096), b''):
            sha256.update(chunk)
    return sha256.hexdigest()


def check_integrity():
    """Checks the integrity of a file by comparing
    its SHA-256 checksum with an expected checksum.

    Returns:
        bool: True if the checksums match, False otherwise.
    """

    actual_checksum = calculate_sha256()
    print(f"Actual SHA-256 Checksum: {actual_checksum}")
    return actual_checksum == expected_checksum


if __name__ == "__main__":
    file_path = input("Enter the path to the file: ")
    expected_checksum = input("Enter the expected SHA-256 checksum: ")

    if os.path.isfile(file_path):
        if check_integrity():
            print("File integrity verified: The file \
                  has not been tampered with.")
        else:
            print("File integrity check failed: The file \
                  may have been tampered with.")
    else:
        print("Error: File not found.")
