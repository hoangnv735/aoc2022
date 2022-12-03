input_file = 'input.txt'
# input_file = "example.txt"


def compute(part1, part2):
    common = set(part1) & set(part2)
    # print(common)
    return sum([ord(e) - ord("a") + 1 if ord(e) >= ord("a") else ord(e) - ord("A") + 27 for e in list(common)])


total = 0
with open(input_file) as f:
    for line in f:
        data = line.strip()
        part1 = data[: len(data) // 2]
        part2 = data[len(data) // 2 :]
        tmp = compute(part1, part2)
        # print(tmp)
        total += tmp

print(total)
