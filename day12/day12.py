from turtle import done


start_square = (0,0)
end_square = (0,0)
max_col, max_row = -1, -1
heights = dict()

with open('day12/input.txt') as f:
    for line in [l.rstrip() for l in f]:
        max_row += 1
        if max_col == -1:
            max_col = len(line) - 1
        for i in range(len(line)):
            if line[i] == 'S':
                 heights[(i, max_row)] = 0
                 start_square = (i, max_row)
            elif line[i] == 'E':
                heights[(i, max_row)] = 25
                end_square = (i, max_row)
            else:
                heights[(i, max_row)] = ord(line[i]) - 97

distances = dict()
distance = 1
distances[end_square] = 0
active_squares = set()
active_squares.add(end_square)

def find_linked_squares(sq_x, sq_y):
    links = list()
    height = heights[(sq_x, sq_y)]
    # up
    if sq_y > 0:
        if heights[(sq_x, sq_y - 1)] + 1 >= height:
            links.append((sq_x, sq_y - 1))
    # down
    if sq_y < max_row:
        if heights[(sq_x, sq_y + 1)] + 1 >= height:
            links.append((sq_x, sq_y + 1))
    # left
    if sq_x > 0:
        if heights[(sq_x - 1, sq_y)] + 1 >= height:
            links.append((sq_x - 1, sq_y))
    # right
    if sq_x < max_col:
        if heights[(sq_x + 1, sq_y)] +1 >= height:
            links.append((sq_x + 1, sq_y))
    return links
 
# starting_points = [start_square]
starting_points = [y[0] for y in filter(lambda x: x[1] == 0, heights.items())]

done = False
while not done:
    next_batch = set()
    for sq in active_squares:
        for lsq in find_linked_squares(sq[0], sq[1]):
            if lsq in starting_points:
                distances[lsq] = distance
                print(distance)
                done = True
            elif lsq not in distances:
                distances[lsq] = distance
                next_batch.add(lsq)
    active_squares = next_batch
    distance += 1
