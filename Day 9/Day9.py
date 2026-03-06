#Day 9 Task: Read JSON logs and print specific fields
import json
import argparse

def main(file, denials=False, allowed=False, top_src=False, top_dst=False):
    json_data = read_log_file(file)
    for entry in json_data:
        print(entry['timestamp'])
    if denials:
        fails = get_denials(json_data)
    if allowed:
        allows = get_allows(json_data)
    if top_src:
        top_src_ips = get_top_src(json_data)
    if top_dst:
        top_dst_ips = get_top_dst(json_data)

    # print(type(json_data))
    # print(json_data)

def read_log_file(f):
    log_lines = [] # Creates a list that will be populated with dictionary entries from the log file
    with open(f) as f:
        for line in f:
            if not line.strip(): # skip past any empty lines in the file
                continue
            data = json.loads(line) # Creates a dictionary object with the log data.
            log_lines.append(data) # Adds the dictionary object to the log_lines list
    return log_lines

# Find all denied login attempts
def get_denials(data):
    auth_fails = []
    for line in data:
        action = line['action'].lower() # normalize search to allow for different log cases
        if action == 'deny':
            auth_fails.append(line)
    # for item in auth_fails:
    #     print(item)
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
        

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process firewall logs')
    parser.add_argument('-f', '--file', required=True, help='Path to the log file')
    parser.add_argument('-d', '--denials', action='store_true', help='Print denied entries')
    parser.add_argument('-a', '--allowed', action='store_true', help='Print allowed entrieds')
    parser.add_argument('-ts', '--top-src', type=int, help='Print the top n source IP addresses')
    parser.add_argument('-td', '--top-dst', type=int, help='Print the top n destination IP addresses')
    args = parser.parse_args()
    main(args.file, args.denials, args.allowed, args.top_src, args.top_dst)

# print(get_denials(r"D:\Scripts\Python\100 Days of Python\firewall_traffic.log"))

# random_function(r"D:\Scripts\Python\100 Days of Python\firewall_traffic.log")

# This is still very much a work in progress. I'm trying to understand the logic behind working with json
# objects, but it's a start. What I think I understand so far is that json.loads creates a python-friendly 
# dictionary from a json object. https://docs.python.org/3/library/json.html#:~:text=of%20service%20attacks.-,json.loads(,-s%2C%20*