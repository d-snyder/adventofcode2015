import re
import sys

lights = [[0 for x in range(1000)] for x in range(1000)]


def main(fname):
    p = re.compile('(turn on|turn off|toggle)\s*([0-9]+),([0-9]+)\s*through\s*([0-9]+),([0-9]+)')
    for line in open(fname):
        m = p.match(line.rstrip())
        operation = m.group(1)
        x = int(m.group(2))
        y = int(m.group(3))
        x1 = int(m.group(4))
        y1 = int(m.group(5))
        if operation == 'turn on':
            visit(x, y, x1, y1, turnon)
        elif operation == 'turn off':
            visit(x, y, x1, y1, turnoff)
        elif operation == 'toggle':
            visit(x, y, x1, y1, toggle)
    print getcount()


def visit(x, y, x1, y1, operation):
    for i in range(x, x1 + 1):
        for j in range(y, y1 + 1):
            operation(i, j)


def turnon(x, y):
    # print "turn on %d,%d" % (x,y)
    lights[x][y] += 1


def turnoff(x, y):
    # print "turn off %d,%d" % (x,y)
    lights[x][y] = max(lights[x][y] - 1, 0)


def toggle(x, y):
    # print "toggle %d,%d" % (x,y)
    lights[x][y] += 2


def getcount():
    count = 0
    for i in range(0, 1000):
        for j in range(0, 1000):
            count += lights[i][j]
    return count


if __name__ == '__main__':
    fname = "input.txt"
    if len(sys.argv) > 1:
        fname = open(sys.argv[1])
    main(fname)

