"""
This script analyzes Python code quality
in a specified directory using Pylint and Flake8.

It identifies Python files within the directory
and runs both linters on each file,providing feedback
on potential issues with the code.
"""

import os
import subprocess


def analyze_code():
    """Analyzes Python code quality in the specified directory.

    Returns:
        None
    """

    # List Python files in the directory
    python_files = [file for file in os.listdir(
        directory) if file.endswith('.py')]

    if not python_files:
        print("No Python files found in the specified directory.")
        return

    # Analyze each Python file using pylint and flake8
    for file in python_files:
        print(f"Analyzing file: {file}")
        file_path = os.path.join(directory, file)

        # Run pylint with explicit check for success
        print("\nRunning pylint...")
        pylint_command = ["pylint", file_path]
        subprocess.run(pylint_command, check=False)

        # Run flake8 with explicit check for success
        print("\nRunning flake8...")
        flake8_command = ["flake8", file_path]
        subprocess.run(flake8_command, check=False)


if __name__ == "__main__":
    user_profile = os.path.expanduser('~')  # Get the user's profile directory
    directory = os.path.join(user_profile, 'Desktop',
                             'Automation-scripts', 'auto-image-downloader')
    analyze_code()
