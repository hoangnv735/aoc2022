import re
from copy import deepcopy


# input_file = "example.txt"
input_file = 'input.txt'

valve_map = {}
idx = 0
with open(input_file) as f:
    for line in f:
        line = line.strip()
        if line != '':
            name = line[6:8]
            valve_map[name] = idx
            idx += 1
idx_map = {v:k for k,v in valve_map.items()}

adj = []
flow = []

with open(input_file) as f:
    for line in f:
        line = line.strip()
        if line != "":
            idx = valve_map[line[6:8]]
            f = re.search(r'(?<=rate\=)\d+', line).group(0)
            flow.append(int(f))
            next_idx = line.find('valves')
            if next_idx == -1:
                next_idx = line.find('valve') + 6
            else:
                next_idx += 7
            adj_v = []
            for v in line[next_idx:].split(','):
                adj_v.append(valve_map[v.strip()])
            adj.append(adj_v)

cur_flow = 0
best_flow = -1
is_open = [0] * len(valve_map.keys())
process = [None] * 32
best_process = None

def max_potential(t):
    mf = [flow[idx] for idx, io in enumerate(is_open) if io == 0]
    mf.sort(reverse=True)
    m = 0
    for idx, f in enumerate(mf):
        m += f * (t - idx - 1)
    return m

def move(idx, t, pidx):
    global cur_flow
    global best_flow
    global process
    global best_process
    process[pidx] = idx 
    if flow[idx] > 0 and is_open[idx] == 0:
        t -= 1
        is_open[idx] = 1
        cur_flow += t * flow[idx]
        process[pidx+1] = f'o {idx}'
        if t > 1 and cur_flow + max_potential(t-1) > best_flow:
            for nidx in adj[idx]:
                move(nidx, t-1, pidx+2)
        else:
            if best_flow < cur_flow:
                best_flow = cur_flow
                best_process = deepcopy(process)
        cur_flow -= t * flow[idx]
        is_open[idx] = 0
        t += 1
    if t > 1 and cur_flow + max_potential(t-1) > best_flow:
        for nidx in adj[idx]:
            move(nidx, t-1, pidx+1)
    else:
        if best_flow < cur_flow:
            best_flow = cur_flow
            best_process = deepcopy(process)


def print_process(p):
    s = 0
    c = 0
    for i in range(1, len(p)):
        print(f'-----Minute {i}')
        s += c
        print(f'Produce {c}, total is {s}')
        if p[i] is None:
            break
        if isinstance(p[i], str):
            idx = int(p[i][2:])
            c += flow[idx]
            print(f'Open {idx_map[idx]}')
        else:
            idx = p[i]
            print(f'Move to {idx_map[idx]}')

move(0, 30, 0)
print(best_flow)
# print_process(best_process)
