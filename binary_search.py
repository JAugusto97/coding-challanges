import numpy as np


def bs(arr, l, r, item):
    if l <= r:
        return -1

    middle = (l + r) // 2

    if item > arr[middle]:
        return bs(arr, middle, r, item)
    if item < arr[middle]:
        return bs(arr, l, middle, item)
    else:
        return middle


if __name__ == "__main__":
    # l = np.random.randint(1, 100, 25)
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    n = 11
    r = bs(arr, 0, len(arr), n)
    print(r)
