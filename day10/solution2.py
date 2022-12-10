# input_file = 'example.txt'
input_file = "input.txt"

cur_cycle = 0
x = 1
crt_line = []
with open(input_file) as f:
    for line in f:
        line = line.strip()
        if line != "":
            data = line.split()
            if data[0] == "noop":
                if (cur_cycle % 40) in [x - 1, x, x + 1]:
                    crt_line.append("#")
                else:
                    crt_line.append(".")
                cur_cycle += 1
                if cur_cycle > 239:
                    break
            else:
                v = int(data[1])
                for _ in range(2):
                    if (cur_cycle % 40) in [x - 1, x, x + 1]:
                        crt_line.append("#")
                    else:
                        crt_line.append(".")
                    cur_cycle += 1
                    if cur_cycle > 239:
                        break
                x += v

print("\n".join(["".join(crt_line[i * 40 : (i + 1) * 40]) for i in range(6)]))
