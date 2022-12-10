trees = list()
seen = set()

with open('day8/input.txt') as f:
    for line in [l.strip() for l in f]:
        trees.append(list(map(int, list(line))))

forest_size = len(trees)

# obviously, it would be better not to iterate the whole thing 
# four times. I bet this burns me in step 2
# from left
for y in range(0, forest_size):
    highest = -1
    for x in range(0, forest_size):
        if trees[y][x] > highest:
            highest = trees[y][x]
            seen.add((x,y))
# from right
for y in range(0, forest_size):
    highest = -1
    for x in range(forest_size - 1, -1, -1):
        if trees[y][x] > highest:
            highest = trees[y][x]
            seen.add((x,y))      
# from top
for x in range(0, forest_size):
    highest = -1
    for y in range(0, forest_size):
        if trees[y][x] > highest:
            highest = trees[y][x]
            seen.add((x,y))
# from bottom
for x in range(0, forest_size):
    highest = -1
    for y in range(forest_size - 1, -1, -1):
        if trees[y][x] > highest:
            highest = trees[y][x]
            seen.add((x,y))

print(len(seen))

trees_to_check = list()
scenic_scores = dict()

def calc_scenic_score(x,y):
    height = trees[y][x]
    up_score, down_score, left_score, right_score = 0, 0, 0, 0
    # up
    for y2 in range(y - 1, -1, -1):
        up_score += 1
        if trees[y2][x] >= height:
            break
    # down
    for y2 in range(y + 1, forest_size):
        down_score += 1
        if trees[y2][x] >= height:
            break
    # left
    for x2 in range(x - 1, -1, -1):
        left_score += 1
        if trees[y][x2] >= height:
            break
    # right
    for x2 in range(x + 1, forest_size):
        right_score += 1
        if trees[y][x2] >= height:
            break
    return up_score * down_score * left_score * right_score


for y in range(1, forest_size - 1):
    for x in range(1, forest_size -1):
        scenic_scores[(x,y)] = calc_scenic_score(x,y)

print(max(scenic_scores.values()))








