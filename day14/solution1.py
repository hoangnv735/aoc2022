# input_file = "example.txt"
input_file = "input.txt"

rock_lines = []
with open(input_file) as f:
    for line in f:
        line = line.strip()
        if line != "":
            data = [d for d in line.split(" ") if d != "->"]
            rock_lines.append(data)

all_rocks = []
new_rock_lines = []
for data in rock_lines:
    rocks = []
    for d in data:
        x, y = map(int, d.split(","))
        rocks.append((y, x))
    new_rock_lines.append(rocks)
    all_rocks.extend(rocks)
rock_lines = new_rock_lines
del new_rock_lines

# print(rocks)

min_x = min(all_rocks, key=lambda x: x[0])[0]
min_y = min(all_rocks, key=lambda x: x[1])[1]
max_x = max(all_rocks, key=lambda x: x[0])[0]
max_y = max(all_rocks, key=lambda x: x[1])[1]

del all_rocks

sand_pos = (0, 500)
# min_x = min(min_x, sand_pos[1])
max_y = max(max_y, sand_pos[1])
max_x = max(max_x, sand_pos[0])

new_rock_lines = []
for rocks in rock_lines:
    new_rocks = []
    for r in rocks:
        new_rocks.append((r[0], r[1] - min_y))
    new_rock_lines.append(new_rocks)

max_y = max_y - min_y

rock_lines = new_rock_lines
del new_rock_lines
# print(rocks)

sand_pos = (sand_pos[0], sand_pos[1] - min_y)

# print(sand_pos)

N = max_x + 1
M = max_y + 1
# print(N, M)


matrix = [[0] * M for _ in range(N)]
for rocks in rock_lines:
    for idx in range(len(rocks) - 1):
        cur_pos = rocks[idx]
        next_pos = rocks[idx + 1]
        if cur_pos[0] == next_pos[0]:
            r = cur_pos[0]
            c1, c2 = cur_pos[1], next_pos[1]
            if c1 > c2:
                tmp = c1
                c1 = c2
                c2 = tmp
                del tmp
            for i in range(c1, c2 + 1):
                matrix[r][i] = 1
        else:
            c = cur_pos[1]
            r1 = cur_pos[0]
            r2 = next_pos[0]
            if r1 > r2:
                tmp = r1
                r1 = r2
                r2 = tmp
                del tmp
            for i in range(r1, r2 + 1):
                matrix[i][c] = 1


def valid(x, y):
    # print(x, y)
    return 0 <= x and x < N and 0 <= y and y < M


import os


def print_map():
    os.system("clear")
    output = "\n".join(["".join(["." if c == 0 else "#" for c in r]) for r in matrix])
    print(output)


cnt = 0
while True:
    # print_map()
    # input()
    x, y = sand_pos
    is_valid = True
    while True:
        if not valid(x, y):
            is_valid = False
            break
        if valid(x + 1, y):
            if matrix[x + 1][y] == 0:
                x += 1
                continue
            else:
                if valid(x + 1, y - 1):
                    if matrix[x + 1][y - 1] == 0:
                        x += 1
                        y -= 1
                        continue
                    if valid(x + 1, y + 1):
                        if matrix[x + 1][y + 1] == 0:
                            x += 1
                            y += 1
                            continue
                        else:
                            matrix[x][y] = 1
                            cnt += 1
                            break
                    else:
                        is_valid = False
                        break
                else:
                    is_valid = False
                    break
        else:
            is_valid = False
            break

    if not is_valid:
        break

print(cnt)
