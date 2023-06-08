# Script created by https://github.com/elclay7 with the help of ChatGPT
import hashlib
import os

# Define the directories to search
directories_to_search = ['/dir1', '/dir2']
# Specify the path of the stored hashes file
output_file_path = '/hash.txt'

def save_file_hashes(directories, output_file):
    with open(output_file, 'w') as f:
        for directory in directories:
            for root, dirs, files in os.walk(directory):
                for file in files:
                    file_path = os.path.join(root, file)
                    with open(file_path, 'rb') as file_obj:
                        content = file_obj.read()
                        hash_value = hashlib.sha256(content).hexdigest()
                        f.write(f"{file_path}: {hash_value}\n")

# Call the function to save the file hashes
save_file_hashes(directories_to_search, output_file_path)