
from itertools import tee
import re

blocked_sqs = set()

# I really need to remember to update python
def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

with open('day14/input.txt') as f:
    for l in f:
        for seg in pairwise(re.findall(r'(\d+),(\d+)', l)):
            start = (int(seg[0][0]), int(seg[0][1]))
            end = (int(seg[1][0]), int(seg[1][1]))
            if start[0] == end[0]:
                count_step = 1 if start[1] < end[1] else -1
                for i in range(start[1], end[1] + count_step, count_step):
                    sq = (start[0], i)
                    blocked_sqs.add(sq)
            else:
                count_step = 1 if start[0] < end[0] else -1
                for i in range(start[0], end[0] + count_step, count_step):
                    sq = (i, start[1])
                    blocked_sqs.add(sq)
    void_line = max([s[1] for s in blocked_sqs])



def find_resting_point_1(drop_x, drop_y):
    if drop_y == void_line:
        return None
    elif (drop_x, drop_y + 1) not in blocked_sqs_1:
        return find_resting_point_1(drop_x, drop_y + 1)
    elif (drop_x -1, drop_y + 1) not in blocked_sqs_1:
        return find_resting_point_1(drop_x -1, drop_y + 1)
    elif (drop_x +1, drop_y + 1) not in blocked_sqs_1:
        return find_resting_point_1(drop_x +1, drop_y + 1)
    else:
        return (drop_x, drop_y)

origin = (500, 0)
blocked_sqs_1 = blocked_sqs.copy()
sandy_sqs_1 = set()
# part 1
# while True:
#     new_sand_loc = find_resting_point_1(origin[0], origin[1])
#     if new_sand_loc != None:
#         blocked_sqs_1.add(new_sand_loc)
#         sandy_sqs_1.add(new_sand_loc)
#     else:
#         break
# print(len(sandy_sqs_1))

# part 2
blocked_sqs_2 = blocked_sqs.copy()
sandy_sqs_2 = set()
floor = void_line + 2
def find_resting_point_2(drop_x, drop_y):
    if drop_y + 1 == floor:
        return (drop_x, drop_y)
    elif (drop_x, drop_y + 1) not in blocked_sqs_2:
        return find_resting_point_2(drop_x, drop_y + 1)
    elif (drop_x -1, drop_y + 1) not in blocked_sqs_2:
        return find_resting_point_2(drop_x -1, drop_y + 1)
    elif (drop_x +1, drop_y + 1) not in blocked_sqs_2:
        return find_resting_point_2(drop_x +1, drop_y + 1)
    else:
        return (drop_x, drop_y)

while True:
    new_sand_loc = find_resting_point_2(origin[0], origin[1])
    if new_sand_loc == origin:
        sandy_sqs_2.add(origin)
        break
    elif new_sand_loc != None:
        blocked_sqs_2.add(new_sand_loc)
        sandy_sqs_2.add(new_sand_loc)

print(len(sandy_sqs_2))