# input_file = 'example.txt' 
input_file = 'input.txt' 

from collections import namedtuple

Pos = namedtuple('Pos', ['x', 'y'])
tail_maps = set()
start_pos = Pos(0,0)
tail_pos = Pos(0,0)
head_pos = Pos(0,0)
tail_maps.add(tail_pos)

direction_mapper = {
    'R': Pos(0,1),
    'L': Pos(0,-1),
    'U': Pos(-1, 0),
    'D': Pos(1, 0)
}

def next_post(pos):
    return Pos(pos.x + d.x, pos.y + d.y)

def dist(pos1, pos2):
    return (pos1.x - pos2.x)**2 + (pos1.y - pos2.y)**2

def _move(direction):
    global head_pos
    global tail_pos
        
    d = direction_mapper[direction]
    new_head_pos = Pos(head_pos.x + d.x, head_pos.y + d.y)
    distance = dist(tail_pos, new_head_pos)
    if distance in [0,1,2]:
        head_pos = new_head_pos
    elif distance in [4,5]:
        tail_pos = head_pos
        tail_maps.add(tail_pos)
        head_pos = new_head_pos
    else:
        raise ValueError()

def move(direction, step):
    for _ in range(step):
        _move(direction)

with open(input_file) as f:
    for line in f:
        line = line.strip()
        if line != '':
            direction, step = tuple(line.split())
            move(direction, int(step))

print(len(tail_maps))
