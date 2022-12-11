# input_file = "example.txt"
input_file = "input.txt"

def gcd(a, b):
    if b > a:
        a = a + b
        b = a - b
        a = a - b
    r = a % b
    if r == 0:
        return b
    else:
        return gcd(b,r)

def lcm(a, b):
    return a * b // gcd(a, b)

def create_func(s, m):
    data = s.split(' ')
    if data[1] == '+':
        if data[2] == 'old':
            return lambda x: (x + x) % m
        else:
            return lambda x: (x + int(data[2])) % m
    elif data[1] == '*':
        if data[2] == 'old':
            return lambda x: (x * x) % m
        else:
            return lambda x: (x * int(data[2])) % m

class Monkey():
    def __init__(self, idx, items, s, d, id1, id2):
        self.idx = idx
        self.items = items
        self.d = d
        self.s = s
        self.id1 = id1
        self.id2 = id2
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

    def update_func(self, m):
        self.get_worry_level = create_func(self.s, m)
        self.next = lambda w: self.id1 if w % self.d == 0 else self.id2


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

M = monkeys[0].d
for m in monkeys[1:]:
    M = lcm(M, m.d)

for m in monkeys:
    m.update_func(M)

r = 1
while r <= 10000:
    for idx, m in enumerate(monkeys):
        while len(m) > 0:
            wl, idx = m.inspect()
            monkeys[idx].add(wl)
    r += 1

cnts = [m.cnt for m in monkeys]
cnts.sort()
# print(cnts)
print(cnts[-1] * cnts[-2])
