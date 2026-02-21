import argparse
import re
from collections import Counter

def main(file, words=None, top=None):
    word_count = word_counter(file)

    # If no arguments are supplied, print out the count for each word in the file.
    if not words and not top:
        print('Word Count: ')
        for word in word_count:
            print(f'{word} : {word_count.get(word)}')

    # If one or more -w argument is supplied, runs case insensitive search for the word using the result from word_counter(). If found, print the word and the number of times it appears.        
    if words:
        for item in words:
            item = item.lower()
            print(f'Searching for word "{item}" in [{file}]...\n')
            count = word_count.get(item)
            if count:
                print(f'Word "{item}" found:\n{item} : {count}\n')
            else:
                print(f'"{item}" not found in [{file}].\n')
    
    # if the -t argument is supplied, print the top(t) number of words in the file along with the count for each.
    if top:
        most_common = word_count.most_common(top)
        print(f'Top {top} words:')
        for w, count in most_common:
            print(f'{w} : {count}')

def word_counter(file):
    with open(file, 'r') as f:
        text = f.read().lower() 
        words = re.findall(r"[a-z]+(?:'[a-z]+)?", text) #find all words, including words with apostrophes. This normalizes the words in the file, removing whitespace and punctuation.
        return Counter(words) # Create a dictionary with each word and it's count for each word in the input file.
    
if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', required=True, help='Path to input file')
    parser.add_argument('-w', '--words', action='append', help='Optional word to search for')
    parser.add_argument('-t', '--top', type=int, help='Identify the top n number of words.')
    args = parser.parse_args()
    main(args.file, args.words, args.top)

# 2/19/2026
# Working on practicing more with dictionaries. In this task, we built a slightly more robust command-line word counter.
# This word counter accepts a text file as input, along with an optional word to search for. If no word is given,
# it will return the count of every word in the file.  
# 
# 2/20/2026
# Added a bit more functionality to the code. Ajusted the --words parser using action-'append' to allow
# it to accept the words argument more than once, and adjusted the logic in main to account for more than one possible word.            
               
