# input_file = "example.txt"
input_file = "input.txt"

def parse(p):
    data = []
    cur = ''
    idx = 1
    # only parse from idx 1 to idx len - 2
    while idx < len(p) - 1:
        c = p[idx]
        if ord('0') <= ord(c) and ord(c) <= ord('9'):
            cur += c
        elif c == ',':
            if cur != '':
                data.append(int(cur)) 
                cur = ''
        elif c == '[':
            stack = 1
            sub_p = c
            while stack > 0:
                idx += 1
                sub_p += p[idx]
                if p[idx] == '[':
                    stack += 1
                elif p[idx] == ']':
                    stack -= 1
            data.append(parse(sub_p))
        idx += 1
    if cur != '':
        data.append(int(cur))
        cur = ''
    return data

def compare_list(o1, o2):
    l1 = len(o1)
    l2 = len(o2)
    idx = 0
    if l1 == 0 and l2 > 0:
        return 1
    elif l1 > 0 and l2 == 0:
        return -1

    while idx < max(l1, l2):
        v1 = None
        v2 = None
        try:
            v1 = o1[idx]
        except:
            v1 = None

        try: 
            v2 = o2[idx]
        except:
            v2 = None

        if v1 is None and v2 is not None:
            return 1
        elif v1 is not None and v2 is None:
            return -1
        elif v1 is not None and v2 is not None:
            res = compare(v1, v2)
            if res != 0:
                return res
            else:
                idx += 1
        else:
            raise ValueError()
    return 0

def compare(o1, o2):
    if isinstance(o1, list) and isinstance(o2, list):
        return compare_list(o1, o2)
    elif isinstance(o1, list) and isinstance(o2, int):
        return compare_list(o1, [o2])
    elif isinstance(o1, int) and isinstance(o2, list):
        return compare_list([o1], o2)
    elif isinstance(o1, int) and isinstance(o2, int):
        if o1 < o2:
            return 1
        elif o1 == o2:
            return 0
        else:
            return -1
    else:
        raise ValueError(f"{type(o1)} {type(o2)}")

def compute(p1, p2):
    p1 = parse(p1)
    p2 = parse(p2)
    res = compare_list(p1, p2)
    return res

d1 = parse('[[2]]')
d2 = parse('[[6]]')
idx1 = 1
idx2 = 0
cnt = 0
with open(input_file) as f:
    for line in f:
        line = line.strip()
        if line != "":
            cnt += 1 
            p = parse(line)
            res = compare_list(p, d1)
            if res == 1:
                idx1 += 1
            res = compare_list(d2, p)
            if res == 1:
                idx2 += 1

idx2 = cnt + 2 - idx2
print(idx1, idx2)
print(idx1 * idx2)
