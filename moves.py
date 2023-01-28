f = [[3, 8, 22, 13], [4, 6, 21, 15], [9, 11, 12, 10]]
r = [[13, 15, 16, 14], [4, 12, 24, 17], [2, 10, 22, 19]]
u = [[1, 3, 4, 2], [9, 13, 17, 5], [10, 14, 18, 6]]

notr_moves = [{0, 0}, {1, 1}, {2, 2}, {3, 3}, {4, 4}, {5, 5}, {6, 6}, {7, 7}, {8, 8},
              {0, 1}, {3, 4}, {6, 7}]  # If they follow each other they are senseless.

def move(m, p,last):
    for q in m:
        if p == 0:
            h = last[q[0]]
            last[q[0]] = last[q[1]]
            last[q[1]] = last[q[2]]
            last[q[2]] = last[q[3]]
            last[q[3]] = h
        elif p == 1:
            h = last[q[0]]
            last[q[0]] = last[q[3]]
            last[q[3]] = last[q[2]]
            last[q[2]] = last[q[1]]
            last[q[1]] = h
        elif p == 2:
            h = last[q[0]]
            last[q[0]] = last[q[2]]
            last[q[2]] = h
            h = last[q[1]]
            last[q[1]] = last[q[3]]
            last[q[3]] = h
    return last
