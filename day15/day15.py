from cgi import print_environ_usage
import re

# loong sigh. This is heading into the world of math I don't have


beacons = list()
sensors = dict()
with open('day15/input.txt') as f:
    for l in f:
        for sensor in re.findall(r'x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)', l):
            sensor_x = int(sensor[0])
            sensor_y = int(sensor[1])
            beacon_x = int(sensor[2])
            beacon_y = int(sensor[3])
            distance = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
            beacons.append((beacon_x, beacon_y))
            sensors[(sensor_x, sensor_y)] = distance

# part 1
line_to_check = 2000000
impossible_points = set()
for k,v in sensors.items():
    dist_from_line = abs(k[1] - line_to_check)
    for i in range((v - dist_from_line) + 1):
        impossible_points.add(k[0] + i)
        impossible_points.add(k[0] - i)

for b in filter(lambda x: x[1] == line_to_check, beacons):
     impossible_points.discard(b[0])

print(len(impossible_points))

# part 2
# point sets definitely don't work here!

def cut_range(ranges, cut_start, cut_end) -> list:
    new_ranges = list()
    for r in ranges:
        # no overlap
        if r[1] < cut_start or r[0] > cut_end:
            new_ranges.append(r)
        elif r[0] >= cut_start and r[1] <= cut_end:
            # range entirely contained in cut
            pass
        elif r[0] < cut_start and r[1] > cut_end:
            # cut entirely in range
            new_ranges.append((r[0], cut_start - 1))
            new_ranges.append((cut_end + 1, r[1]))
        elif r[0] >= cut_start and r[1] >= cut_end:
            new_ranges.append((cut_end + 1, r[1]))
        elif r[0] <= cut_start and r[1] <= cut_end:
            new_ranges.append((r[0], cut_start - 1))
            
    return new_ranges

max_val = 4000000
sensors = sorted(sensors.items(), key=lambda item: item[1], reverse=True)
for y in range(0, max_val + 1):
    ranges = list()
    ranges.append((0, max_val))
    for k,v in sensors:
        dist_from_line = abs(k[1] - y)
        if dist_from_line <= v:
            ranges = cut_range(ranges, k[0] - (v - dist_from_line), k[0] + (v-dist_from_line))
            if len(ranges) == 0:
                break
    if len(ranges) > 0:
        print((ranges[0][0] * 4000000) + y)
        break
        

            