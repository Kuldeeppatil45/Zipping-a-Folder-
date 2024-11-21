# Zipping-a-Folder

## Description
This program compresses a specified folder (directory) and its contents (including subdirectories) into a .zip archive. It ensures that the resulting zip file preserves the folder structure and handles errors gracefully, such as invalid paths or permission issues.

## Features
Compresses all files and subdirectories inside the folder.
Creates a .zip file with the same name as the folder in the same directory.
Handles invalid paths, empty folders, and permission errors gracefully.
Ensures the resulting .zip file can be extracted to recreate the original folder structure.
(Optional) Allows users to specify a custom name for the .zip file.
(Optional) Supports password protection for the .zip file.

## Prerequisites
1. Python version: Ensure you have Python 3.6 or above installed.
2. Required Library: The program uses the built-in zipfile and os libraries, so no additional installations are needed.
   
## How to Use
1.Run the Program:
Open a terminal or command prompt.
Navigate to the directory where the program file (zip_folder.py) is saved.
Run the program by typing:
 - python zip_folder.py

2.Provide Input:
When prompted, enter the full path to the folder you want to compress. 

Example:
Please enter the folder path to zip: C:\Users\YourUsername\Documents\my_folder

3. Output:
The program creates a .zip file in the same location as the input folder.

Example:
Folder successfully zipped as: C:\Users\YourUsername\Documents\my_folder.zip

# Expected Input/Output
## Input Example
Folder path: C:\Users\YourUsername\Documents\my_folder

## Output
A ".zip" file will be created in the same directory:
C:\Users\YourUsername\Documents\my_folder.zip

# Error Handling
If the folder path is invalid or does not exist, the program will display:
 - Error: The provided folder path does not exist.
If the folder is empty, the program will create an empty .zip file without errors.
If there are permission issues, the program will display an appropriate error message.

# Testing

Test with:

A small folder containing a few files and subdirectories.

A large folder with multiple levels of subdirectories and files.

An empty folder.

Verify that the resulting .zip file can be extracted and matches the original folder structure.

