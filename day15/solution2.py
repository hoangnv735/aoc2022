from tqdm import tqdm

# input_file = "example.txt"
input_file = "input.txt"

import re

sensors = []
beacons = []
dists = []


def dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


with open(input_file) as f:
    for line in f:
        line = line.strip()
        if line != "":
            data = []
            for m in re.finditer(r"-?\d+", line):
                tmp = int(line[m.start() : m.end()])
                data.append(tmp)
            sensors.append((data[1], data[0]))
            beacons.append((data[3], data[2]))
            dists.append(dist(sensors[-1], beacons[-1]))


M = 4000000
if input_file == "example.txt":
    M = 20


def compute(line):
    found = False
    check = [0] * len(sensors)
    y = 0
    while y < M:
        is_covered = False
        for idx, s in enumerate(sensors):
            if check[idx] == 0:
                r = dists[idx] - abs(s[0] - line)
                if r >= 0:
                    c = s[1]
                    if c - r <= y and y <= c + r:
                        # print(line, y, s, d)
                        y = c + r + 1
                        check[idx] = 1
                        is_covered = True
                        break
        if not is_covered:
            print(y, line)
            print(line + y * 4000000)
            found = True
            break
    return found


for line in tqdm(range(M + 1)):
    if compute(line):
        break
