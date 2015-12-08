import md5
import sys


def checkrepeated(input):
    seen_pairs = dict()
    for i in range(1, len(input)):
        key = input[i - 1:i + 1]
        if key in seen_pairs:
            if i - seen_pairs[key] > 1:
                return True
        else:
            seen_pairs[key] = i
        i += 1
    return False


def checkseparated(input):
    for i in range(2, len(input)):
        if input[i - 2] == input[i]:
            return True
    return False


def main(fname):
    nicecnt = 0
    for line in open(fname):
        if checkrepeated(line.rstrip()) and checkseparated(line.rstrip()):
            nicecnt += 1

    print nicecnt


if __name__ == '__main__':
    fname = "input.txt"
    if len(sys.argv) > 1:
        fname = sys.argv[1]
    main(fname)
