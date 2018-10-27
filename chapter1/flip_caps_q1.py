def pleaseConform(caps):
    start = forward = backward = 0
    intervals = []
    for i in range(1, len(caps)):
        if caps[start] != caps[i]:
            intervals.append((start, i-1, caps[start]))
            if caps[start] == 'F':
                forward += 1
            else:
                backward += 1
            start = i
    intervals.append((start, len(caps)-1, caps[start]))
    if caps[start] == 'F':
        forward += 1
    else:
        backward += 1
    if forward < backward:
        flip = 'F'
    else:
        flip = 'B'
    for t in intervals:
        if t[2] == flip:
            if t[0] == t[1]:
                print('Person at position {0} flip your cap!'.format(t[0]))
            else:
                print('People in positions {0} through {1} flip your caps!'.format(t[0], t[1]))

if __name__ == '__main__':
    caps1 = ['F', 'F', 'B', 'B', 'B', 'F', 'B',
             'B', 'B', 'F', 'F', 'B', 'F']
    pleaseConform(caps1)
