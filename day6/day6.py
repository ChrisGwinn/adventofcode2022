def is_break(w):
    return len(set(w)) == len(w)

with open('day6/day6-input.txt') as f:
    packet_starts = list()
    signal = f.readline().strip()
    size = 14
    for i in range(size, len(signal)):
        window = signal[i-size:i]
        if (is_break(window)):
            print(i)
            break


