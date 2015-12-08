import sys


def main(fname):
    area = 0
    ribbon = 0
    for line in open(fname):
        dims = line.rstrip().split('x')
        area += calcpaper(int(dims[0]), int(dims[1]), int(dims[2]))
        ribbon += calcribbon(int(dims[0]), int(dims[1]), int(dims[2]))

    print "paper %d" % area
    print "ribbon %d" % ribbon


def calcpaper(l, w, h):
    a1 = l * w
    a2 = w * h
    a3 = h * l
    area = 2 * ( a1 + a2 + a3 ) + min(a1, a2, a3)
    return area


def calcribbon(l, w, h):
    p1 = 2 * l + 2 * w
    p2 = 2 * w + 2 * h
    p3 = 2 * h + 2 * l

    return min(p1, p2, p3) + (l * w * h)


if __name__ == '__main__':
    fname = "input.txt"
    if len(sys.argv) > 1:
        fname = sys.argv[1]
    main(fname)
