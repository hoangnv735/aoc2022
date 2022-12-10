# input_file = 'example.txt'
input_file = 'input.txt'

total = 0
cur_cycle = 1
x = 1
with open(input_file) as f:
    for line in f:
        line = line.strip()
        if line != '':
            data = line.split()
            if data[0] == 'noop':
                if (cur_cycle + 20) % 40 == 0:
                    total += x * cur_cycle
                cur_cycle += 1
                if cur_cycle > 220:
                    break
            else:
                v = int(data[1])
                for _ in range(2):
                    if (cur_cycle + 20) % 40 == 0:
                        total += x * cur_cycle
                    cur_cycle += 1
                    if cur_cycle > 220:
                        break
                x += v

print(total)  
