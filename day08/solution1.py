# input_file = 'example.txt'
input_file = 'input.txt'

matrix = []
with open(input_file) as f:
    for line in f:
        line = list(line.strip())
        row = list(map(int, line))
        matrix.append(row)
N = len(matrix)
M = len(matrix[0])
visible = [[0] * M for _ in range(N)]

directions = [(+1, 0), (-1,0), (0,+1), (0,-1)]

def next_pos(x, y, direction):
    x += direction[0]
    y += direction[1]
    if 0 <= x and x < N and 0 <= y and y < M:
        return x, y
    else:
        return None, None

def check(x, y, direction, highest):
    if highest < matrix[x][y]:
        highest = matrix[x][y]
        visible[x][y] = 1
    x, y = next_pos(x, y, direction)
    if x is not None:
        return check(x, y, direction, highest)
    else:
        return None

init_heigh = -1
for x in range(N):
    for direction in directions:
        check(x, 0, direction, init_heigh)
        check(x, M-1, direction, init_heigh)
for y in range(M):
    for direction in directions:
        check(0, y, direction, init_heigh)
        check(N-1, y, direction, init_heigh)

cnt = 0
for row in visible:
#    print(''.join([' ' if e == 0 else '1' for e in row]))
    cnt += sum(row)
print(cnt)
