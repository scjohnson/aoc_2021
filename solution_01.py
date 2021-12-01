import numpy as np
import pandas as pd


def count(input):
    return np.sum(input[1:]-input[:-1] > 0)


def count2(input):
    return count(np.array(pd.Series(input).rolling(3).sum()[2:]))


if __name__ == "__main__":

    data = np.array([int(i) for i in open("input_01.txt")])
    print(count(data))
    print(count2(data))
