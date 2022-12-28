from collections import deque

# input_file = 'example.txt'
input_file = "input.txt"


class Monkey:
    def __init__(self, st):
        self.v = None
        self.dep = None
        self.op_str = None
        if st.isdigit():
            self.v = int(st)
        else:
            data = st.split()
            self.p1 = data[0]
            self.op_str = data[1]
            self.p2 = data[2]
            self.op = self.make_op(self.op_str)

    def make_op(self, op):
        if op == "+":
            return lambda x, y: x + y
        if op == "-":
            return lambda x, y: x - y
        if op == "*":
            return lambda x, y: x * y
        if op == "/":
            return lambda x, y: x // y
        raise Exception("Oh no")

    def make_reverse_op(self, op, pos=None):
        if op == "+":
            return lambda x, y: x - y
        if op == "-":
            if pos == 1:
                return lambda x, y: x + y
            else:
                return lambda x, y: y - x
        if op == "*":
            return lambda x, y: x // y
        if op == "/":
            if pos == 1:
                return lambda x, y: x * y
            else:
                return lambda x, y: y // x
        raise Exception("Oh no")        

    def update(self):
        if self.v is None:
            if isinstance(self.p1, str) and monkeys[self.p1].v is not None:
                self.p1 = monkeys[self.p1].v
            if isinstance(self.p2, str) and monkeys[self.p2].v is not None:
                self.p2 = monkeys[self.p2].v
            if isinstance(self.p1, int) and isinstance(self.p2, int):
                self.v = self.op(self.p1, self.p2)
                if self.dep is not None:
                    self.dep.update()

    def calc(self, target):
        if isinstance(self.p1, str) and isinstance(self.p2, int):
            pos = 1
            op = self.make_reverse_op(self.op_str, pos)
            monkeys[self.p1].calc(op(target, self.p2))
        elif isinstance(self.p1, int) and isinstance(self.p2, str):
            pos = 2
            op = self.make_reverse_op(self.op_str, pos)
            monkeys[self.p2].calc(op(target, self.p1))
        else:
            raise Exception('Not good')


class RootMonkey:
    def __init__(self, st):
        self.v = None
        self.dep = None
        if st.isdigit():
            self.v = int(st)
        else:
            data = st.split()
            self.p1 = data[0]
            self.p2 = data[2]

    def update(self):
        if self.v is None:
            if isinstance(self.p1, str) and monkeys[self.p1].v is not None:
                self.p1 = monkeys[self.p1].v
            if isinstance(self.p2, str) and monkeys[self.p2].v is not None:
                self.p2 = monkeys[self.p2].v

    def calc(self):
        if isinstance(self.p1, str) and isinstance(self.p2, int):
            monkeys[self.p1].calc(self.p2)
        elif isinstance(self.p1, int) and isinstance(self.p2, str):
            monkeys[self.p2].calc(self.p1)
        else:
            raise Exception('Not good')


class Human:
    def __init__(self):
        self.v = None
        self.dep = None

    def calc(self, target):
        self.v = target


monkeys = {}

with open(input_file) as f:
    for line in f:
        line = line.strip()
        if line != "":
            data = line.split(":")
            name = data[0].strip()
            st = data[1].strip()
            if name == "root":
                monkeys[name] = RootMonkey(st)
            elif name == "humn":
                monkeys[name] = Human()
            else:
                monkeys[name] = Monkey(st)


for m in monkeys.values():
    if m.v is None and not isinstance(m, Human):
        if isinstance(m.p1, str):
            monkeys[m.p1].dep = m
        if isinstance(m.p2, str):
            monkeys[m.p2].dep = m


m = monkeys["root"]
q1 = deque([m])
q2 = deque()
while len(q1) > 0:
    m = q1.popleft()
    q2.append(m)
    if m.v is None:
        if not isinstance(monkeys[m.p1], Human):
            q1.append(monkeys[m.p1])
        if not isinstance(monkeys[m.p2], Human):            
            q1.append(monkeys[m.p2])
    else:
        m.dep.update()

monkeys['root'].calc()

print(monkeys["humn"].v)
