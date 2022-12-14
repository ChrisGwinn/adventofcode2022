from functools import cmp_to_key
from operator import indexOf

ORDERED = -1
NOT_ORDERED = 1
NEXT = 0

def in_order(l, r) -> int:
    # print(f'comparing {l} and {r}')
    if isinstance(l, int)  and isinstance(r, int):
        if l < r:
            return ORDERED
        elif r < l:
            return NOT_ORDERED
        else:
            return NEXT
    
    if isinstance(l, list):
        if  isinstance(r, list):
            if len(l) == 0:
                if  len(r) > 0:
                    return ORDERED
                elif len(r) == 0:
                    return NEXT
            elif len(r) == 0:
                return NOT_ORDERED
            else:
                fv = in_order(l[0], r[0])
                if fv == NEXT:
                    return in_order(l[1:],r[1:])
                else:
                    return fv
        else:
            wrapped_r = list()
            wrapped_r.append(r)
            return in_order(l, wrapped_r)
    else:
        wrapped_l = list()
        wrapped_l.append(l)
        return in_order(wrapped_l, r)

with open('day13/input.txt') as f:
    line_count = 1
    ordered = list()
    left, right = None, None
    for line in [l.rstrip() for l in f]:
        if (line_count %3) == 0:
            if in_order(left, right) == ORDERED:
                ordered.append(line_count // 3)
            left, right = None, None
        elif (line_count % 3) == 1:
            # actually using eval() on third-party input feels wildly transgressive
            left = eval(line)
        else:
            right = eval(line)
        line_count += 1
    print(sum(ordered))

packets = list()
divider_1 = [[2]]
divider_2 = [[6]]
packets.append(divider_1)
packets.append(divider_2)

with open('day13/input.txt') as f:
    for line in [l.rstrip() for l in f]:
        if line != '':
            packets.append(eval(line))

sorted_packets = sorted(packets, key=cmp_to_key(in_order))
print((indexOf(sorted_packets, divider_1) + 1) * (indexOf(sorted_packets, divider_2) + 1))

