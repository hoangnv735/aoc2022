input_file = 'input.txt'
# input_file = "example.txt"

cnt = 0
with open(input_file) as f:
    for line in f:
        if line.strip() == '':
            continue
        data = line.strip().split(',')
        start1 = int(data[0].split('-')[0])
        end1 = int(data[0].split('-')[1])
        start2 = int(data[1].split('-')[0])
        end2 = int(data[1].split('-')[1])
        if start1<= start2 and end2 <= end1:
            cnt += 1
        elif start2 <= start1 and end1 <= end2:
            cnt += 1
        elif start1 <= start2 and start2 <= end1:
            cnt += 1
        elif start2 <= start1 and start1 <= end2:
            cnt += 1

print(cnt)
