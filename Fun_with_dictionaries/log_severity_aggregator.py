# Task: Create a dictionary mapping log level → count. Output results sorted by frequency.
import csv
import argparse
from collections import Counter

def main(file, level=None):
    level_count = count_log_levels(file)
    level_lines = find_levels(file, level)
    for l, c in level_count.items():
        print(f"Level:\n{l}:{c}\n")

    if level:
        if level_lines:
            for line in level_lines:
                print(line)
        else:
            print('Level not found.')
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
    return level_values

def find_levels(file, level):
    log_lines = []
    levels = []
    for item in level:
        levels.append(item.strip().lower())
    with open(file, newline='') as f:
        log_file=csv.DictReader(f)
        for line in log_file:
            if line['Level'].lower().strip() in levels:
                log_lines.append(line)
        return log_lines

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', required=True)
    parser.add_argument('-l', '--level', action='append', help='Accepts a case-sensitive string matching a log level. Options are "error", "notice" and "warning"')
    args = parser.parse_args()

    main(args.file, args.level)

    # 2/21/2026: Getting some more practice working with dictionaries and csv files.
    # Today I started a script that will collect and count the different log levels from an apache log csv file.
    # I'll be adding more to it, but this is a start.

    # 2/23/2026: Today I worked on adding functionality to search for and print specific log levels. 