class Folder:
    def __init__(self, name, parent):
        self.name = name
        self.files = list() 
        self.subfolders = list()
        self.size = 0
        self.parent = parent

root_dir = Folder('/', None)
working_dir = root_dir
all_dirs = list()

with open('day7/day7-input.txt') as f:
    for line in [l.strip() for l in f]:
        if line[0] == '$':
            if line[2:4] == 'cd':
                _,_, nd = line.split(' ')
                if nd == '/':
                    working_dir = root_dir
                elif nd == '..':
                    working_dir = working_dir.parent
                else:
                    cd = Folder(nd, working_dir)
                    working_dir.subfolders.append(cd)
                    all_dirs.append(cd)
                    working_dir = cd
            elif line[2:4] == 'ls':
                pass
        else:
            if line[0:3] == 'dir':
                _, d = line.split(' ')
                working_dir.subfolders.append(Folder(nd, working_dir))
            else:
                sz, f = line.split(' ')
                if f not in working_dir.files:
                    working_dir.size += int(sz)
                    working_dir.files.append(f)
                    pd = working_dir.parent
                    while pd != None:
                        pd.size += int(sz)
                        pd = pd.parent

print(sum(map(lambda y: y.size, filter(lambda x: x.size <= 100000, all_dirs))))
size_to_delete = 30000000 - (70000000 - root_dir.size)
print(next(filter(lambda y: y.size >= size_to_delete, sorted(all_dirs, key=lambda x: x.size))).size)