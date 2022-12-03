input_file = 'input.txt'
# input_file = 'example.txt'

idx = 1
total = 0
max_calo = -1
max_idx = -1

with open(input_file) as f:
    for line in f:
        # print(line.strip())
        if line.strip() == "":
            if total > max_calo:
                max_calo = total
                max_idx = idx
            idx += 1
            total = 0
        else:
            total += int(line.strip())

if total > max_calo:
    max_calo = total
    max_idx = idx

print(max_calo, max_idx)