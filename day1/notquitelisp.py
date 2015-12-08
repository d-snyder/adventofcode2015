import sys


def main(fname):
    seen_basement = False
    count = 0
    char = 0
    line = open(fname).readline()
    for c in line:
        char += 1
        if c == '\n':
            break
        elif c == '(':
            count += 1
        elif c == ')':
            count -= 1
        if count < 0 and not seen_basement:
            print "entered basement at char %d" % char
            seen_basement = True
    print "ended up at floor %d" % count


if __name__ == "__main__":
    fname = "input.txt"
    if len(sys.argv) > 1:
        fname = sys.argv[1]
    main(fname)
