import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

# PART 1
SCORE_SCALE = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

with open(f'{dir_path}/input.txt') as file:
    sharedItems = []
    rucksacks = file.readlines()
    for rucksack in rucksacks:
        firstCompartment = rucksack[0:int(len(rucksack) / 2)]
        secondCompartment = rucksack[int(len(rucksack) / 2):]
        for item in secondCompartment:
            if item in firstCompartment:
                sharedItems.append(item)
                break
    
    score = sum([SCORE_SCALE.index(item) + 1 for item in sharedItems])
    print(f'Part 1 {score}')

# PART 2

    sharedItems = []
    for idx in range(int(len(rucksacks) / 3)):
        for item in rucksacks[idx * 3]:
            if item in rucksacks[(idx * 3) + 1] and item in rucksacks[(idx * 3) + 2]:
                sharedItems.append(item)
                break
    score = sum([SCORE_SCALE.index(item) + 1 for item in sharedItems])
    print(f'Part 2 {score}')

    