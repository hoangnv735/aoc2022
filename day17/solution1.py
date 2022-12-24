import os
from copy import deepcopy 
input_file = 'example.txt'
# input_file = 'input.txt'

with open(input_file) as f:
    effect_string = f.read().strip()


sidx = 0
sl = len(effect_string)
def get_effect():
    global sidx
    effect = effect_string[sidx]
    sidx = (sidx + 1) % sl
    return -1 if effect == '<' else 1

rocks = [
    {
        # shape: bar
        'blocks': [(0,0), (0,1), (0,2), (0,3)],
        'height': 1,
        'width': 4,
    },
    {
        # shape: cross
        'blocks': [(0,1), (1,0), (1,1), (1,2), (2,1)],
        'height': 3,
        'width': 3,
    },
    {
        # shape: L
        'blocks': [(0,0), (0,1), (0,2), (1,2), (2,2)],
        'height': 3,
        'width': 3,
    },
    {
        # shape: column
        'blocks': [(0,0), (1,0), (2,0), (3,0)],
        'height': 4,
        'width': 1,
    },
    {
        # shape: square
        'blocks': [(0,0), (0,1), (1,0), (1,1)],
        'height': 2,
        'width': 2,
    },
]
ridx = 0
rl = len(rocks)
def get_rock():
    global ridx
    rock = rocks[ridx]
    ridx = (ridx + 1) % rl
    return rock


max_height = 0
pg = []
for _ in range(3):
    row = [0] * 7
    pg.append(row)


def get_pos():
    y = 2
    x = max_height + 3
    return x, y


def valid(rock, pos):
    # right wall
    if pos[1] + rock['width'] > 7:
        return False
    # left wall
    if pos[1] < 0: 
        return False
    # bottom
    if pos[0] < 0:
        return False
    for block in rock['blocks']:
        x = pos[0] + block[0]
        y = pos[1] + block[1]
        print(x, y)
        if pg[x][y] == 1:
            return False
    return True


def buffer(height):
    global pg
    l = len(pg)
    if l <= height:
        for _ in range(height - l + 1):
            pg.append([0] * 7)


def print_pg(rock, pos):
    os.system('clear')
    new_pg = deepcopy(pg) 
    for block in rock['blocks']:
        x = pos[0] + block[0]
        y = pos[1] + block[1]
        new_pg[x][y] = 2

    for idx in reversed(range(len(pg))):
        visual_row = []
        for p in new_pg[idx]:
            if p == 0:
                visual_row.append('.')
            elif p == 1:
                visual_row.append('#')
            else:
                visual_row.append('@')
        print(''.join(visual_row))


def compute(m):
    global pg
    global max_height
    turn = 0
    while turn < m:
        rock = get_rock()
        effect = get_effect()
        pos = get_pos()
        print('rock', rock)
        print('effect', effect)
        print('pos', pos)
        input()
        buffer(pos[1] + rock['height'])
        while True:
            # effect
            new_pos = (pos[0], pos[1] + effect)
            if valid(rock, new_pos):
                pos = new_pos
            # fall
            new_pos = (pos[0] - 1, pos[1])
            if valid(rock, new_pos):
                pos = new_pos
            else:
                for block in rock['blocks']:
                    x = pos[0] + block[0]
                    y = pos[1] + block[1]
                    pg[x][y] = 1
                max_height = max(max_height, pos[1] + rock['height'])
                print_pg(rock, pos)
                input()
                break
            print_pg(rock, pos)
            input()


print(compute(1))
