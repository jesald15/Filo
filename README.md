# Filo

<img width="645" height="374" alt="image" src="https://github.com/user-attachments/assets/a69ae4fd-a3ac-4eef-bcd4-f9fd46105d28" />


A Python CLI tool that automatically organizes files in a directory by categorizing them into folders based on file extensions. 

This project is a command-line folder organizer written in Python that helps automatically sort and organize files within a specified directory. The script scans the target folder, categorizes files based on their extensions, creates appropriate directories if they do not exist, and moves files accordingly.

It is designed as a practical automation utility and a learning project for understanding file system operations in Python.

## Features

Organizes files by extension into predefined categories
Automatically creates destination folders when missing

Supports common file types:
Music
Videos
Images
Documents
Archives
Code
Applications
Simple CLI-based user input
Lightweight and dependency-free

How It Works
User provides the directory path to organize
Script scans all files in the directory
Files are grouped by extension using a dictionary
Folders are created based on predefined extension mappings
Files are moved into their respective folders

Run this code on your terminal: ``python filo.py``

Then enter the absolute path of the directory you want to organize (example):
/home/user/Downloads/

