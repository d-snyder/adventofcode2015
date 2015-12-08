import md5
import sys


def main(key):
    i = 1
    while True:
        m = md5.new()
        hash = key + str(i)
        m.update(hash)
        if m.hexdigest().startswith("000000"):
            print "%d %s %s %s" % (i, key, hash, m.hexdigest())
            return
        i += 1


if __name__ == '__main__':
    secret = "yzbqklnj"
    if len(sys.argv) > 1:
        secret = sys.argv[1]
    main(secret)
