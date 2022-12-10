SEGMENT_COUNT = 9
visited_points_list = list()
head_moves = list()

def is_adjacent(hx: int, hy: int, tx: int, ty: int) -> bool:
    if abs(hx - tx) <= 1 and abs(hy-ty) <=1:
        return True
    else:
        return False

def move_tail(hx: int, hy: int, tx: int, ty: int) -> tuple():
    x_delta, y_delta = 0, 0
    
    if hx > tx:
        x_delta += 1
    elif hx < tx:
        x_delta -= 1
    
    if hy > ty:
        y_delta += 1
    elif hy < ty:
        y_delta -= 1
    
    return (x_delta, y_delta)


with open('day9/input.txt') as f:
    for line in [l.strip() for l in f]:
        dir, distance = line.split(' ')
        if dir == 'U':
            for _ in range(int(distance)):
                head_moves.append((0, 1))
        elif dir == 'D':
            for _ in range(int(distance)):
                head_moves.append((0, -1))
        elif dir == 'R':
            for _ in range(int(distance)):
                head_moves.append((1, 0))
        elif dir == 'L':
            for _ in range(int(distance)):
                head_moves.append((-1, 0))

moves = head_moves
for _ in range(SEGMENT_COUNT):
    visited_points = set()
    new_moves = list()
    visited_points.add((0,0))
    head_loc_x, head_loc_y, tail_loc_x, tail_loc_y = 0, 0, 0, 0
    for dx, dy in moves:
        head_loc_x += dx
        head_loc_y += dy
        if not is_adjacent(head_loc_x, head_loc_y, tail_loc_x, tail_loc_y):
            tail_delta = move_tail(head_loc_x, head_loc_y, tail_loc_x, tail_loc_y)
            tail_loc_x += tail_delta[0]
            tail_loc_y += tail_delta[1]
            new_moves.append(tail_delta)
            visited_points.add((tail_loc_x, tail_loc_y))
    visited_points_list.append(visited_points)
    moves = new_moves

print(len(visited_points_list[-1]))


