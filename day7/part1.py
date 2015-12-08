import sys
import numpy as np

instructions = dict()
cache = dict()


def calculate(key):
    if key.isdigit():
        return np.uint16(key)

    if key in cache:
        return cache[key]

    result = None

    instruction = instructions[key]
    print "executing %s for key %s" % (instruction, key)
    tokens = instruction.split()

    if len(tokens) == 1:
        """assignment"""
        result = calculate(tokens[0])
    elif len(tokens) == 2:
        """one param operation"""
        if tokens[0] == 'NOT':
            result = ~ calculate(tokens[1])
    elif len(tokens) == 3:
        """two param operation"""
        if tokens[1] == 'AND':
            result = calculate(tokens[0]) & calculate(tokens[2])
        elif tokens[1] == 'OR':
            result = calculate(tokens[0]) | calculate(tokens[2])
        elif tokens[1] == 'LSHIFT':
            result = calculate(tokens[0]) << calculate(tokens[2])
        elif tokens[1] == 'RSHIFT':
            result = calculate(tokens[0]) >> calculate(tokens[2])
    else:
        raise Exception("Operation %s not recognized" % tokens[1])

    cache[key] = result
    return result


def main():
    fname = "input_part1.txt"
    var = "a"
    if len(sys.argv) > 1:
        fname = sys.argv[1]
    if len(sys.argv) > 2:
        var = sys.argv[2]

    for line in open(fname):
        instruction = line.rstrip().split(" -> ")
        instructions[instruction[1]] = instruction[0]

    print calculate(var)


if __name__ == '__main__':
    main()
