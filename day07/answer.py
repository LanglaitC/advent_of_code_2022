import os
dir_path = os.path.dirname(os.path.realpath(__file__))

COMMAND_CHAR = "$"
DIR_ENUM = "dir"
FILE_ENUM = "file"

# Part 1

def getScore(tree, score):
    size = 0
    for file in tree["content"]:
        if (file["type"] == FILE_ENUM):
            size += file["size"]
        else:
            tmpSize, score = getScore(file, score)
            size += tmpSize
    if (size < 100000):
        score += size
    return (size, score)

def getAllDirectoriesSize(tree):
    size = 0
    directories = []
    for file in tree["content"]:
        if (file["type"] == FILE_ENUM):
            size += file["size"]
        else:
            tmpSize, tmpDirectories = getAllDirectoriesSize(file)
            size += tmpSize
            directories += tmpDirectories
            directories += [tmpSize]
    return size, directories + [size]
        

with open(f'{dir_path}/input.txt') as file:
    input = file.readlines()
    tree = { "name": "/", "content":[] }
    currentDirectory = tree
    for idx, line in enumerate(input):
        splittedCommand = line.rstrip().split(' ')
        if line[0] == COMMAND_CHAR:
            if (splittedCommand[1] == "cd"):
                if splittedCommand[2] == "..":
                    currentDirectory = currentDirectory["parent"]
                elif splittedCommand[2] == "/":
                    currentDirectory = tree
                else:
                    currentDirectory = [file for file in currentDirectory["content"] if file["name"] == splittedCommand[2]][0]
        elif (splittedCommand[0] == "dir"):
            currentDirectory["content"].append({"name": splittedCommand[1], "type": DIR_ENUM, "content":[], "parent": currentDirectory})
        else:
            currentDirectory["content"].append({"name": splittedCommand[1], "type": FILE_ENUM, "size": int(splittedCommand[0])})
    values = []
    _, score = getScore(tree, 0)
    print(f'Part 1 {score}')

# Part 2

    totalSize, directoriesSize = getAllDirectoriesSize(tree)
    directoriesSize.sort()
    availableSize = 70000000 - totalSize
    minSizeToDelete = 30000000 - availableSize
    for size in directoriesSize:
        if (size > minSizeToDelete):
            print(f'Part 2 {size}')
            break
        


        


        
