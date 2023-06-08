### Features

- Monitoring files using hashes.
- Notifications via mail when finding a new or modified file.

### What I need

+ Linux server
+ Python3
    + hashlib
    + os
    + smtplib

### How does it work

The repo contains 2 scripts:

- **hashcreation.sh** - Finds the hashes of all files found in the selected directories and saves those hashes to the file hash.txt
- **hashmonitor.sh** - Looks up the hashes of all files in the selected directories and compares them with those stored in hash.txt

Will notify you by mail when:

- **Files changed**: The hash found does not match the one stored in hash.txt
- **New files**: Found hash does not exist in hash.txt

### Run for tests

`python3 hashcreation.sh`

`python3 hashmonitor.sh`

both scripts have verbose.

### Running in production

1. **Creation of the hashes:** the creation of the hash must be executed manually **hashcreation.sh** as long as we are sure that our site is clean and run it every time we make a modification to a file that is found within the monitored directories.
2. **Search for new or changed files:** Execute the **hashmonitor.sh** script via crontab

`0 */1 * * * python3 /hashmonitor.sh`

If it finds any modified or new file, it will be notified via email.

#### Important:
- The directories to monitor/exclude must be set in the code of the scripts.
- The file where the hashes will be stored must be created manually and its path must be set in the script.