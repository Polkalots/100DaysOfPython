#Day 7 Task: Build a simple "log cleaner" that removes empty lines & comments.

import re

def main():
    cleaned_log = get_log_file(r"D:\Scripts\Python\100 Days of Python\debug_sample.log")
    print(''.join(cleaned_log))

def get_log_file(file_path):
    with open(file_path, 'r') as file:
        # open() returns an iterable file object. Here, I'm telling python to add each line from the file object
        # into a list only if the line does not start with '#' or is not an empty line. 
        log_lines = [line for line in file if not line.strip().startswith('#') and not line.strip() == '']
    return log_lines

if __name__ == '__main__':
    main()

# Lessons learned:
# Reinforced list comprehension with Python a bit more. 
# Reinforced the use of strip() for removing white space at the beginning and ends of strings.
# Learned that there is a function, startswith(), that checks for specific characters at the beginning of a string. 
# Reinforced use of the join() function. In this case, join() was used to concatenate the items in the list object that was returned by the get_log_file() function.
