import os
import re
dir_path = os.path.dirname(os.path.realpath(__file__))

# Part 1

def addToStacks(line: str, stacks: list[list[str]]) -> list[list[str]]:
    for idx in range(int(len(line) / 4)):
        if (line[idx * 4 + 1] != ' '):
            stacks[idx].insert(0, line[idx * 4 + 1])
    return stacks

def printState(stacks: list[list[str]]) -> list[list[str]]:
    maxHeight = max([len(stack) for stack in stacks])
    for idx in reversed(range(maxHeight)):
        for stack in stacks:
            if (len(stack)) >= idx + 1:
                print(f'[{stack[idx]}] ', end='')
            else:
                print('    ', end='')
        print('')
    print('')

        

with open(f'{dir_path}/input.txt') as file:
    lines = file.readlines()
    stacks = [[] for _ in range (int(len(lines[0]) / 4))]
    shouldKeepParsing = True
    for line in lines:
        if shouldKeepParsing and line.strip()[0] == '1':
            shouldKeepParsing = False
        if shouldKeepParsing:
            stacks = addToStacks(line, stacks)
        elif line[0] == 'm':
            movingInfo = re.match(r"move (?P<amount>[-+]?\d+) from (?P<origin>[-+]?\d+) to (?P<destination>[-+]?\d+)", line)
            for _ in range(int(movingInfo["amount"])):
                stacks[int(movingInfo["destination"]) - 1].append(stacks[int(movingInfo["origin"]) - 1].pop())
    print(''.join([each[len(each) - 1] for each in stacks]))

# Part 2

    stacks = [[] for _ in range (int(len(lines[0]) / 4))]
    shouldKeepParsing = True
    for line in lines:
        if shouldKeepParsing and line.strip()[0] == '1':
            shouldKeepParsing = False
        if shouldKeepParsing:
            stacks = addToStacks(line, stacks)
        elif line[0] == 'm':
            movingInfo = re.match(r"move (?P<amount>[-+]?\d+) from (?P<origin>[-+]?\d+) to (?P<destination>[-+]?\d+)", line)
            destination = int(movingInfo["destination"]) - 1
            origin = int(movingInfo["origin"]) - 1
            amount = int(movingInfo["amount"])
            tmp = []
            for each in range(amount):
                tmp.append(stacks[origin].pop())
            stacks[destination] += reversed(tmp)
    print(''.join([each[len(each) - 1] for each in stacks]))

