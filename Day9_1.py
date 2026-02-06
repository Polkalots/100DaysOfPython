# This is just a bit of extra practice for Day 9 concepts. 

import json

def sanitize_logs(f):
    sanitized_values = []
    with open(f) as f:
        for line in f:
            if not line.strip():
                continue
            #Take each line in the file, and convert it to a dictionary using json.loads()
            data = json.loads(line)
            # Create an empty dictionary named sanitized
            sanitized = {}
            # Using the data dictionary, replace the value for every key with ***
            for key in data:
                sanitized[key] = "***"
            sanitized_values.append(sanitized)
    # I think you can probably figure this one out.
    print(sanitized_values)

sanitize_logs(r"D:\Scripts\Python\100 Days of Python\firewall_traffic.log")

# Lessons learned today:
# Today I decided to do some more practice with a bit of the json and dictionary stuff I learned yesterday.
# In this case, I wanted to find a way to sanitize a log file for sharing. I sanitized the whole file this time,
# but this definitely needs to be expanded to only sanitize certain fields. For example, we could remove fields that reveal 
# sensitive data about my environment, users, etc.