"""
Build a histogram from scratch. Inputs: a list of floats and an integer representing the number of bins that the histogram
should have. This algorithm should return a list of lists in the following format: [start_range, end_range, count].
representing the lower end of the respective bin, the higher end of the respective bin and the number of elements contained within
that bin. 
"""

import numpy as np
import time


def get_min_max(L):
    minn = float("infinity")
    maxx = float("-infinity")
    for element in L:
        if element < minn:
            minn = element
        if element > maxx:
            maxx = element

    return minn, maxx


def histogramv1(L, n):
    max_v, min_v = get_min_max(L)  # O(L)
    bin_size = (max_v - min_v) / n

    low_end = min_v
    high_end = min_v + bin_size
    num_elements = 0
    hist = []
    for element in sorted(L):  # O(L*logL) + O(L)
        if element <= high_end:
            num_elements += 1
        else:
            hist.append([(low_end, high_end), num_elements])
            num_elements = 1
            low_end = high_end
            high_end += bin_size

    hist.append([(low_end, high_end), num_elements])

    return hist


def histogramv2(L, n):
    max_v, min_v = get_min_max(L)  # O(L)
    bin_size = (max_v - min_v) / n

    low_end = min_v
    high_end = min_v + bin_size
    hist = []
    for _ in range(n):  # O(N)
        hist.append([low_end, high_end, 0])
        low_end = high_end
        high_end += bin_size

    for element in L:  # O(L)
        i = int(np.ceil((n * ((element - min_v) / (max_v - min_v))))) - 1
        hist[i][2] += 1

    return hist


if __name__ == "__main__":
    L = np.random.randn(1_000_000)
    n = 1000

    start_v1 = time.time()
    result1 = histogramv1(L, n)
    end_v1 = time.time()

    print(end_v1 - start_v1)

    start_v2 = time.time()
    result2 = histogramv2(L, n)
    end_v2 = time.time()

    print(end_v2 - start_v2)
