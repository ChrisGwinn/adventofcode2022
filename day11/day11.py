
from collections import deque
from functools import partial
import operator
import re

class monkey:
    def __init__(self, monkey_list) -> None:
        self.items_held = deque()
        self.monkeys = monkey_list
        self.inspected_count = 0
        self.true_dest = 0
        self.false_dest = 0
        self.divisor = 0
        self.inspect_func = None
        self.worry_decay = False

    def find_destination(self, worry) -> int:
        if worry % self.divisor == 0:
            return self.true_dest
        else:
            return self.false_dest

    def inspect(self, worry) -> int:
        self.inspected_count += 1
        return self.inspect_func(worry)

    def inspect_items(self, modulo):
        while len(self.items_held) > 0:
            itm = self.items_held.popleft()
            itm = self.inspect(itm)
            if self.worry_decay:
                itm = itm//3
            else:
                itm = itm % modulo
            self.monkeys[self.find_destination(itm)].items_held.append(itm)

monkeys = list()

magic_monkey_num = 1 
with open('day11/input.txt') as f:
    line_count = 0
    for line in [l.rstrip() for l in f]:
        line_type = line_count % 7
        # why did I not upgrade to python 3.10 before starting advent of code?
        if line_type == 0:
            new_monkey = monkey(monkeys)
        elif line_type == 1:
            for i in re.findall(r'\d+', line):
                new_monkey.items_held.append(int(i))
        elif line_type == 2:
            worry_func_match = re.search(r'(?:new = old )([+*]) (\w+)', line)
            if worry_func_match[1] == '*':
                if worry_func_match[2] == 'old':
                    new_monkey.inspect_func = lambda x: x * x
                else:
                    new_monkey.inspect_func = partial(operator.mul, int(worry_func_match[2]))
            else:
                if worry_func_match[2] == 'old':
                    new_monkey.inspect_func = lambda x: x + x
                else:
                    new_monkey.inspect_func = partial(operator.add, int(worry_func_match[2]))
        elif line_type == 3:
            new_monkey.divisor = int(re.search(r'\d+', line)[0])
            magic_monkey_num *= new_monkey.divisor
        elif line_type == 4:
            new_monkey.true_dest = int(re.search(r'\d+', line)[0]) 
        elif line_type == 5:
            new_monkey.false_dest = int(re.search(r'\d+', line)[0])
            monkeys.append(new_monkey)      

        line_count += 1

for _ in range(10000):
    for m in monkeys:
        m.inspect_items(magic_monkey_num)

top_two = sorted([m.inspected_count for m in monkeys])[-2:]
print(top_two[0] * top_two[1])

# I didn't figure out the trick for part 2 and had to look something up. 
# It's the AoC golden rule - if you don't need something to calculate the answer, you don't
# need to keep it around