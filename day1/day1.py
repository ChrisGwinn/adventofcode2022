with open('day1/day1-input.txt') as f:
    elves = list()
    foods = list()
    for line in [l.strip() for l in f]:
        if len(line) > 0:
            cals = int(line)
            foods.append(cals)
        else:
            elves.append(sum(foods))
            foods = list()

elf_totals = sorted(elves, reverse=True)
print(elf_totals[0])
print(sum(elf_totals[:3]))