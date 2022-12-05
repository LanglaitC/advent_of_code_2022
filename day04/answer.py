import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

# Part 1

def areOverlappingCompletely(firstPair: list[int], secondPair: list[int]) -> bool:
    return (firstPair[0] <= secondPair[0] and firstPair[1] >= secondPair[1]) or (secondPair[0] <= firstPair[0] and secondPair[1] >= firstPair[1])

def areOverlapping(firstPair: list[int], secondPair: list[int]) -> bool:
    return firstPair[1] >= secondPair[0] and firstPair[1] <= secondPair[1] or secondPair[1] >= firstPair[0] and secondPair[1] <= firstPair[1]

with open(f'{dir_path}/input.txt') as file:
    lines = file.readlines()
    score = 0
    for line in lines:
        pairs = [[int(pair.split('-')[0]), int(pair.split('-')[1])] for pair in line.strip().split(',')]
        if (areOverlappingCompletely(pairs[0], pairs[1])):
            score += 1
    print(f'Part 1 {score}')

# Part 2

    score = 0
    for line in lines:
        pairs = [[int(pair.split('-')[0]), int(pair.split('-')[1])] for pair in line.strip().split(',')]
        if (areOverlapping(pairs[0], pairs[1])):
            score += 1
    print(f'Part 2 {score}')
            