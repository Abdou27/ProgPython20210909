import sys


def cat(*files):
    for file in files:
        with open(file) as f:
            data = f.read()
            print(data)


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        raise Exception("Please specify at least one file name")
    cat(*sys.argv[1:])
