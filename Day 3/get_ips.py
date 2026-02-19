#Day 3 Task: Extract all IP addresses from a text or csv file. See comments at the bottom. 

import re
from pathlib import Path
import ipaddress
import csv
import argparse

def main(file):
    extension = get_file_ext(file)
    if extension == '.txt':
        ip_addresses = get_ip_addresses_txt(file)
        print(ip_addresses)
    elif extension == '.csv':
        ip_addresses = get_ip_addresses_csv(file)
        for column, ips in ip_addresses.items():
            print(f'{column}:')
            for ip in ips:
                print(ip)

    #ip_address_list = get_ip_addresses(r"file path")
    #for address in ip_address_list:
        #print(f"{address}")
    #print(get_file_ext(r"file path"))

#Get the file extension for handling of various file types
def get_file_ext(file_name):
    ext = Path(file_name).suffix
    return ext

#Uses csv.reader() to retrieve each row of the file, and next() to return the first row with the header names.
def get_csv_column_names(csv_file):
    with open(csv_file, newline='') as f:
        rows = csv.reader(f)
        headers = next(rows)
        return headers
    
def get_ip_columns(csv_file):
    with open(csv_file, newline='') as f:
        rows = csv.DictReader(f)
        ip_columns = {}
        row_count = 0
        for row in rows:
            for column, value in row.items():
                try:
                    ipaddress.ip_address(value) # Test the value in each column to see if it's an IP address
                    if column not in ip_columns: #If it is a valid IP address, this part checks to see if the column name is in the ip_columns dictionary. If not, it adds it, and adds a count of 1.
                        ip_columns[column] = 1
                    else:
                        ip_columns[column] += 1 # If the column name is already in the dictionary, it increases the count by 1.
                except ValueError:
                    pass
            row_count += 1
            if row_count > 100: # I only want to sample the first 100 rows of the file. This will break the loop once 100 rows have been examined.
                break

        valid_columns = []
        for item, value in ip_columns.items(): # Here we are checking to see what percentage of each column is valid IP addresses. If more than 70% of the column is IP addresses, that's a good indicator that it's a valid "IP Address" column.
            percentage = value/row_count
            if percentage >= .70:
                valid_columns.append(item)
        return valid_columns
    
def get_ip_addresses_csv(csv_file):
        ip_columns = get_ip_columns(csv_file) # Calls the function to find which columns are valid IP address columns
        with open(csv_file, newline='') as f:
            rows = csv.DictReader(f) # Creates dict object from eac row in the file
            column_names_values = {}
            for row in rows: # Loop over each row in the file
                for column, value in row.items(): # Loop over each column in each row
                    if column in ip_columns: # Check each column to see if it's an IP Address column
                        if column not in column_names_values: #creates a nested dictionary with the column name and a list of IP addresses for each column name.
                             column_names_values[column] = [value]
                        else:
                            column_names_values[column].append(value)
        return column_names_values
            
def get_ip_addresses_txt(a):
    ip_addresses = []
    with open(a, 'r') as file:
        for line in file:
            match = re.search(r'\b(?:(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.){3}(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\b', line)
            if match:
                ip_addresses.append(match.group())
    return ip_addresses

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', required=True)
    args = parser.parse_args()
    main(args.file)


# 2/11/2026:
# Working on adding some more functionality to the original Day 3 task. This time, I'm attempting to add
# the ability to detect the file type, and retrieve data depending on the file type. In working toward that
# today, I've learned a bit more about the csv module, specifically the csv.reader and next() functions. 
# Csv.reader returns lists of each row in the csv file. In this case, I'm using it to get the names of the
# csv header fields, using the next() function to return only the first row (which presumably has the headers).
# It's pretty messy at the moment, but I'm working on it.

# 2/18/2026
# I'm getting closer. Still working on wrapping my head around dictionary objects, and how to work with them. But I'm 
# starting to understand a bit more how to work with dictreader objects, looping first over each row then over
# each item in each row using .items() to retrieve each value. So far I've got it to where it will accept a file 
# as an argument, check the file extension, and handle either a csv or text file appropriately, printing off all 
# ip addresses in the file. Still messy, but better.