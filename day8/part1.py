import sys

def main(fname):
    diff = 0
    for line in open(fname):
        decoded_string = line.rstrip()[1:-1].decode('string_escape')
        diff += (len(line.rstrip()) - len(decoded_string))
    print diff


if __name__=='__main__':
    fname = "input.txt"
    if len(sys.argv) > 1:
        fname = sys.argv[1]
    main(fname)