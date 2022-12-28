import os
from collections import defaultdict
from copy import deepcopy

# input_file = "example.txt"
input_file = "input.txt"

with open(input_file) as f:
    effect_string = f.read().strip()


sidx = 0
sl = len(effect_string)


def get_effect():
    global sidx
    effect = effect_string[sidx]
    ei = sidx
    sidx = (sidx + 1) % sl
    return -1 if effect == "<" else 1, ei


rocks = [
    {
        # shape: bar
        "blocks": [(0, 0), (0, 1), (0, 2), (0, 3)],
        "height": 1,
        "width": 4,
    },
    {
        # shape: cross
        "blocks": [(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)],
        "height": 3,
        "width": 3,
    },
    {
        # shape: L
        "blocks": [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)],
        "height": 3,
        "width": 3,
    },
    {
        # shape: column
        "blocks": [(0, 0), (1, 0), (2, 0), (3, 0)],
        "height": 4,
        "width": 1,
    },
    {
        # shape: square
        "blocks": [(0, 0), (0, 1), (1, 0), (1, 1)],
        "height": 2,
        "width": 2,
    },
]
ridx = 0
rl = len(rocks)


def get_rock():
    global ridx
    rock = rocks[ridx]
    ri = ridx
    ridx = (ridx + 1) % rl
    return rock, ri


max_height = 0
pg = []
hidden = 0
pile = []
rock_and_effect_to_row = defaultdict(list)


def get_pos():
    global max_height
    y = 2
    x = max_height + 3
    return x, y


def valid(rock, pos):
    # right wall
    if pos[1] + rock["width"] > 7:
        return False
    # left wall
    if pos[1] < 0:
        return False
    # bottom
    if pos[0] < 0:
        return False
    for block in rock["blocks"]:
        x = pos[0] + block[0]
        y = pos[1] + block[1]
        # print(x, y, len(pg))
        if pg[x][y] == 1:
            return False
    return True


def buffer(height):
    global pg
    l = len(pg)
    if l <= height:
        for _ in range(height - l + 1):
            pg.append([0] * 7)


def print_pg(rock=None, pos=None):
    # os.system("clear")
    new_pg = deepcopy(pg)
    if rock is not None:
        for block in rock["blocks"]:
            x = pos[0] + block[0]
            y = pos[1] + block[1]
            new_pg[x][y] = 2

    for idx in reversed(range(len(pg))):
        visual_row = []
        for p in new_pg[idx]:
            if p == 0:
                visual_row.append(".")
            elif p == 1:
                visual_row.append("#")
            else:
                visual_row.append("@")
        print("".join(visual_row))


def to_int(row):
    p = 6
    v = 0
    while p >= 0:
        v += row[6 - p] << p
        p -= 1
    return v


def add_row(pos):
    global pile
    global pg
    x = pos[0]
    if x < len(pile):
        pile = pile[: x - 1]
        for idx in range(x, len(pg)):
            pile.append(to_int(pg[idx]))
    else:
        for idx in range(len(pile), len(pg)):
            # print(pg[idx])
            pile.append(to_int(pg[idx]))


def check(l1, l2):
    for e1, e2 in zip(l1, l2):
        if e1 != e2:
            return False
    return True


def find_pattern(ri, ei, x, turn):
    cur_pattern = (ri, ei)
    for row, t in rock_and_effect_to_row[cur_pattern]:
        c = x - row
        if row < x and row > c - 1:
            if check(pile[row - c : row], pile[row:x]):
                return c, turn - t
    return None, None


def compute(m):
    global pg
    global max_height
    global hidden
    turn = 1
    found = False
    while turn <= m:
        ri = ridx
        rock, _ = get_rock()
        pos = get_pos()
        buffer(pos[0] + rock["height"])
        effect = None
        ei = sidx
        while True:
            # effect
            effect, _ = get_effect()
            new_pos = (pos[0], pos[1] + effect)
            if valid(rock, new_pos):
                pos = new_pos
            # fall
            new_pos = (pos[0] - 1, pos[1])
            if valid(rock, new_pos):
                pos = new_pos
            else:
                for block in rock["blocks"]:
                    x = pos[0] + block[0]
                    y = pos[1] + block[1]
                    pg[x][y] = 1
                max_height = max(max_height, pos[0] + rock["height"])
                break
        if not found:
            add_row(pos)
            height, cycle = find_pattern(ri, ei, pos[0], turn)
            if height is not None:
                # print(cycle, height, turn)
                found = True
                hidden = height * ((m - turn) // cycle)
                m = ((m - turn) % cycle) + turn
            else:
                rock_and_effect_to_row[(ri, ei)].append((pos[0], turn))

        turn += 1
    return max_height


M = 1000000000000
# M = 2022
c = compute(M)
print(hidden + c, hidden, c)
