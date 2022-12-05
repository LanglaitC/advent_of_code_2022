SCORE = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

WINNING_ENCOUNTERS = {
    'C': 'X',
    'A': 'Y',
    'B': 'Z'
}

DRAWING_ENCOUNTER = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z'
}

LOSING_ENCOUNTER = {
    'B': 'X',
    'C': 'Y',
    'A': 'Z',
}

LOOSE_SIGNAL = 'X'
DRAW_SIGNAL = 'Y'
WIN_SIGNAL = 'Z'



with open(f'{dir_path}/input.txt') as file:
    instructions = file.readlines()
    score = 0
    for instruction in instructions:
        opponent_move = instruction[0]
        your_move = instruction[2]
        if your_move == WINNING_ENCOUNTERS[opponent_move]:
            score += 6
        elif your_move == DRAWING_ENCOUNTER[opponent_move]:
            score += 3
        score += SCORE[your_move]
    print('Part 1 ' + str(score))

    score = 0
    for instruction in instructions:
        opponent_move = instruction[0]
        expected_outcome = instruction[2]
        if (expected_outcome == LOOSE_SIGNAL):
            score += SCORE[LOSING_ENCOUNTER[opponent_move]]
        elif (expected_outcome == DRAW_SIGNAL):
            score += SCORE[DRAWING_ENCOUNTER[opponent_move]] + 3
        elif (expected_outcome == WIN_SIGNAL):
            score += SCORE[WINNING_ENCOUNTERS[opponent_move]] + 6
    print('Part 2 ' + str(score))


