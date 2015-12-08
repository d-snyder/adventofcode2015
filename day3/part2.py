import sys
from sets import Set


def main(fname):
    visits = Set([(0, 0)])
    santa = (0, 0)
    robo_santa = (0, 0)
    count = 0

    line = open(fname).readline()
    for c in line:
        if count % 2 == 0:
            santa = calculate_new_position(c, santa)
            visits.add(santa)
        else:
            robo_santa = calculate_new_position(c, robo_santa)
            visits.add(robo_santa)
        count += 1
    print len(visits)


def calculate_new_position(c, pos):
    x = pos[0]
    y = pos[1]

    if c == '>':
        x += 1
    elif c == '<':
        x -= 1
    elif c == '^':
        y += 1
    elif c == 'v':
        y -= 1

    return (x, y)


if __name__ == '__main__':
    fname = "input.txt"
    if len(sys.argv) > 1:
        fname = sys.argv[1]
    main(fname)
