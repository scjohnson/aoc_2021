import numpy as np
from scipy.optimize import minimize
import math


if __name__ == "__main__":
    locations = np.array([int(i)
                         for i in open("input_07.txt").read().split(',')])

    def fun(x): return np.sum(np.abs(locations-x))
    res = minimize(fun, np.ones(1, dtype=np.int))
    print(min(fun(math.floor(res.x)), fun(math.ceil(res.x))))

    def fun(x): return np.sum((np.abs(locations-x)+1)*np.abs(locations-x)/2)
    res = minimize(fun, np.ones(1, dtype=np.int))
    print(min(fun(math.floor(res.x)), fun(math.ceil(res.x))))
