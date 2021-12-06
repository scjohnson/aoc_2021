import numpy as np
from skimage.draw import line


def parse(input_file):
    lines = []
    for row in open(input_file):
        f, l = row.split(" -> ")
        lines.append([int(f.split(',')[0]), int(f.split(',')[1]),
                     int(l.split(',')[0]), int(l.split(',')[1])])
    return np.array(lines)


def part1(input_file):
    lines = parse(input_file)
    image1 = np.zeros((np.max(lines)+1, np.max(lines)+1), dtype=np.uint8)
    image2 = np.zeros((np.max(lines)+1, np.max(lines)+1), dtype=np.uint8)

    for l in lines:
        rr, cc = line(l[0], l[1], l[2], l[3])

        if l[0] != l[2] and l[1] != l[3]:
            image2[rr, cc] += 1
        else:
            image1[rr, cc] += 1
            image2[rr, cc] += 1
    return (np.sum(image1 > 1), np.sum(image2 > 1))


if __name__ == "__main__":
    print("test solution: ", part1("test_05.txt"))
    print("solution: ", part1("input_05.txt"))
