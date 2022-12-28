# input_file = "example.txt"
input_file = "input.txt"

from collections import deque


class Cube:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def adj(self, o):
        if self.y == o.y and self.z == o.z and abs(self.x - o.x) == 1:
            return True
        if self.x == o.x and self.z == o.z and abs(self.y - o.y) == 1:
            return True
        if self.y == o.y and self.x == o.x and abs(self.z - o.z) == 1:
            return True
        return False

    def __repr__(self):
        return f"({self.x}, {self.y}, {self.z})"


cubes = []
with open(input_file) as f:
    for line in f:
        line = line.strip()
        if line != "":
            cubes.append(Cube(*(map(int, line.split(",")))))
            # print(cubes[-1])


def get_min(cubes, d):
    if d == "x":
        return min([c.x for c in cubes])
    if d == "y":
        return min([c.y for c in cubes])
    if d == "z":
        return min([c.z for c in cubes])


def get_max(cubes, d):
    if d == "x":
        return max([c.x for c in cubes])
    if d == "y":
        return max([c.y for c in cubes])
    if d == "z":
        return max([c.z for c in cubes])


def get_shape(cubes):
    min_x = get_min(cubes, "x")
    min_y = get_min(cubes, "y")
    min_z = get_min(cubes, "z")

    max_x = get_max(cubes, "x")
    max_y = get_max(cubes, "y")
    max_z = get_max(cubes, "z")

    size_x = max_x - min_x + 1
    size_y = max_y - min_y + 1
    size_z = max_z - min_z + 1

    offset = (min_x, min_y, min_z)
    size = (size_x, size_y, size_z)
    return offset, size


offset, size = get_shape(cubes)
space = []
for _ in range(size[0]):
    d1 = []
    for __ in range(size[1]):
        d1.append([0] * size[2])
    space.append(d1)


def convert(c, offset):
    return c.x - offset[0], c.y - offset[1], c.z - offset[2]


for c in cubes:
    x, y, z = convert(c, offset)
    space[x][y][z] = 1

cnt = 0
for idx in range(len(cubes)):
    for idx2 in range(idx + 1, len(cubes)):
        if cubes[idx].adj(cubes[idx2]):
            cnt += 1


# def is_extream(x, y, z):
#     return x == 0 or y == 0 or z == 0 or x == size[0] - 1 or y == size[1] - 1 or z == size[2] - 1


def is_valid(x, y, z):
    return x >= 0 and y >= 0 and z >= 0 and x < size[0] and y < size[1] and z < size[2]


dxs = [0, 0, 0, 0, 1, -1]
dys = [0, 0, 1, -1, 0, 0]
dzs = [1, -1, 0, 0, 0, 0]

q = deque()


def search(x, y, z):
    global space
    for dx, dy, dz in zip(dxs, dys, dzs):
        x_, y_, z_ = x + dx, y + dy, z + dz
        if is_valid(x_, y_, z_) and space[x_][y_][z_] == 0:
            q.append((x_, y_, z_))
            space[x_][y_][z_] = 2


def find_extream():
    global space
    global q
    cnt_ext = 0
    x = 0
    for y in range(size[1]):
        for z in range(size[2]):
            if space[x][y][z] == 0:
                space[x][y][x] = 2
                q.append((x, y, z))
                while len(q) > 0:
                    cnt_ext += 1
                    x, y, z = q.popleft()
                    search(x, y, z)
    y = 0
    for x in range(size[0]):
        for z in range(size[2]):
            if space[x][y][z] == 0:
                space[x][y][x] = 2
                q.append((x, y, z))
                while len(q) > 0:
                    cnt_ext += 1
                    x, y, z = q.popleft()
                    search(x, y, z)
    z = 0
    for y in range(size[1]):
        for x in range(size[0]):
            if space[x][y][z] == 0:
                space[x][y][x] = 2
                q.append((x, y, z))
                while len(q) > 0:
                    cnt_ext += 1
                    x, y, z = q.popleft()
                    search(x, y, z)
    return cnt_ext


cnt_ext = find_extream()
bubbles = []
for x in range(size[0]):
    for y in range(size[1]):
        for z in range(size[2]):
            if space[x][y][z] == 0:
                bubbles.append(Cube(x, y, z))

cnt_bubbles = 0
for idx in range(len(bubbles)):
    for idx2 in range(idx + 1, len(bubbles)):
        if bubbles[idx].adj(bubbles[idx2]):
            cnt_bubbles += 1

print(len(cubes) * 12 - 2 * cnt - 6 * (size[0] * size[1] * size[2]) + 6 * cnt_ext + 2 * cnt_bubbles)
