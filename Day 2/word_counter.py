# Time to start learning command line arguments. The goal for this exercise is to create a script
# that will accept a file name and a key word, and count how many times the key word appears in the file.

import argparse

#def main():

# Take a file name and a keyword, and count how many exact matches to that keyword appear in the file.
# Normalizes words before searching for a match. 
def count_words(i, keyword):
    matches = 0
    keyword = keyword.lower()
    with open(i, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                word = word.lower().rstrip('.,!? :)(;')
                if word == keyword:
                    matches += 1
    return matches

#Creates argument parser to accept command line input. Positional arguments are file and word. 
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Receives a file and key word as input, and outputs the count for the keyword in the file.', epilog='Matching is case insensitive, and only matches on whole words.')
    parser.add_argument('file', type=str)
    parser.add_argument('word', type=str)
    args=parser.parse_args()

    print(f'Keyword count: {count_words(args.file, args.word)}')

# 2/09/26: This code is not complete, but it's a start. 
# 2/10/26: Managed to complete a very simple argument parser. 
