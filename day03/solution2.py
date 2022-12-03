input_file = 'input.txt'
# input_file = "example.txt"

bags = []
with open(input_file) as f:
    for line in f:
        data = line.strip()
        bags.append(data)

total = 0
for i in range(0, len(bags), 3):
    
    join = set(bags[i]) & set(bags[i + 1]) & set(bags[i + 2])
    e = list(join)[0]
    score = ord(e) - ord("a") + 1 if ord(e) >= ord("a") else ord(e) - ord("A") + 27
    total += score  
    print(join, score)
print(total)
