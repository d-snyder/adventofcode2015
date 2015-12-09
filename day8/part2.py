import sys

def main(fname):
    diff = 0
    for line in open(fname):
        encoded_string = brute_encode(line.rstrip())
        diff += (len(encoded_string) + 2 - len(line.rstrip()))
    print diff

def brute_encode(string):
    string = string.replace('\\', '\\\\')
    string = string.replace('"', '\\"')
    return string


if __name__=='__main__':
    fname = "input.txt"
    if len(sys.argv) > 1:
        fname = sys.argv[1]
    main(fname)