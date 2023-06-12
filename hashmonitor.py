# Script created by https://github.com/elclay7 with the help of ChatGPT
import hashlib
import os
import smtplib
from email.mime.text import MIMEText
import requests

# Search directories
directories_to_search = ['/dir1', '/dir2']
# Directories to exclude
excluded_directories = ['/dir1/a', '/dir1/b']
# Hash file path
hash_file_path = '/hash.txt'

# Telegram conf
telegram_token = 'YOUR_TELEGRAM_BOT_TOKEN'
telegram_chat_id = 'YOUR_TELEGRAM_CHAT_ID'

def calculate_file_hash(file_path):
    with open(file_path, 'rb') as file_obj:
        content = file_obj.read()
        hash_value = hashlib.sha256(content).hexdigest()
        return hash_value

# Mail conf
def send_email(subject, body):
    sender = 'some@email.com'
    receiver = 'some@email.com'
    smtp_server = 'smtp.email.com'
    smtp_port = 587
    username = 'some@email.com'
    password = 'password' 

    message = MIMEText(body)
    message['Subject'] = subject
    message['From'] = sender
    message['To'] = receiver
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(username, password)
        server.send_message(message)

def send_telegram_message(message):
    url = f'https://api.telegram.org/bot{telegram_token}/sendMessage'
    data = {
        'chat_id': telegram_chat_id,
        'text': message
    }
    response = requests.post(url, json=data)
    if response.status_code != 200:
        print(f"Failed to send Telegram message. Error code: {response.status_code}")

def compare_file_hashes(directories, hash_file):
    modified_files = []
    new_files = []
    stored_hashes = {}
    with open(hash_file, 'r') as f:
        for line in f:
            file_path, hash_value = line.strip().split(': ')
            stored_hashes[file_path] = hash_value
    
    for directory in directories:
        for root, dirs, files in os.walk(directory):
            dirs[:] = [d for d in dirs if os.path.join(root, d) not in excluded_directories]
            
            for file in files:
                file_path = os.path.join(root, file)
                if file_path in stored_hashes:
                    stored_hash = stored_hashes[file_path]
                    calculated_hash = calculate_file_hash(file_path)
                    if stored_hash != calculated_hash:
                        modified_files.append(file_path)
                        print(f"Modified file: {file_path}")
                else:
                    new_files.append(file_path)
                    print(f"New file: {file_path}")
    
    return modified_files, new_files

print("Comparing file hashes...")

modified_files, new_files = compare_file_hashes(directories_to_search, hash_file_path)

subject = 'File Hash Comparison'
body = ''

if modified_files:
    body += 'Modified files:\n'
    body += '\n'.join(modified_files)
    body += '\n\n'
    print("Modified files found.")

if new_files:
    body += 'New files:\n'
    body += '\n'.join(new_files)
    print("New files found.")

if modified_files or new_files:
    send_email(subject, body)
    send_telegram_message(f"{subject}\n\n{body}")
    print("Email and Telegram notification sent.")
else:
    print("No modified or new files found.")