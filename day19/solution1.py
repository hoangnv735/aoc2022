# input_file = "example.txt"
input_file = "input.txt"

import re
import timeit
from collections import deque

blue_prints = []

with open(input_file) as f:
    for line in f:
        line = line.strip()
        if line != "":
            data = line[14:].split(".")
            ore_robot_cost = int(re.search(r"\d+", data[0]).group(0))
            clay_robot_cost = int(re.search(r"\d+", data[1]).group(0))
            obs_robot_cost = (
                int(re.search(r"\d+ (?=ore)", data[2]).group(0)),
                int(re.search(r"\d+ (?=clay)", data[2]).group(0)),
            )
            geo_robot_cost = (
                int(re.search(r"\d+ (?=ore)", data[3]).group(0)),
                int(re.search(r"\d+ (?=obsidian)", data[3]).group(0)),
            )
            # print(ore_robot_cost, clay_robot_cost, obs_robot_cost, geo_robot_cost)
            blue_prints.append((ore_robot_cost, clay_robot_cost, obs_robot_cost, geo_robot_cost))


def compute(blue_print):
    co, cc, (co1, co2), (cg1, cg2) = blue_print
    t = 24
    max_o = max(co, cc, co1, cg1)

    state = (0, 0, 0, 0, 1, 0, 0, 0, t)
    q = deque([state])
    seen = set()
    best = 0
    while len(q) > 0:
        state = q.popleft()
        if state in seen:
            continue
        seen.add(state)
        # print(state)
        a1, a2, a3, a4, r1, r2, r3, r4, t = state
        if best < a4:
            best = a4
            # if t == 0:
            # print('update best', best, 'state', state)
        if t == 0:
            continue
        if a1 >= t * max_o - (t - 1) * r1:
            a1 = t * max_o - (t - 1) * r1
        if a2 >= t * co2 - (t - 1) * r2:
            a2 = t * co2 - (t - 1) * r2
        if a3 >= t * cg2 - (t - 1) * r3:
            a3 = t * cg2 - (t - 1) * r3
        # make nothing
        q.append((a1 + r1, a2 + r2, a3 + r3, a4 + r4, r1, r2, r3, r4, t - 1))
        # make ore robot
        if a1 >= co and r1 < max_o and t > 2:
            q.append((a1 - co + r1, a2 + r2, a3 + r3, a4 + r4, r1 + 1, r2, r3, r4, t - 1))
        # make clay robot
        if a1 >= cc and r2 < co2 and t > 2:
            q.append((a1 - cc + r1, a2 + r2, a3 + r3, a4 + r4, r1, r2 + 1, r3, r4, t - 1))
        # make obsidian robot
        if a1 >= co1 and a2 >= co2 and r3 < cg2 and t > 2:
            q.append((a1 - co1 + r1, a2 - co2 + r2, a3 + r3, a4 + r4, r1, r2, r3 + 1, r4, t - 1))
        # make geoge robot
        if a1 >= cg1 and a3 >= cg2 and t > 1:
            q.append((a1 - cg1 + r1, a2 + r2, a3 - cg2 + r3, a4 + r4, r1, r2, r3, r4 + 1, t - 1))

    return best


start = timeit.default_timer()
total = 0
for idx, blue_print in enumerate(blue_prints):
    c = compute(blue_print)
    # print(idx+1, c)
    total += (idx + 1) * c
print("run time:", timeit.default_timer() - start)
print(total)
