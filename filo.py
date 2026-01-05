import os
import time

print("""
███████╗██╗██╗     ███████╗
██╔════╝██║██║     ██   ██║
█████╗  ██║██║     ██   ██║
██╔══╝  ██║██║     ██   ██║
██║     ██║███████╗███████║
╚═╝     ╚═╝╚══════╝╚══ ═ ═╝

""")
print("Folder path example: /home/user/Downloads/")
folder_path = input("Please specify the directory path you wish to organize:")

print("""
========================================
        FILE ORGANIZER STARTED
========================================
""")


files = []

if os.path.exists(folder_path):
    for file in os.listdir(folder_path):
        full_path = folder_path + "/" + file
        if os.path.isfile(full_path):
            files.append(file)

else:
    print("This folder does not exist")

categorized_files = {}

for file in files:
    name = os.path.splitext(file)
    ext = name[1]
    if ext in categorized_files:
        categorized_files[ext].append(file)
    else:
        categorized_files[ext] = [file]

extension_map = {
    # Audio
    ".mp3": "Music",
    ".wav": "Music",
    ".aac": "Music",
    ".flac": "Music",
    ".ogg": "Music",
    ".m4a": "Music",
    ".wma": "Music",
    # Video
    ".mp4": "Videos",
    ".mkv": "Videos",
    ".avi": "Videos",
    ".mov": "Videos",
    ".webm": "Videos",
    ".flv": "Videos",
    ".wmv": "Videos",
    ".m4v": "Videos",
    # Images
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".bmp": "Images",
    ".webp": "Images",
    ".tiff": "Images",
    ".svg": "Images",
    # Documents
    ".txt": "Documents",
    ".pdf": "Documents",
    ".doc": "Documents",
    ".docx": "Documents",
    ".odt": "Documents",
    ".rtf": "Documents",
    ".md": "Documents",
    # Spreadsheets / Data
    ".xls": "Documents",
    ".xlsx": "Documents",
    ".csv": "Documents",
    ".ods": "Documents",
    # Presentations
    ".ppt": "Documents",
    ".pptx": "Documents",
    ".odp": "Documents",
    # Archives
    ".zip": "Archives",
    ".rar": "Archives",
    ".7z": "Archives",
    ".tar": "Archives",
    ".gz": "Archives",
    ".bz2": "Archives",
    # Applications
    ".apk": "Apps",
    ".exe": "Apps",
    ".msi": "Apps",
    ".deb": "Apps",
    ".rpm": "Apps",
    ".appimage": "Apps",
    # Disk Images
    ".iso": "Others",
    ".img": "Others",
    # Code
    ".py": "Code",
    ".js": "Code",
    ".html": "Code",
    ".css": "Code",
    ".json": "Code",
    ".xml": "Code",
    ".sh": "Code",
    ".c": "Code",
    ".cpp": "Code",
    ".java": "Code",
}


for key, value in categorized_files.items():
    if key in extension_map:
        folder_name = extension_map[key]
        new_folder_path = folder_path + "/" + folder_name

        if not os.path.exists(new_folder_path):
            os.makedirs(new_folder_path)

        for file in value:
            print(f"Moving {file}  -->  {folder_name}/")
            source_path = folder_path + "/" + file
            destination_path = new_folder_path + "/" + file
            os.rename(source_path, destination_path)

    else:
        folder_name = "others"


print("""
[======================================]
[  STATUS : FOLDER ORGANIZED COMPLETE  ]
[======================================]
""")

print(f"Completed at {time.strftime('%Y-%m-%d %H:%M:%S')}")
