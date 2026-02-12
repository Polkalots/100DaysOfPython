#Day 3 Task: Extract all IP addresses from a text file using regex. 

import re
from pathlib import Path
import ipaddress
import csv

def main():
    ip_address_list = get_ip_addresses(r"file path")
    for address in ip_address_list:
        print(f"{address}")
    print(get_file_ext(r"file path"))

#Get the file extension for handling of various file types
def get_file_ext(file_name):
    ext = Path(file_name).suffix
    return ext

#Uses csv.reader() to retrieve each row of the file, and next() to return the first row with the header names.
def get_csv_column_names(csv_file):
    with open(csv_file, newline='') as csv_file:
        rows = csv.reader(csv_file)
        headers = next(rows)
        return headers

    
# def get_ip_addresses_csv(i):
#     with open(i, newline='') as csv_file:
#         csv_file = csv.DictReader(csv_file)
#         headers = csv_file.fieldnames
#         for line in csv_file:
#             ip_match = ipaddress.ip_address(header)
            

def get_ip_addresses(a):
    ip_addresses = []
    with open(a, 'r') as file:
        for line in file:
            match = re.search(r'\b(?:(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.){3}(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\b', line)
            if match:
                ip_addresses.append(match.group())
    return ip_addresses

if __name__=='__main__':
    main()
    get_csv_column_names(r"file path")

# 2/11/2026:
# Working on adding some more functionality to the original Day 3 task. This time, I'm attempting to add
# the ability to detect the file type, and retrieve data depending on the file type. In working toward that
# today, I've learned a bit more about the csv module, specifically the csv.reader and next() functions. 
# Csv.reader returns lists of each row in the csv file. In this case, I'm using it to get the names of the
# csv header fields, using the next() function to return only the first row (which presumably has the headers).
# It's pretty messy at the moment, but I'm working on it.