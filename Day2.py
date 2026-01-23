#Task: Count how many times each word appears in a file (simple frequency counter).
"""With this task, I've learned a bit more about list comprehension in Python, and using loops with list
comprehension. I also learned about the Counter() function that will create a dictionary with the count 
of each item in the dictionary. """

from collections import Counter

def main():
    words = get_words(r"D:\Scripts\Python\100 Days of Python\Day2.txt")
    count = get_word_count(words)
    
    for word, freq in count.items():
        print(f"{word}: {freq}")

#Accepts file as parameter, and uses list comprehension to normalize each word in the file.
def get_words(a):
    with open(a, 'r') as file:
        words = [word.lower().rstrip(',:.; ') for word in file.read().split()]
        return words

"""Counter returns a dictionary object with the count for each key in the list. In this case it will take as
input the 'words' variable from main() and will count each word in the list, returning a dictionary with 
each word as the key, and the count as the value."""
def get_word_count(b):
    return Counter(b)
    

if __name__=='__main__':
    main()
