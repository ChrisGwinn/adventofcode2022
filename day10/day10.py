instruction_queue = list()
# the puzzle starts at 1 and I don't want to be fiddly
instruction_queue.append(1)

with open('day10/input.txt') as f:
    for line in [l.strip() for l in f]:
        if line.startswith('addx'):
            _, n = line.split(' ')
            instruction_queue.append(0)
            instruction_queue.append(int(n))
        else:
            instruction_queue.append(0)

relevant_values = list()
for i in range(20, len(instruction_queue), 40):
        relevant_values.append(sum(instruction_queue[0:i]) * i)

print(sum(relevant_values))

rv = 1
line = ''
for i in range(1, len(instruction_queue)):
    col = i % 40
    if col == 0:
        print(line)
        line = ''
    
    rv += instruction_queue[i]
    if abs(rv - col) <= 1:
        line = line + '#'
    else:
        line = line + '.'
print(line)




