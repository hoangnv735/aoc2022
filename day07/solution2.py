# input_file = 'example.txt'
input_file = "input.txt"


class File:
    def __init__(self, name, is_dir, size=0, parent=None):
        self.name = name
        self.size = size
        self.parent = parent
        self.is_dir = is_dir
        self.children = []

    def abs_path(self):
        ...

    def __repr__(self):
        return self.name

    def update_size(self, size):
        self.size += size

    def update_child(self, child):
        self.children.append(child)
        child.parent = self


def is_cmd(text):
    return text[0] == "$"


cur_dir = File("/", is_dir=True)
files = [cur_dir]

with open(input_file) as f:
    for line in f:
        line = line.strip()
        if is_cmd(line):
            data = line.split(" ")
            command = data[1]
            if command == "cd":
                param = data[2]
                if param == ".":
                    continue
                elif param == "..":
                    cur_dir = cur_dir.parent
                else:
                    for child in cur_dir.children:
                        if child.name == param:
                            cur_dir = child
                            break
            elif command == "ls":
                continue
        else:
            data = line.split(" ")
            if data[0].isdigit():
                new_dir = File(data[1], is_dir=False, size=int(data[0]))
            else:
                new_dir = File(data[1], is_dir=True)
            files.append(new_dir)
            cur_dir.update_child(new_dir)

checked = [False] * len(files)


def compute_size(file):
    if not file.is_dir:
        return file.size
    for child in file.children:
        file.update_size(compute_size(child))
    return file.size


compute_size(files[0])

dir_size = [f.size for f in files if f.is_dir]
dir_size.sort()
required_size = 30000000 - (70000000 - files[0].size)
print(required_size)
for s in dir_size:
    if s >= required_size:
        print(s)
        break
