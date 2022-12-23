import re
from collections import defaultdict, deque
from functools import lru_cache


input_file = "example.txt"
# input_file = "input.txt"

valve_adj = defaultdict(list)
flow_rates = {}


with open(input_file) as f:
    for line in f:
        line = line.strip()
        if line != "":
            valve = line[6:8]
            flow_rates[valve] = int(re.search(r"(?<=rate\=)\d+", line).group(0))

            next_idx = line.find("valves")
            if next_idx == -1:
                next_idx = line.find("valve") + 6
            else:
                next_idx += 7
            for v in line[next_idx:].split(","):
                valve_adj[valve].append(v.strip())


@lru_cache
def distance(v1, v2):
    if v1 == v2:
        return 0

    valves = list(valve_adj.keys())
    visited = {}
    for v in valves:
        visited[v] = False

    q = deque([(v1, 0)])
    visited[v1] = True

    while len(q) > 0:
        cur_v, d = q.popleft()
        visited[cur_v] = True
        if cur_v == v2:
            return d
        else:
            for v in valve_adj[cur_v]:
                if not visited[v]:
                    q.append((v, d + 1))


best_flow_rate = -1
cur_flow_rate = 0
valves = list(valve_adj.keys())
visited = {}
for v in valves:
    visited[v] = False

potential_valves = [k for k, v in flow_rates.items() if v > 0]


def move(v, t):
    global best_flow_rate
    global cur_flow_rate
    visited[v] = True
    if best_flow_rate < cur_flow_rate:
        best_flow_rate = cur_flow_rate
    for u in valves:
        if u in potential_valves:
            d = distance(v, u)
            if not visited[u] and d + 1 < t:
                new_t = t - d - 1
                cur_flow_rate += flow_rates[u] * new_t
                move(u, new_t)
                cur_flow_rate -= flow_rates[u] * new_t
    visited[v] = False


move("AA", 30)
print(best_flow_rate)
