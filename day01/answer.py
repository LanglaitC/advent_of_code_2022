import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

with open(f'{dir_path}/input.txt') as file:
    lines = file.readlines()
    sums = [0]
    for line in lines:
        if (line == '\n'):
            sums.append(0)
        else:
            sums[len(sums) - 1] += int(line)
    sums.sort()
    print(sums[len(sums) - 1] + sums[len(sums) - 2] + sums[len(sums) - 3])