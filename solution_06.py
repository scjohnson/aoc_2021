import numpy as np


def part2(ages):
    hist = np.histogram(ages, bins=7, range=(0, 7))[0]
    i = 0
    new_kids = np.zeros(3)
    for _ in range(256):
        hist[i-1] += new_kids[2]
        new_kids[1:] = new_kids[:-1]
        new_kids[0] = hist[i]
        i = (i+1) % 7
    return int(np.sum(hist) + np.sum(new_kids))


def part1(ages):
    for d in range(80):
        ages = np.append(ages, 9*np.ones(np.sum(ages == 0)))
        ages[ages == 0] = 7
        ages = ages - 1
    return len(ages)


if __name__ == "__main__":
    print("test solution: ", part1(np.array([3, 4, 3, 1, 2])))
    print("test solution: ", part2(np.array([3, 4, 3, 1, 2])))
    print("solution: ", part1(np.array([1, 2, 1, 3, 2, 1, 1, 5, 1, 4, 1, 2, 1, 4, 3, 3, 5, 1, 1, 3, 5, 3, 4, 5, 5, 4, 3, 1, 1, 4, 3, 1, 5, 2, 5, 2, 4, 1, 1, 1, 1, 1, 1, 1, 4, 1, 4, 4, 4, 1, 4, 4, 1, 4, 2, 1, 1, 1, 1, 3, 5, 4, 3, 3, 5, 4, 1, 3, 1, 1, 2, 1, 1, 1, 4, 1, 2, 5, 2, 3, 1, 1, 1, 2, 1, 5, 1, 1, 1, 4, 4, 4, 1, 5, 1, 2, 3, 2, 2, 2, 1, 1, 4, 3, 1, 4, 4, 2, 1, 1, 5, 1, 1, 1, 3, 1, 2, 1, 1, 1, 1, 4, 5, 5, 2, 3, 4, 2, 1, 1, 1, 2, 1, 1, 5, 5, 3, 5, 4, 3, 1, 3, 1, 1, 5, 1,
                                        1, 4, 2, 1, 3, 1, 1, 4, 3, 1, 5, 1, 1, 3, 4, 2, 2, 1, 1, 2, 1, 1, 2, 1, 3, 2, 3, 1, 4, 5, 1, 1, 4, 3, 3, 1, 1, 2, 2, 1, 5, 2, 1, 3, 4, 5, 4, 5, 5, 4, 3, 1, 5, 1, 1, 1, 4, 4, 3, 2, 5, 2, 1, 4, 3, 5, 1, 3, 5, 1, 3, 3, 1, 1, 1, 2, 5, 3, 1, 1, 3, 1, 1, 1, 2, 1, 5, 1, 5, 1, 3, 1, 1, 5, 4, 3, 3, 2, 2, 1, 1, 3, 4, 1, 1, 1, 1, 4, 1, 3, 1, 5, 1, 1, 3, 1, 1, 1, 1, 2, 2, 4, 4, 4, 1, 2, 5, 5, 2, 2, 4, 1, 1, 4, 2, 1, 1, 5, 1, 5, 3, 5, 4, 5, 3, 1, 1, 1, 2, 3, 1, 2, 1, 1])))
    print("solution: ", part2(np.array([1, 2, 1, 3, 2, 1, 1, 5, 1, 4, 1, 2, 1, 4, 3, 3, 5, 1, 1, 3, 5, 3, 4, 5, 5, 4, 3, 1, 1, 4, 3, 1, 5, 2, 5, 2, 4, 1, 1, 1, 1, 1, 1, 1, 4, 1, 4, 4, 4, 1, 4, 4, 1, 4, 2, 1, 1, 1, 1, 3, 5, 4, 3, 3, 5, 4, 1, 3, 1, 1, 2, 1, 1, 1, 4, 1, 2, 5, 2, 3, 1, 1, 1, 2, 1, 5, 1, 1, 1, 4, 4, 4, 1, 5, 1, 2, 3, 2, 2, 2, 1, 1, 4, 3, 1, 4, 4, 2, 1, 1, 5, 1, 1, 1, 3, 1, 2, 1, 1, 1, 1, 4, 5, 5, 2, 3, 4, 2, 1, 1, 1, 2, 1, 1, 5, 5, 3, 5, 4, 3, 1, 3, 1, 1, 5, 1,
                                        1, 4, 2, 1, 3, 1, 1, 4, 3, 1, 5, 1, 1, 3, 4, 2, 2, 1, 1, 2, 1, 1, 2, 1, 3, 2, 3, 1, 4, 5, 1, 1, 4, 3, 3, 1, 1, 2, 2, 1, 5, 2, 1, 3, 4, 5, 4, 5, 5, 4, 3, 1, 5, 1, 1, 1, 4, 4, 3, 2, 5, 2, 1, 4, 3, 5, 1, 3, 5, 1, 3, 3, 1, 1, 1, 2, 5, 3, 1, 1, 3, 1, 1, 1, 2, 1, 5, 1, 5, 1, 3, 1, 1, 5, 4, 3, 3, 2, 2, 1, 1, 3, 4, 1, 1, 1, 1, 4, 1, 3, 1, 5, 1, 1, 3, 1, 1, 1, 1, 2, 2, 4, 4, 4, 1, 2, 5, 5, 2, 2, 4, 1, 1, 4, 2, 1, 1, 5, 1, 5, 3, 5, 4, 5, 3, 1, 1, 1, 2, 3, 1, 2, 1, 1])))
