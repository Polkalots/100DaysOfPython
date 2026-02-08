#Task: Write a script that reads a text file and prints the number of lines.

def get_lines(file):
    with open(file, 'r') as text_file:
        lines = 0
        for line in text_file:
            lines += 1
        return lines
    
print(get_lines(r"[file path]"))



