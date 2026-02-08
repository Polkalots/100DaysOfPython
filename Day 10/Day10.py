# Day 10 Task: Create a script that flags lines containing suspicious keywords. I decided to create a script
# that looks for files that may contain cleartext passwords, as this is something I do regularly in my work,
# but with other tools.

import csv
import re

def main():
    password_files = find_creds(r"D:\Scripts\Python\100 Days of Python\dlp_file_activity_sample.csv")
    print("Likely password files found:")
    for file in password_files:
        print(file)

def find_creds(i):
    with open(i, newline='') as f:
        password_files = []
        file_paths = []
        # offending_users = {}
        file_event = csv.DictReader(f)
        for line in file_event:
            # users = line['username']
            file_paths.append(line['file_path'])
        
        for path in file_paths:
            match = re.findall(r'.*(password|login|credential|creds|secret|key|passwd).*', path)
            if match:
                password_files.append(path)

        return password_files

# find_creds(r"D:\Scripts\Python\100 Days of Python\dlp_file_activity_sample.csv")

if __name__ == "__main__":
    main()

# Lessons learned today:
# Although I didn't end up using it in the final working code, today I discovered the pathlib library, which 
# (for this case at least) is useful for removing file extensions from file names. However, because the file names
# for my sample file contained other words in addition to my trigger "password" words, I decided it would be better
# to use regex to find them and not worry about removing the file extensions.


            
            