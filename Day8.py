#Day 8 Task: Convert a CSV of users into a list of dictionaries. I went a bit further than the task requirement,
# and added a function to get a list of IT workers from our list of dictionaries. Ideas for improvement: Add
# functions to retrieve and store various categories of data from our list of dictionaries. 

import csv

def main():
    users = read_csv(r"D:\Scripts\Python\100 Days of Python\sample_users.csv")
    # it_users = get_it_users(r"D:\Scripts\Python\100 Days of Python\sample_users.csv")
    all_departments = [user['Department'] for user in users]
    for user in users:
        print(f"Name: {user['Full Name']}\nDepartment: {user['Department']}")
    print(f'Departments:\n {set(all_departments)}')

# Open the CSV file, which contains a list of employee names, start dates, etc, and use csv.DictReader() to create a
# dictionary reader object, and convert that to a list of dictionaries, with each dictionary representing a
# single employee. Return the list of dictionaries.
def read_csv(csv_file):
    with open (csv_file, newline='') as f:
        users = list(csv.DictReader(f))
    return users 

# Take the list of dictionaries from read_csv(), and create another list of dictionaries with just IT employees.
# Return that list.
def get_it_users(file): 
    users = read_csv(file) 
    it_users = [user for user in users if user['Department'] == 'IT']
    return it_users

if __name__ == '__main__':
    main()

#Lessons Learned today: 
# More list comprehension. I struggled wrapping my head around how to retrieve specific fields and values
# from our list of dictionaries. List comprehension appears to be a good way to achieve that. Specifically:
# new_list = [item for item in list if item['Field'] == 'value']. This of course requires that I know what 
# the possible fields and values are in my CSV file. An interesting challenge would be to retrieve the available 
# fields and values from a file where I don't know the options. 