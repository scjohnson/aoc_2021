import numpy as np
import operator


def most_common(instructions):
    values = np.zeros(len(instructions[0]))
    for ins in instructions:
        values += np.array([int(c) for c in ins.strip()])
    return "".join([str(int(i)) for i in np.round(values/len(instructions) + .001)])


def xo2_filter(consider, index, comparator):
    if len(consider) == 1:
        return consider

    values = most_common(consider)
    new_consider = list(filter(lambda c: comparator(values[index], c[index]), consider))

    return xo2_filter(new_consider, index+1, comparator)


def xo2_rating(file_name, comparator):
    consider = [ins.strip() for ins in open(file_name)]
    index = 0
    return int(xo2_filter(consider, index, comparator)[0], 2)


def part1(file_name):
    binary = most_common([ins.strip() for ins in open(file_name)])
    second_binary = ''.join(['1' if i == '0' else '0'
                             for i in binary])

    return int(binary, 2) * int(second_binary, 2)


if __name__ == "__main__":
    print("test part 1: ", part1("test_03.txt"))
    print("part 1: ", part1("input_03.txt"))  # 2498354
    print("test part 2: ", xo2_rating("test_03.txt", operator.eq)
          * xo2_rating("test_03.txt", operator.ne))
    print("part 2: ", xo2_rating("input_03.txt", operator.eq)
          * xo2_rating("input_03.txt", operator.ne))  # 3277956
