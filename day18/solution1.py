# input_file = "example.txt"
input_file = 'input.txt'


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


cubes = []
with open(input_file) as f:
    for line in f:
        line = line.strip()
        if line != "":
            cubes.append(Cube(*(map(int, line.split(",")))))

cnt = 0
for idx in range(len(cubes)):
    for idx2 in range(idx + 1, len(cubes)):
        if cubes[idx].adj(cubes[idx2]):
            cnt += 1

print(len(cubes) * 6 - 2 * cnt)
