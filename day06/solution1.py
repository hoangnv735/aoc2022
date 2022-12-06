# input_file = 'example.txt'
input_file = 'input.txt'
data = open(input_file).read().strip()

def valid(s):
    return len(s) == len(set(s))
    
for i in range(3,len(data)):
    if valid(data[i-3:i+1]):
        print(i+1)
        break
    
