from inspect import iscoroutinefunction


with open('day2/day2-input.txt') as f:
    pairs = list()
    for line in [l.strip() for l in f]:
        pairs.append(tuple(line.split(' ')))

# day 1
scores = {'X': 1,'Y':2, 'Z':3}
identity = {'A':'X', 'B':'Y', 'C':'Z'}
winners = {'A':'Y', 'B':'Z', 'C':'X'}

my_score = 0

for (them, me) in pairs:
    my_score += scores[me]
    if identity[them] == me:
        # tie
        my_score += 3
    elif winners[them] == me:
        # win
        my_score += 6

print(my_score)


# day 2
# oh man, I am rusty. I should have converted all these to numbers on load
winners_for_real = {'A': 'B', 'B':'C', 'C':'A'}
losers_for_real = {'B':'A', 'C':'B', 'A':'C'}
scores_for_real =  {'A': 1,'B':2, 'C':3}

my_score = 0

for (them, result) in pairs:
    me = ''
    if result == 'X':
        # lose
        me = losers_for_real[them]
    elif result == 'Y':
        # tie
        me = them
        my_score += 3
    else:
        # win
        me = winners_for_real[them]
        my_score += 6
    my_score += scores_for_real[me]

print(my_score)
