import sys

SYNTAX = "Syntax : cut.py -d 'delimiter' -f 'columns' 'file'."


def process_line(line, delimiter, columns):
    line = line.strip("\n")
    line_separated = line.split(delimiter)
    out = ""

    for column in columns:
        if column > len(line_separated):
            continue
        out += line_separated[column - 1] + delimiter

    if len(out) > len(delimiter):
        out = out[:-len(delimiter)]
    if out:
        print(out)


def get_ranges(columns):
    columns_separated = columns.split(",")
    for i in range(len(columns_separated)):
        split = columns_separated[i].split("-")

        if len(split) != 2:
            raise Exception("Invalid argument " + columns_separated[i])

        # str to int
        for j in range(len(split)):
            split[j] = int(split[j])

        split = range(split[0], split[1] + 1)

        columns_separated[i] = split
    ranges = []
    for my_range in columns_separated:
        ranges += list(my_range)
    ranges = set(ranges)
    return ranges


def cut(*args):
    global SYNTAX
    if args[0] != "-d":
        raise Exception("Missing '-d' argument." + "\n" + SYNTAX)
    if args[2] != "-f":
        raise Exception("Missing '-f' argument." + "\n" + SYNTAX)

    delimiter = args[1]
    columns = args[3]
    file_path = args[4]

    columns = get_ranges(columns)

    with open(file_path) as file:
        while True:
            # Get next line from file
            line = file.readline()
            # if line is empty, end of file is reached
            if not line:
                break

            process_line(line, delimiter, columns)

    pass


if __name__ == '__main__':
    if len(sys.argv) != 6:
        raise Exception("Expected 5 arguments, got " + str(len(sys.argv) - 1) + " instead." + "\n" + SYNTAX)
    cut(*sys.argv[1:])
