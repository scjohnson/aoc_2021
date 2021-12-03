import numpy as np
import operator


def xo2_filter(consider, index, comparator):
    if len(consider) == 1:
        return consider

    values = np.zeros(len(consider[1]))
    length = 0
    for ins in consider:
        values += np.array([int(c) for c in ins.strip()])
        length += 1
    values = "".join([str(int(i)) for i in np.round(values/length + .001)])
    new_consider = []
    for c in consider:
        if comparator(values[index], c[index]):
            new_consider.append(c)
    return xo2_filter(new_consider, index+1, comparator)


def xo2_rating(file_name, comparator):
    consider = [ins.strip() for ins in open(file_name)]
    index = 0
    return int(xo2_filter(consider, index, comparator)[0], 2)


def part1(file_name, string_length):
    values = np.zeros(string_length)
    length = 0
    for ins in open(file_name):
        values += np.array([int(c) for c in ins.strip()])
        length += 1
    binary = "".join([str(int(i)) for i in np.round(values/length)])
    second_binary = "".join([str(int(i))
                            for i in np.round(np.abs(values/length - 1))])

    return int(binary, 2) * int(second_binary, 2)


if __name__ == "__main__":
    print("test part 1: ", part1("test_03.txt", 5))
    print("part 1: ", part1("input_03.txt", 12))  # 2498354
    print("test part 2: ", xo2_rating("test_03.txt", operator.eq)
          * xo2_rating("test_03.txt", operator.ne))

    print("part 2: ", xo2_rating("input_03.txt", operator.eq)
          * xo2_rating("input_03.txt", operator.ne))  # 3277956
