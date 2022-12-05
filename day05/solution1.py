import re
import stack_data

# input_file = "example.txt"
input_file = "input.txt"

crate_strings = []
orders = []
with open(input_file) as f:
    mode = 1
    for line in f:
        tmp = line.strip()
        if tmp == "":
            mode = 2
            continue
        if mode == 1:
            crate_strings.append(line)
            
        else:
            orders.append(line)

n_crate = len(crate_strings[-1].split())
crate_stacks = [[] for _ in range(n_crate)]
for idx in range(len(crate_strings) - 2, -1, -1):
    s = crate_strings[idx]
    for cidx, c in enumerate(s):
        if c not in [" ", "[", "]", "\n"]:
            crate_stacks[cidx // 4].append(c)
# print(crate_stacks)

for order in orders:
    # print(orders)
    amount, start, end = tuple([int(d) for d in re.findall(r"\d+", order)])
    while amount > 0:
        crate_stacks[end - 1].append(crate_stacks[start - 1].pop())
        amount -= 1

out = "".join([c.pop() for c in crate_stacks])
print(out)
