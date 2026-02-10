# Time to start learning command line arguments. The goal for this exercise is to create a script
# that will accept a file name and a key word, and count how many times the key word appears in the file.

import argparse

def main():

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

if __name__ == '__main__':
    parser = argparse.ArgumentParser(help="Takes a file and a word, and case-insensitively counts the number occurences of that word in the file." )
    parser.add_argument('file', type=str)
    parser.add_argument('word', type=str)

# 2/09/26: This code is not complete, but it's a start. 
