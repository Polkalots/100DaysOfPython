# Day 11 Task: Build a simple menu-based CLI (text menu with numbered options).
# This is about as simple as it gets. Menu inlcudes the option to say hello, or roll the dice.

import argparse
import random

def main(answer):
    if answer == '1':
        print("Hello there!")
    elif answer == '2':
        dice = input('How many sides does the die have?\n1) 6\n2) 12\n3) 20\n')
        if dice == '1':
            roll = random.randint(1, 6)
            print(f'You rolled a {roll}.')
        elif dice == '2':
            roll = random.randint(1, 12)
            print(f'You rolled a {roll}.')
        elif dice == '3':
            roll = random.randint(1,20)
            print(f'You rolled a {roll}.')
        else:
            print('That is not an available option.')
    else:
        print('That is not an available option.')


if __name__=='__main__':
    main(input(f'What would you like to do?\n1) Say Hello\n2) Roll the dice\n'))