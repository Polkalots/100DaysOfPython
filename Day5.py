#Day 5 task: Identify the top 5 most common IPs in a log file.

import csv
from collections import Counter

def main():
    source_ips = extract_source_ips(r"C:\Users\Maurina\Downloads\sample packets.csv")
    dest_ips = extract_dest_ips(r"C:\Users\Maurina\Downloads\sample packets.csv")
    source_count = count_source_ips(source_ips)
    dest_count = count_dest_ips(dest_ips)
    top_five_sources = source_count.most_common(5)
    top_five_dest = dest_count.most_common(5)
    print(f'Top Five Source IP Addresses:')
    for ip, count in top_five_sources:
        print(f"{ip} : {count}")
    print(f"\nTop Five Destination IP Addresses:")
    for ip, count in top_five_dest:
        print(f"{ip} : {count}")
    
def extract_source_ips(csvfile):
    #open the csv log file, convert the data to a dictionary, and add all source IP addresses from that dictionary to a separate list.
    with open(csvfile, newline='') as file:
        pcap = csv.DictReader(file)
        source_ips = []
        for row in pcap:
            source_ips.append(row['Source IP'])
        return source_ips

def extract_dest_ips(csvfile):
    #open the csv log file, convert the data to a dictionary, and add all dest IP addresses from that dictionary to a separate list.
    with open(csvfile, newline='') as file:
        pcap = csv.DictReader(file)
        dest_ips = []
        for row in pcap:
            dest_ips.append(row['Destination IP'])
        return dest_ips
    
def count_source_ips(source_ips):
    #Accepts a list object and counts each item in that object, returning a dictionary with each item and its count
    ip_count = Counter(source_ips)
    return ip_count

def count_dest_ips(dest_ips):
    #Accepts a list object and counts each item in that object, returning a dictionary with each item and its count
    ip_count = Counter(dest_ips)
    return ip_count

if __name__ == '__main__':
    main()

# Lessons learned today:
# Working with CSV files:
# csv.DictReader() returns a dictionary object with the CSV column headers as keys, and the rows as values. 
# When working with CSV files, you need to use "newline=''" This prevents python from trying to handle the newline characters,
# since the CSV module already does that. 
