import re
#part 1
elf_pairs = list()
with open('day4/day4-input.txt') as f:
    for line in f:
        nums = re.findall(r'\d+', line)
        elf_pairs.append(((int(nums[0]), int(nums[1])), (int(nums[2]), int(nums[3]))))

contain_count = 0
for ep in elf_pairs:
    if ep[0][0] <= ep[1][0] and ep[0][1] >= ep[1][1]:
        contain_count += 1
    elif ep[1][0] <= ep[0][0] and ep[1][1] >= ep[0][1]:
        contain_count += 1
print(contain_count)

# part 2
overlap_count = 0
for ep in elf_pairs:
    if ep[0][0] <= ep[1][0]:
        if ep[0][1] >= ep[1][0]:
            overlap_count += 1
    else:
        if ep[1][1] >= ep[0][0]:
            overlap_count += 1

print(overlap_count)

        