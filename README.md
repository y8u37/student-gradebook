# EduTrack: Student Grade & Performance Management System

## Overview
EduTrack is a simple, modular Python application built for managing student records, calculating grade averages, and ranking student performance. It is designed to demonstrate core programming principles, clean code structure, and data management. 

This project comes in two versions a text-based command-line interface (CLI) and a graphical user interface (GUI) both of which share the exact same core logic.

---

## Project Structure
To keep things clean and maintainable, the project is split into three main parts:
* **`student_logic.py`**: Handles all the heavy lifting. This file manages the data structure (lists and dictionaries), data calculations (averages and rankings), and file reading/writing (`students_data.csv`).
* **`main_cli.py`**: The command-line front end. It allows users to interact with the system entirely through text prompts in the terminal.
* **`main_gui.py`**: The graphical front end built using Python's built-in `tkinter` library. It provides a visual table and menus while utilizing the exact same logic as the text version.

---

## Features
1. **Add Students**: Input a student ID, name, and grades for three subjects (Math, Science, English) with built-in input validation to prevent errors.
2. **View & Search**: Display all student records in a structured list or table format.
3. **Automatic Sorting & Rankings**: Uses a sorting algorithm to automatically rank students based on their overall grade averages from highest to lowest.
4. **Data Persistence**: Automatically saves and loads student records from a local CSV file so data isn't lost when you close the application.

---

