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


monkeys = {}

with open(input_file) as f:
    for line in f:
        line = line.strip()
        if line != "":
            data = line.split(":")
            name = data[0].strip()
            st = data[1].strip()
            monkeys[name] = Monkey(st)


for m in monkeys.values():
    if m.v is None:
        if isinstance(m.p1, str):
            monkeys[m.p1].dep = m
        if isinstance(m.p2, str):
            monkeys[m.p2].dep = m


m = monkeys["root"]
q1 = deque([m])
while len(q1) > 0:
    m = q1.popleft()
    if m.v is None:
        q1.append(monkeys[m.p1])
        q1.append(monkeys[m.p2])
    else:
        m.dep.update()

print(monkeys["root"].v)
