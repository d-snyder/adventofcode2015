import md5
import sys
from sets import Set


def isnice(input):
    vowel_count = 0
    repeated_count = 0
    restricted_count = 0
    restricted = Set(['ab', 'cd', 'pq', 'xy'])
    vowels = Set(['a', 'e', 'i', 'o', 'u'])

    if input[0] in vowels:
        vowel_count += 1

    for i in range(1, len(input)):
        if input[i] in vowels:
            vowel_count += 1
        if input[i - 1:i + 1] in restricted:
            restricted_count += 1
        if input[i - 1] == input[i]:
            repeated_count += 1

    # print "vowel_count=%d, restricted_count=%d, repeated_count=%d" % (vowel_count, restricted_count, repeated_count)

    if vowel_count >= 3 and repeated_count > 0 and restricted_count == 0:
        return True
    else:
        return False


def main(fname):
    nicecnt = 0
    for line in open(fname):
        if isnice(line.rstrip()):
            nicecnt += 1

    print nicecnt


if __name__ == '__main__':
    fname = "input.txt"
    if len(sys.argv) > 1:
        fname = sys.argv[1]
    main(fname)
