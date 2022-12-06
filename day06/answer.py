import os
import re
dir_path = os.path.dirname(os.path.realpath(__file__))

# Part 1

        

with open(f'{dir_path}/input.txt') as file:
    input = file.readlines()
    lastLetters = []
    print(dir_path)
    for idx, letter in enumerate(input[0]):
        if len(lastLetters) >= 4:
            lastLetters.pop(0)
        lastLetters.append(letter)
        if (len(set(lastLetters)) == 4):
            print(lastLetters)
            print(f'Part 1: {idx + 1}')
            break
    
# Part 2

    for idx, letter in enumerate(input[0]):
        if len(lastLetters) >= 14:
            lastLetters.pop(0)
        lastLetters.append(letter)
        if (len(set(lastLetters)) == 14):
            print(lastLetters)
            print(f'Part 2: {idx + 1}')
            break