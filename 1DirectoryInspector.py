"""
Task 1: Directory Inspector:
    - Problem Statement:
        - Create a Python script that lists all files and subdirectories in a given directory. Your script should prompt the user for the directory path and then display the contents.
    - Expected Outcome:
        - The script should correctly list all files and subdirectories in the specified directory. Handle exceptions for invalid paths or inaccessible directories.
"""
import os

dir_list = os.listdir("/Users/kelseaconrad/Desktop")
print(dir_list)


"""
Task 2: File Size Reporter:
    - Problem Statement:
        - Write a Python program that reports the sizes of all files in a specific directory. The program should ask the user for a directory path and then print each file's name and size within that directory.
    - Expected Outcome:
        - Your program should display the name and size (in bytes) of each file in the given directory. Ensure that the program only reports on files, not directories, and handles any errors gracefully.
"""


# def get_file_size(file_path):
#     try:
#         file_info = os.stat(file_path)
#         return file_info.st_size
#     except FileNotFoundError:
#         print(f"File {file_path} not found.")
#         return None
#
#
# directory_path = input("Please enter the directory path: ")
# if os.path.exists(directory_path) and os.path.isdir(directory_path):
#     for f in os.listdir(directory_path):
#         full_path = os.path.join(directory_path, f)
#         if os.path.isfile(full_path):
#             file_size = get_file_size(full_path)
#             if file_size is not None:
#                 print(f"Name: {f}, Size: {file_size} bytes")
# else:
#     print("The path provided does not exist or is not a directory.")


"""
Task 3: File Extension Counter:
    - Problem Statement:
        - Develop a Python script that counts the number of files of each extension type in a directory. For instance, in a directory with five '.txt' files and three '.py' files, the script should report "TXT: 5" and "PY: 3".
    - Expected Outcome:
        - The script should accurately count and display the number of files for each extension type in the specified directory. Handle different cases of file extensions (e.g., '.TXT' and '.txt' should be considered the same).
To Dos: 
- List the files, including their file type
    - splitext('filename'): returns a tuple: (filename, extension)
- Add each one to a list according to the file type.
- Count each list.
- Print out the report.
"""


def count_file_extensions(directory):
    extensions = []
    extension_dict = {}
    for item in os.listdir(directory):
        item = item.lower()
        extension = os.path.splitext(item)
        if extension[1] not in extension_dict:
            extension_dict[extension[1]] = 1
        elif extension[1] in extension_dict:
            extension_dict[extension[1]] += 1

    for item in extension_dict:
        print(f"{item}: {extension_dict[item]}")


if __name__ == "__main__":
    directory_needed = input("Please type the directory you need: ")
    count_file_extensions(directory_needed)
