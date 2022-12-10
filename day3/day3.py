#part 1
with open('day3/day3-input.txt') as f:
    total = 0
    for line in [l.strip() for l in f]:
        sack1 = line[:len(line)//2]
        sack2 = line[len(line)//2:]
        shared_item = set(sack1).intersection(set(sack2)).pop()
        if shared_item.isupper():
            total += (ord(shared_item) - 38)
        else:
           total += (ord(shared_item) - 96)
    print(total)

# part 2
with open('day3/day3-input.txt') as f:
    count, total = 0, 0
    sack1, sack2, sack3 = '','',''
    for line in [l.strip() for l in f]:
        count += 1
        if count % 3 == 1:
            sack1 = line
        elif count %3 == 2:
            sack2 = line
        else:
            sack3 = line
            badge = set(sack1).intersection(set(sack2)).intersection(set(sack3)).pop()
            if badge.isupper():
                total += (ord(badge) - 38)
            else:
                total += (ord(badge) - 96)
    print(total)


