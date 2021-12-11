import numpy as np
from scipy import ndimage

if __name__ == "__main__":
    im = [i.strip() for i in open("test_09.txt").readlines()]
    im = [i.strip() for i in open("input_09.txt").readlines()]
    im = np.array([int(i) for line in im for i in line]
                  ).reshape(len(im), len(im[0]))

    mins = ndimage.generic_filter(im, np.min, footprint=np.array(
        [[0, 1, 0], [1, 1, 1], [0, 1, 0]])) == im
    print("Part 1: ", (im[mins][im[mins] < 9]+1).sum())

    basins = ndimage.label(im < 9)[0]
    print(ndimage.label(im < 9)[0])    
    sizes = [basins[basins == i].size for i in range(basins.max()+1)]
    print("Part 2:", np.prod(sorted(sizes, reverse=True)[1:4]))
