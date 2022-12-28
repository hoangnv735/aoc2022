# input_file = "example.txt"
input_file = 'input.txt'


class Node:
    def __init__(self, v):
        self.v = v
        self.before = None
        self.after = None

    def __repr__(self):
        # return f"{self.before.v} {self.v} {self.after.v}"
        return f"{self.v}"


s = list(map(Node, map(int, open(input_file).read().strip().split("\n"))))
l = len(s)
# print(l)
# node_0 = None
# for node in s:
#     if node.v == 0:
#         node_0 = node
#         break

for idx, node in enumerate(s):
    # print((idx - 1) % l, idx, (idx + 1) % l)
    node.before = s[(idx - 1) % l]
    node.after = s[(idx + 1) % l]
# print(s[-10:])


def move(node):
    v = node.v
    if v > 0:
        pointer = node
        d = abs(v) % (l - 1)
        if d > 0:
            nb = node.before
            na = node.after
            nb.after = na
            na.before = nb

            while d > 0:
                pointer = pointer.after
                d -= 1

            pa = pointer.after

            pointer.after = node
            node.after = pa
            node.before = pointer
            pa.before = node
    elif v < 0:
        pointer = node
        d = abs(v) % (l - 1)
        if d > 0:
            nb = node.before
            na = node.after
            nb.after = na
            na.before = nb
            while d > 0:
                pointer = pointer.before
                d -= 1

            pb = pointer.before

            pb.after = node
            node.after = pointer
            pointer.before = node
            node.before = pb
    else:
        global node_0
        node_0 = node


def print_all():
    pointer = node_0
    d = l
    output = []
    while d > 0:
        output.append(pointer.v)
        pointer = pointer.after
        d -= 1
    print(output)


# print_all()
for node in s:
    move(node)
    # print_all()

r = 1000 % l
total = 0
pointer = node_0
for _ in range(3):
    d = r
    while d > 0:
        pointer = pointer.after
        d -= 1
    # print(pointer.v)
    total += pointer.v

print(total)
