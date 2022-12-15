# input_file = 'example.txt'
input_file = 'input.txt'

import re

sensors = []
beacons = []

with open(input_file) as f:
    for line in f:
        line = line.strip()
        if line != "":
            data = []
            for m in re.finditer(r'\d+', line):
                tmp = int(line[m.start():m.end()])
                data.append(tmp)
            sensors.append((data[1], data[0]))
            beacons.append((data[3], data[2]))

L = 2000000
if input_file == 'example.txt':
    L = 10

def dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

max_dist = dist(sensors[0], beacons[0])
for idx in range(1, len(sensors)):
    max_dist = max(max_dist, dist(sensors[idx], beacons[idx]))

min_y = int(1e9)
max_y = int(-1e9)

for idx in range(len(sensors)):
    min_y = min(min_y, sensors[idx][1])
    max_y = max(max_y, sensors[idx][1])

min_y -= max_dist
max_y += max_dist

def compute(line):
    offset = min_y
    N = max_y - min_y + 1
    invalid = [0] * N

    def map_col(col):
        return col - offset

    for s, b in zip(sensors, beacons):
        d = dist(s, b)
        r = d - abs(s[0] - line)
        if r >= 0:
            c = map_col(s[1])
            for y in range(c-r, c+r+1):
                if 0 <= y and y < N:
                    invalid[y] = 1
                else:
                    raise ValueError()

    for b in beacons + sensors:
        if b[0] == line:
            c = map_col(b[1])
            if 0 <= c and c < N:
                invalid[c] = 0
    return sum(invalid)

print(compute(L))
