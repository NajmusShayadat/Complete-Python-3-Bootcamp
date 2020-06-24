# RegEx and OS module exercise
# Extract a zip file and search through the folder and files of the unzipped content and find a phone number in a file.

import shutil
import os
import re


def text_in_folders(file_path, pattern):
    """
    This function takes the a pattern and root directory.
    Creates file path for each files found in the folders and sub folders.
    Then open and read each file and search using Regular Expression
    Prints out the file path, filename and the found pattern
    """

    for folder, sub_folders, files in os.walk(file_path):

        for file in files:

            # Create path including filename
            filename = folder + '\\' + file

            with open(filename, 'r') as f:
                phone = re.search(pattern, f.read())
                if phone:
                    print('\n\nPhone number:\t' + phone.group() + '\n')
                    print('Folder path:\t:' + folder + '\n')
                    print('File name:\t' + file + '\n')
                    # break # break in case you need just one targeted pattern
                else:
                    continue


def grab_folder_name(a, b):
    """
    This function returns name of the unzipped files/folder by comparing before and
    after list of files/folders.
    """

    c = list((set(a) | set(b)) - (set(a) & set(b)))
    return c[0]


# Folder and file list from the working directory before and after unzipping
before = os.listdir()
shutil.unpack_archive("unzip_me_for_instructions.zip")
after = os.listdir()

# Find the unzipped folder name
content = grab_folder_name(before, after)

# Create the file path of thee working directory
fp = os.getcwd() + "\\" + content

# Read the Instructions.txt file
with open(fp + "\\" + 'Instructions.txt', 'r') as fl:
    print(fl.read())

# Set the pattern to look up in the text files
ptrn = r'\d{3}-\d{3}-\d{4}'

# Call the function to return the search result
text_in_folders(fp, ptrn)
