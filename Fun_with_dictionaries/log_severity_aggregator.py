# Task: Create a dictionary mapping log level → count. Output results sorted by frequency.
import csv
import argparse
from collections import Counter

def main(file):
    log_file = count_log_levels(file)
    #for line in log_file:
        #print(line)

def count_log_levels(file):
    level_values = {}
    with open(file, newline='') as f:
        log_file = csv.DictReader(f)
        for line in log_file:
            # for item in line:
            #     print(line.get(item))
            level = line['Level']
            if level not in level_values:
                level_values[level] = 1
            else:
                level_values[level] += 1
    print(level_values)
    #return log_file

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', required=True)
    parser.add_argument('-l', '--level', action='append', help='Accepts a case-sensitive string matching a log level. Options are "Error", "Info" and "Warning"')
    args = parser.parse_args()

    main(args.file, args.level)

    # 2/21/2026: Getting some more practice working with dictionaries and csv files.
    # Today I started a script that will collect and count the different log levels from an apache log csv file.
    # I'll be adding more to it, but this is a start.