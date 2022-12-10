import re

# part 1
def move_crates(stacks, count, move_from, move_to):
    for _ in range(count):
        stacks[move_to - 1].append(stacks[move_from - 1].pop())
# part 2
def move_crates_in_stack(stacks, count, move_from, move_to):
    temp = list()
    for _ in range(count):
        temp.append(stacks[move_from - 1].pop())
    while len(temp) > 0:
        stacks[move_to -1].append(temp.pop())

stacks = list()
with open('day5/day5-input.txt') as f:
    for line in f:
        if len(stacks) == 0:
            for _ in range(0, len(line)//4):
                stacks.append(list())
        if '[' in line:
            # I am sure there's a cool pythonic way to do this. Perhaps I will remember after coffee
            i = 0
            while (i * 4) <= len(line):
                stk = line[i * 4:i * 4 + 4]
                if stk.startswith('['):
                    stacks[i].insert(0, stk[1:2])
                i += 1
        elif line.startswith('move'):
            nums = re.findall(r'\d+', line)
            move_crates_in_stack(stacks, int(nums[0]), int(nums[1]), int(nums[2]))

print(''.join(s[-1] for s in stacks))
