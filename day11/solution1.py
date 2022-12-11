# input_file = "example.txt"
input_file = "input.txt"


def create_func(s):
    data = s.split(' ')
    if data[1] == '+':
        if data[2] == 'old':
            return lambda x: (x + x) // 3
        else:
            return lambda x: (x + int(data[2])) // 3
    elif data[1] == '*':
        if data[2] == 'old':
            return lambda x: (x * x) // 3
        else:
            return lambda x: (x * int(data[2])) // 3

class Monkey():
    def __init__(self, idx, items, s, d, id1, id2):
        self.idx = idx
        self.items = items
        self.get_worry_level = create_func(s)
        self.next = lambda w: id1 if w % d == 0 else id2
        self.cnt = 0
    
    def __len__(self):
        return len(self.items)

    def pop(self):
        if len(self.items) > 0:
            v = self.items[0]
            self.items = list(self.items[1:])
            return v
        else:
            return None

    def add(self, v):
        self.items.append(v)

    def inspect(self):
        v = self.pop()
        if v is None:
            return None, None
        else:
            worry_level = self.get_worry_level(v)
            next_idx = self.next(worry_level)
            self.cnt += 1
            return worry_level, next_idx        


monkeys = []
with open(input_file) as f:
    for line in f:
        line = line.strip()
        if line.startswith('Monkey'):
            idx = line.split(' ')[1]
            idx = int(idx[:-1])
            line = f.readline().strip().split(':')[1]
            items = [int(e.strip()) for e in line.split(',')]
            s = f.readline().strip().split('=')[1].strip()
            d = int(f.readline().strip().split(' ')[-1])
            id1 = int(f.readline().strip().split(' ')[-1])
            id2 = int(f.readline().strip().split(' ')[-1])
            monkeys.append(Monkey(idx, items, s, d, id1, id2))

        
r = 1
while r <= 20:
    for m in monkeys:
        while len(m) > 0:
            wl, idx = m.inspect()
            monkeys[idx].add(wl)
    r += 1

cnts = [m.cnt for m in monkeys]
cnts.sort()
# print(cnts)
print(cnts[-1] * cnts[-2])
