input_file = 'input.txt'
# input_file = 'example.txt'

idx = 1
total = 0
max_calo = -1
max_idx = -1

elves = []

with open(input_file) as f:
    for line in f:
        # print(line.strip())
        if line.strip() == "":
            if total > max_calo:
                max_calo = total
                max_idx = idx
            elves.append((idx, total))
            idx += 1
            total = 0
        else:
            total += int(line.strip())

if total > max_calo:
    max_calo = total
    max_idx = idx
if total > 0:
    elves.append((idx, total))

elves.sort(key=lambda x: x[1], reverse=True)
print(elves[:3])
print(sum([e[1] for e in elves[:3]]))