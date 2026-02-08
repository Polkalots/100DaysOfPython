import re

def main():
    ip_address_list = get_ip_addresses(r'D:\Scripts\Python\100 Days of Python\Day3.txt')
    for address in ip_address_list:
        print(f"{address}")

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