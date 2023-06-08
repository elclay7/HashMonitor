import hashlib
import os

# Define the directories to search
directories_to_search = ['/dir1', '/dir2']
# Specify the path of the stored hashes file
output_file_path = '/hash.txt'

def save_file_hashes(directories, output_file):
    success = True
    with open(output_file, 'w') as f:
        for directory in directories:
            for root, dirs, files in os.walk(directory):
                for file in files:
                    file_path = os.path.join(root, file)
                    with open(file_path, 'rb') as file_obj:
                        content = file_obj.read()
                        try:
                            hash_value = hashlib.sha256(content).hexdigest()
                            # Write the file path and hash value to the output file
                            f.write(f"{file_path}: {hash_value}\n")
                        except Exception as e:
                            success = False
                            break

    if success:
        print("Hashes generated successfully.")
    else:
        print("Failed to generate hashes for some files.")

# Call the function to save the file hashes
save_file_hashes(directories_to_search, output_file_path)