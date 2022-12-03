input_file = 'input.txt'
# input_file = 'example.txt'

turns = []
with open(input_file) as f:
    for line in f:
        turns.append(line.strip().split(' '))

# A: Rock, B: Paper, C: Scissor
# X: Rock, Y: Paper, Z: Scissor
#   A  B  C
# X 3  0  6
# Y 6  3  0 
# Z 0  6  3

vs_score = [
    [3, 0, 6],
    [6, 3, 0],
    [0, 6, 3]
]
# X, Y, Z = [1, 2, 3]
coefs = [1, 2, 3]
shape_map = {
    "A": 0,
    "B": 1,
    "C": 2,
    "X": 0,
    "Y": 1,
    "Z": 2,
}

total_score = 0
for turn in turns:
    opponent = shape_map[turn[0]]
    me = shape_map[turn[1]]
    # print(turn)
    # print(vs_score[me][opponent], coefs[me])
    total_score += vs_score[me][opponent] + coefs[me]

print(total_score)
