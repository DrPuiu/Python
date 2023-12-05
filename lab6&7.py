#Exercitiul 1 tema 6
import os
import sys

def read_and_print_files(directory_path, file_extension):
    try:
        
        if not os.path.isdir(directory_path):
            raise FileNotFoundError(f"Directory not found: {directory_path}")

       
        for filename in os.listdir(directory_path):
            file_path = os.path.join(directory_path, filename)

        
            if os.path.isfile(file_path) and filename.endswith(file_extension):
                try:
                    with open(file_path, 'r') as file:
                        contents = file.read()
                        print(f"Contents of {filename}:\n{contents}\n{'-'*30}")
                except Exception as e:
                    print(f"Error reading file {filename}: {e}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <directory_path> <file_extension>")
    else:
        directory_path = sys.argv[1]
        file_extension = sys.argv[2]
        read_and_print_files(directory_path, file_extension)

#Exercitiul 2 tema 6
import os
import sys

def rename_files_with_sequence(directory_path):
    try:
        
        if not os.path.isdir(directory_path):
            raise FileNotFoundError(f"Directory not found: {directory_path}")

        
        files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]

        
        for i, filename in enumerate(files, start=1):
            try:
                
                new_filename = f"file{i}_{filename}"
                
                
                os.rename(os.path.join(directory_path, filename), os.path.join(directory_path, new_filename))

                print(f"Renamed {filename} to {new_filename}")
            except Exception as e:
                print(f"Error renaming file {filename}: {e}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
    else:
        directory_path = sys.argv[1]
        rename_files_with_sequence(directory_path)


#Exercitiul 3 tema 6
import os
import sys

def calculate_total_size(directory_path):
    try:
        if not os.path.exists(directory_path) or not os.path.isdir(directory_path):
            raise FileNotFoundError(f"Directory not found: {directory_path}")

        total_size = 0

        for root, dirs, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)

                try:
                    file_size = os.path.getsize(file_path)
                    total_size += file_size
                except Exception as e:
                    print(f"Error getting size of file {file_path}: {e}")

        print(f"Total size of all files in {directory_path}: {total_size} bytes")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
    else:
        directory_path = sys.argv[1]
        calculate_total_size(directory_path)


#Exercitiul 4 tema 6
import os
import sys

def count_files_by_extension(directory_path):
    try:
        if not os.path.exists(directory_path) or not os.path.isdir(directory_path):
            raise FileNotFoundError(f"Directory not found: {directory_path}")

        file_counts = {}

        for root, dirs, files in os.walk(directory_path):
            for file in files:
                _, file_extension = os.path.splitext(file)
                file_extension = file_extension.lower()

                if file_extension not in file_counts:
                    file_counts[file_extension] = 1
                else:
                    file_counts[file_extension] += 1

        if not file_counts:
            print(f"No files found in {directory_path}")
        else:
            print("File counts by extension:")
            for extension, count in file_counts.items():
                print(f"{extension}: {count}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
    else:
        directory_path = sys.argv[1]
        count_files_by_extension(directory_path)


#Exercitiul 1 tema 7
import csv

def read_csv(file_path):
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        data = [row for row in csv_reader]

    return header, data
# csv_validator/csv_validator/validator.py

def check_missing_values(data):
    for row_index, row in enumerate(data, start=2):  # Start from 2 to account for the header
        for col_index, value in enumerate(row):
            if not value:
                print(f"Missing value in row {row_index}, column {col_index + 1}")

def check_data_types(data, expected_types):
    for row_index, row in enumerate(data, start=2):
        for col_index, (value, expected_type) in enumerate(zip(row, expected_types)):
            if expected_type and not isinstance(value, expected_type):
                print(f"Invalid data type in row {row_index}, column {col_index + 1}. Expected {expected_type}, got {type(value)}")

# csv_validator/setup.py
from setuptools import setup, find_packages

setup(
    name='csv_validator',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # Any dependencies your package may need
    ],
)

#Exercitiul 3 tema 7
# text_file_merger/text_file_merger/merger.py

from .utils import read_file_content, write_merged_file

def merge_text_files(file_paths, output_file, separator='\n'):
    merged_content = ''

    for file_path in file_paths:
        content = read_file_content(file_path)
        merged_content += content + separator

    write_merged_file(output_file, merged_content)

# text_file_merger/text_file_merger/utils.py

def read_file_content(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def write_merged_file(output_file, content):
    with open(output_file, 'w') as file:
        file.write(content)
# text_file_merger/setup.py
from setuptools import setup, find_packages

setup(
    name='text_file_merger',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # Any dependencies your package may need
    ],
)

#Exercitiul 4 tema 7
# text_file_merger/setup.py
from setuptools import setup, find_packages

setup(
    name='text_file_merger',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # Any dependencies your package may need
    ],
)
# secure_password_generator/setup.py
from setuptools import setup, find_packages

setup(
    name='secure_password_generator',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # Any dependencies your package may need
    ],
)
# Example usage
from secure_password_generator.secure_password_generator import password_generator

# Generate a password with default settings
password = password_generator.generate_password()
print(f"Generated Password: {password}")

# Generate a password with custom settings
custom_password = password_generator.generate_password(
    length=16, include_special_chars=True, include_numbers=True, include_uppercase=True
)
print(f"Custom Password: {custom_password}")
