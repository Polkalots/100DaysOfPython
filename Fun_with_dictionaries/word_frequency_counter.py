import argparse
import re
from collections import Counter

def main(file, word=None):
    word_count = word_counter(file)
    if word:
        print(f'Searching for word {word} in {file}...')
        if word in word_count:
            print(f'{word} : {word_count.get(word)}')
        else:
            print(f'{word} not found in {file}.')
    else:
        print('Word Count: ')
        for word in word_count:
            print(f'{word} : {word_count.get(word)}')

def word_counter(file):
    with open(file, 'r') as f:
        text = f.read().lower() 
        words = re.findall(r"[a-z]+(?:'[a-z]+)?", text) #find all words, including words with apostrophes. This normalizes the words in the file, removing whitespace and punctuation.
        return Counter(words) # Create a dictionary with each word and it's count for each word in the input file.
    
if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', required=True, help='Path to input file')
    parser.add_argument('-w', '--word', help='Optional word to search for')
    args = parser.parse_args()
    main(args.file, args.word)

# 2/19/2026
# Working on practicing more with dictionaries. In this task, we built a slightly more robust command-line word counter.
# This word counter accepts a text file as input, along with an optional word to search for. If no word is given,
# it will return the count of every word in the file.              
               
