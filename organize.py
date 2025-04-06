# Author : Noah Strekow
# Description : Sorts the files in target directory to proper Home directory subfolders

import os


# Store file locations
script_dir = os.getcwd()
target = "C:/Users/NOST/Downloads/"
target_dir = os.fsencode(target)

# Folders & Dictionary of file extensions
folders = ["C:/Users/NOST/Downloads/Documents/", "C:/Users/NOST/Downloads/Pictures/", "C:/Users/NOST/Downloads/Videos/", "C:/Users/NOST/Downloads/Music/"]
for folder in folders:
    os.mkdir(folder)
file_exts = {
    # Documents
    'pdf': folders[0],
    'doc': folders[0],
    'docx': folders[0],
    'txt': folders[0],
    'html': folders[0],
    # Data
    'csv': folders[0],
    'xlsx': folders[0],
    'log': folders[0],
    'bin': folders[0],
    'iso': folders[0],
    # Programs
    'c': folders[0],
    'py': folders[0],
    'css': folders[0],
    'js': folders[0],
    'jar': folders[0],
    'java': folders[0],
    # Archives
    'zip': folders[0],
    'rar': folders[0],
    '7z': folders[0],
    # Images
    'png': folders[1],
    'jpg': folders[1],
    'jpeg': folders[1],
    'gif': folders[1],
    'avif': folders[1],
    'svg': folders[1],
    'webp': folders[1],
    'psd': folders[1],
    'csp': folders[1],
    'xcf': folders[1],
    # Videos
    'mp4': folders[2],
    'mov': folders[2],
    'flv': folders[2],
    'avi': folders[2],
    'wmv': folders[2],
    'webm': folders[2],
    # Audio
    'mp3': folders[3],
    'wav': folders[3],
    'ogg': folders[3],
    # Leave other files in Target folder
}


# Check file type for every file in target directory, move file to proper subfolder
if __name__ == '__main__':
    for file in os.listdir(target_dir):
        filename = os.fsdecode(file)
        filename_split = filename.split('.')
        if len(filename_split) == 1:
            continue    # If no extension, skip
        ext = filename_split[len(filename_split)-1]   # Grab extension
        dest = file_exts.get(ext, target)   # Find where file should go according to extension, defualt = Misc
        print(f'{target_dir}, {filename}, {ext}, {dest}')
        os.rename(f"{target}{filename}", f"{dest}{filename}")    # Move file 
