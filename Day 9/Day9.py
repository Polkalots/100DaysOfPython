#Day 9 Task: Read JSON logs and print specific fields
import json

def main():
   json_data = read_log_file(r"D:\Scripts\Python\100 Days of Python\firewall_traffic.log")
   for entry in json_data:
       print(entry['timestamp'])

def read_log_file(f):
    log_lines = []
    with open(f) as f:
        for line in f:
            if not line.strip():
                continue
            data = json.loads(line)
            log_lines.append(data)
    return log_lines

def get_denials(f):
    auth_fails = []
    with open(f) as f:
        # Iterate through each line in the file, and only process lines that are not empty.
        for line in f:
            if not line.strip():
                continue
            #Create dictionary for each json-formatted line in the provided log file
            data = json.loads(line)
            # Add each dictionary object where the "action" field is "DENY" to our auth_fails list
            if data['action'] == 'DENY':
                auth_fails.append(data)
        return auth_fails
        
def random_function(f):
    with open(f) as f:
        random_json_set = []
        sanitized_values = []
        for item in f:
            if not item.strip():
                continue
            data = json.loads(item)
            random_json_set.append(data)
            if data.get('src_ip'):
                print(data['src_ip'])
        for line in f:
            if not line.strip():
                continue
            data = json.loads(line)
            sanitized = {}
            for key in data:
                sanitized[key] = "***"
            sanitized_values.append(sanitized)
        print(sanitized_values)
        print(random_json_set)
        

# if __name__ == '__main__':
#     main()

# print(get_denials(r"D:\Scripts\Python\100 Days of Python\firewall_traffic.log"))

random_function(r"D:\Scripts\Python\100 Days of Python\firewall_traffic.log")

# This is still very much a work in progress. I'm trying to understand the logic behind working with json
# objects, but it's a start. What I think I understand so far is that json.loads creates a python-friendly 
# dictionary from a json object. https://docs.python.org/3/library/json.html#:~:text=of%20service%20attacks.-,json.loads(,-s%2C%20*