#Day 4 task: Extract all email addresses from text

import re

def main():
    email_addresses = extract_email_addresses(r"D:\Scripts\Python\100 Days of Python\Day4.txt")
    unique_emails = extract_unique_email_addresses(email_addresses)
    
    #print each email on a new line
    for email in unique_emails:
        print(email)


def extract_email_addresses(file): 
    #open the provided file in read-only mode and save to variable 'f'
    with open(file, 'r') as f:
        #read the file, and remove all soft line breaks and HTML junk
        text = f.read().replace('=\n', '').replace('=20', ' ').replace('&nbsp;', '') 
        #use regex to extract all email addresses. Since read() creates a single string from a file, we only run re.findall() once.
        email_addresses = re.findall(r'(?:[A-Za-z0-9!#$%&*+-/?^_.`{|}~]+@[A-Za-z0-9-_]+\.)(?:[A-Za-z]{2,})', text) 
        #returns the extracted email addresses in a list object (which is the default behavior for re.findall()).   
        return email_addresses 
    
def extract_unique_email_addresses(a):
    #Returns list of unique email addresses
    a = set(a)
    return a

if __name__ == '__main__':
    main()

