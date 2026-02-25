# Task: Create a dictionary mapping log level → count. Output results sorted by frequency.
import csv
import argparse

def main(file, level=None):
    counts, lines = process_log(file, level)
    for l, c in counts.items():
        print(f"Level:\n{l}:{c}\n")

    if lines:
        for line in lines:
            print(line)
    else:
        print(f'Level {level} not found.')

def process_log(file, level):
    level_counts = {} # holds the overall count for each log severity level
    log_lines = [] # holds matches for the log levels that were searched for
    if level:
        levels = [item.strip().lower() for item in level] # Because the command accepts multiple log levels to search for, each 'level' argument is part of a list object.
    else:
        levels = [] # create an empty list if the level argument is not provided. This keeps the function from crashing later on.
    with open(file, newline='') as f:
        log_file = csv.DictReader(f)
        for line in log_file:
            row_level = line['Level'].strip().lower() # normalize the levels in the log file
            if row_level not in level_counts: # iterate through each line, and if the level for that line is not in the level_counts variable, add it and make its count 1.
                level_counts[row_level] = 1 
            else:
                level_counts[row_level] += 1 # if the level for a given line is in the level_counts variable, increase its count by 1.

            if levels and row_level in levels: # if the level argument is provided, check each line to see if it matches the provided level argument, and if so, add it to the log_lines variable.
                log_lines.append(line)
    return level_counts, log_lines

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