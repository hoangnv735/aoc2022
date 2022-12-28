# input_file = 'example.txt'
input_file = 'input.txt'

matrix = []
instructions = []
with open(input_file) as f:
    mode = 1
    for line in f:
        line = line.rstrip()
        if line  == '':
            mode = 2
            continue
        if mode == 1:
            row = []
            for e in line:
                if e in [' ', '.', '#']:
                    row.append(e)
            matrix.append(row)
        elif mode == 2:
            cur = ''
            line += 'X'
            for c in line:
                if c.isdigit():
                    cur += c
                elif c in ['R', 'L']:
                    instructions.append(int(cur))
                    cur = ''
                    instructions.append(c)
                else:
                    instructions.append(int(cur))

# pad matrix row
max_col = max([len(r) for r in matrix])
for i in range(len(matrix)):
    matrix[i] += [' '] * (max_col - len(matrix[i]))

def print_matrix():
    for row in matrix:
        tmp = []
        for c in row:
            tmp.append(c)
        print(''.join(tmp))


wrap = []
N = len(matrix)
M = len(matrix[0])
for _ in range(N):
    r = []
    for __ in range(M):
        obj = {
            '>': None,
            'v': None,
            '<': None,
            '^': None
        }
        r.append(obj)
    wrap.append(r)

def make_wrap():
    for i, row in enumerate(matrix):
        for j, c in enumerate(row):
            if c == '.':
                # right
                d = '>'
                if j < M-1 and row[j+1] == '.':
                    wrap[i][j][d] = j+1
                elif j == M-1 or (row[j+1] == ' '):
                    for k in range(j):
                        if row[k] == '#':
                            break
                        if row[k] == '.':
                            wrap[i][j][d] = k
                            break
                # down
                d = 'v'
                if i < N-1 and matrix[i+1][j] == '.':
                    wrap[i][j][d] = i+1
                elif i == N-1 or (matrix[i+1][j] == ' '):
                    for k in range(i):
                        if matrix[k][j] == '#':
                            break
                        if matrix[k][j] == '.':
                            wrap[i][j][d] = k
                            break
                # left 
                d = '<'
                if j > 0 and row[j-1] == '.':
                    wrap[i][j][d] = j-1
                elif j == 0 or (row[j-1] == ' '):
                    for k in range(M-1, j, -1):
                        if row[k] == '#':
                            break
                        if row[k] == '.':
                            wrap[i][j][d] = k
                            break
                # up
                d = '^'
                if i > 0 and matrix[i-1][j] == '.':
                    wrap[i][j][d] = i-1
                elif i == 0 or (matrix[i-1][j] == ' '):
                    for k in range(N-1, i, -1):
                        if matrix[k][j] == '#':
                            break
                        if matrix[k][j] == '.':
                            wrap[i][j][d] = k
                            break

x0 = 0
y0 = 0
d0 = '>'
for i, c in enumerate(matrix[0]):
    if c == '.':
       y0 = i
       break

turn_right = {
    '>': 'v',
    'v': '<',
    '<': '^',
    '^': '>',
}
turn_left = {
    '>': '^',
    'v': '>',
    '<': 'v',
    '^': '<'
}

def move(x, y, d):
#    new_x = x
#    new_y = y
#    if d == '>':
#        new_y += 1
#    elif d == 'v':
#        new_x = x + 1
#    elif d == '<':
#        new_y = y - 1
#    elif d == '^':
#        new_x = x - 1
#
#    if 0 <= new_x and 0 <= new_y and new_x < N and new_y < M:
    k = wrap[x][y][d]
    if k is None:
        return None
    if d in ['>', '<']:
        if matrix[x][k] == '.':
            return x, k
        else:
            return None
    else:
        if matrix[k][y] == '.':
            return k, y
        else:
            return None

#print_matrix()
#print(instructions)
make_wrap()
#for i in range(N):
#    for j in range(M):
#        print(wrap[i][j])
x = x0
y = y0
d = d0
history = []
history.append((x, y, d))
# print(x,y,d)
for c in instructions:
    if c == 'R':
        d = turn_right[d]
        history.append((x, y, d))
    elif c == 'L':
        d = turn_left[d]
        history.append((x, y, d))
    else:
        t = c
        while t > 0:
            k = move(x, y, d)
            if k is None:
                break
            x, y = k
            t -= 1
            history.append((x, y, d))
    # print(c, x, y, d, wrap[x][y][d])

convert_d = {
    '>': 0,
    'v': 1,
    '<': 2,
    '^': 3
}
for (x, y, d) in history:
    matrix[x][y] = d
# print_matrix()
print(x+1, y+1, 1000 * (x+1) + 4 * (y+1) + convert_d[d])
