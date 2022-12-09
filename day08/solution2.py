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

def view(x, y, direction, distance, height):
    if matrix[x][y] < height:
        x, y = next_pos(x, y, direction)
        if x is not None:
            return view(x, y, direction, distance+1, height)
        else:
            return distance
    else:
        return distance

def score(x,y):
    s = 1
    for d in directions:
        new_x, new_y = next_pos(x, y, d)
        if new_x is not None:
            s *= view(new_x, new_y, d, 1, matrix[x][y])
        else:
            return 0
    return s

max_score = -1
for x in range(N):
    for y in range(M):
        s = score(x,y)
        if s > max_score:
            max_score = s

print(max_score)
    
