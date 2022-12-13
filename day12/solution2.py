# input_file = 'example.txt'
input_file = 'input.txt'

x = 0
start_poses = []
end_pos = None
matrix = []
with open(input_file) as f:
    for line in f:
        line = line.strip()
        if line != '':
            height_map = []
            for idx, char in enumerate(line):
                if char == 'S':
                    start_poses.append((x, idx))
                    height_map.append(int(ord('a') - ord('a')))
                elif char == 'E':
                    end_pos = (x, idx)
                    height_map.append(int(ord('z') - ord('a')))
                else:
                    if char == 'a':
                        start_poses.append((x,idx))
                    height_map.append(int(ord(char) - ord('a')))
            x += 1

            matrix.append(height_map)
del x
N = len(matrix)
M = len(matrix[0])

# for i in range(N):
#     for j in range(M):
#         print(f'{matrix[i][j]:3d}', end=' ')
#     print()
# print()

dist = [ [-1] * M for _ in range(N)]
dist[end_pos[0]][end_pos[1]] = 0

def valid(x, y):
    return 0 <= x and x < N and 0 <= y and y < M

def compute_step(x, y):
    d_x = [0, 0, -1, +1]
    d_y = [-1, +1, 0, 0]
    for i in range(4):
        new_x = x + d_x[i]
        new_y = y + d_y[i]
        if valid(new_x, new_y) and dist[new_x][new_y] == -1 and matrix[new_x][new_y]-matrix[x][y] >= -1:
            dist[new_x][new_y] = dist[x][y] + 1
            cells.append((new_x, new_y))

cells = [end_pos]
idx = 0

while idx < len(cells):
    x = cells[idx][0]
    y = cells[idx][1]
    compute_step(x, y)
    idx += 1

# for i in range(N):
#     for j in range(M):
#        print(f'{dist[i][j]:3d}', end=' ')
#     print()

min_step = dist[start_poses[0][0]][start_poses[0][1]]
for p in start_poses[1:]:
    if dist[p[0]][p[1]] >= 0 and dist[p[0]][p[1]] < min_step:
            min_step = dist[p[0]][p[1]]

print(min_step)
