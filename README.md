# Contact Manager App

A simple, lightweight desktop application built with Python and Flet for managing your contacts.

## Features
- **Add Contacts:** Easily save a name and phone number.
- **Delete Contacts:** Remove contacts you no longer need.
- **Persistent Storage:** Contacts are saved automatically to a local `contacts.json` file so you won't lose your data when you close the app.
- **Clean UI:** A simple and intuitive user interface using Flet's Material Design controls.

## Project Structure
- `contact.py`: The main Python application script containing the UI and logic.
- `contacts.json`: The data file where contacts are stored (created automatically if it doesn't exist).
- `requirements.txt`: Contains the required Python dependencies (Flet).
- `contact.gitgnore`: Standard ignore file for Python compilation and build artifacts.

## Prerequisites
- Python 3.7 or newer.

## Installation
1. Clone or extract the project files to a local directory.
2. Open a terminal or command prompt in the project directory.
3. Install the required dependencies using pip:
   ```
   pip install -r requirements.txt
   ```
   *Note: This project specifically uses `flet == 0.25.0`.*

## Usage
Run the application by executing the main script:
   ```
   python contact.py
   ```

## Packaging
If you wish to package this into a standalone executable, you can use the Flet packager:
   ```
   flet pack contact.py
   ```
(Note: `build/`, `dist/`, and `*.spec` are already configured to be ignored by version control).
