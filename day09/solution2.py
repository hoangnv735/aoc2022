import os
input_file = 'example2.txt' 
# input_file = 'input.txt' 

from collections import namedtuple

Pos = namedtuple('Pos', ['x', 'y'])
tail_map = set()
rope = []
N = 10
for _ in range(N):
    rope.append(Pos(0,0))
tail = N-1
tail_map.add(rope[tail])

direction_mapper = {
    'R': Pos(0,1),
    'L': Pos(0,-1),
    'U': Pos(-1, 0),
    'D': Pos(1, 0)
}

def sign(x):
    if x < 0:
        return -1
    else:
        return 1

def next_pos(pos, d):
    return Pos(pos.x + d.x, pos.y + d.y)

def dist(pos1, pos2):
    return (pos1.x - pos2.x)**2 + (pos1.y - pos2.y)**2

def move_body(idx):
    distance = dist(rope[idx], rope[idx-1])
    if distance in [0,1,2]:
        return rope[idx]
    else: #  distance in [4,5]:
        x_adj = 0
        y_adj = 0
        if distance in [4,8]:
            new_x = (rope[idx].x + rope[idx-1].x + x_adj)
            new_y = (rope[idx].y + rope[idx-1].y + y_adj)

            new_x = sign(new_x) * (abs(new_x) // 2)
            new_y = sign(new_y) * (abs(new_y) // 2)
            return Pos(new_x, new_y) 
        elif distance == 5:
            x_adj = 1 if rope[idx-1].x > rope[idx].x else -1
            y_adj = 1 if rope[idx-1].y > rope[idx].y else -1
            return Pos(rope[idx].x + x_adj, rope[idx].y + y_adj)
        else:
            print(rope)
            raise ValueError(idx, distance, rope[idx], rope[idx-1])

def _move(direction):
    # move head
    d = direction_mapper[direction]
    rope[0] = next_pos(rope[0], d)
    # print(rope)
    # move body
    for i in range(1, N):
        new_pos = move_body(i)
        if new_pos.x == rope[i].x and new_pos.y == rope[i].y:
            break
        rope[i] = new_pos
        # print(rope)

    tail_map.add(rope[tail])
    # print(rope[tail].x, rope[tail].y)
    
def move(direction, step):
    for _ in range(step):
        _move(direction)
        # print(rope)


def print_tail_map():
    min_x = min([p.x for p in tail_map])
    min_y = min([p.y for p in tail_map])
    
    max_x = max([p.x for p in tail_map])
    max_y = max([p.y for p in tail_map])

    padding = 2
    x_offset = abs(min_x) + padding
    y_offset = abs(min_y) + padding

    x_length = (max_x - min_x + 1) + padding * 2
    y_length = (max_y - min_y + 1) + padding * 2

    matrix = [ ['.'] * y_length for _ in range(x_length)]
    for p in tail_map:
        matrix[p.x + x_offset][p.y + y_offset] = '#'

    output = '\n'.join([''.join(line) for line in matrix])
    print(output)

def print_map():
    x_offset = 18
    y_offset = 14

    x_length = 25
    y_length = 30

    matrix = [ ['.'] * y_length for _ in range(x_length)]
    for idx, p in enumerate(rope):
        if idx == 0:
            mark = 'H'
        else:
            mark = str(idx)
        matrix[p.x + x_offset][p.y + y_offset] = mark 

    output = '\n'.join([''.join(line) for line in matrix])
    os.system('clear')
    print('\n')
    print(output)

do_print = False
if do_print:
    print_map()
with open(input_file) as f:
    for line in f:
        line = line.strip()
        if line != '':
            direction, step = tuple(line.split())
            if do_print:
                input()
            move(direction, int(step))
            if do_print:
                print_map()
# print_tail_map()
print(len(tail_map))
