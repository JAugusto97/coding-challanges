from typing import Union

numeric = Union[int, float]

class MinHeap:
    def __init__(self, max_capacity: int = 10_000) -> None:
        self.arr = [float("infinity")] * max_capacity
        self.max_capacity = max_capacity
        self.size = 0

    def display(self) -> None:
        print(self.arr[:self.size])

    def get_min(self) -> numeric:
        return self.arr[0]

    def extract_min(self) -> numeric:
        key = self.arr[0]
        self.arr[0] = self.arr[self.size-1]

        if self.size-1 > 0:
            self.__bubble_down()

        self.size -= 1

        return key

    def insert(self, key: numeric) -> None:
        if self.size == self.max_capacity:
            raise Exception("Heap is full")
        else:
            self.size += 1
            self.arr[self.size-1] = key
            self.__bubble_up()

    def __get_parent(self, i: int) -> int:
        return (i-1)//2

    def __get_left_child(self, i: int) -> int:
        return i*2 + 1

    def __get_right_child(self, i: int) -> int:
        return i*2 + 2

    def __swap(self, idx_i: int, idx_j:int) -> None:
        aux = self.arr[idx_i]
        self.arr[idx_i] = self.arr[idx_j]
        self.arr[idx_j] = aux

    def __bubble_up(self) -> None:
        curr_idx = self.size - 1
        parent_idx = self.__get_parent(curr_idx)
        while (self.arr[parent_idx] > self.arr[curr_idx]) and parent_idx >= 0:
            self.__swap(curr_idx, parent_idx)
            curr_idx = parent_idx
            parent_idx = self.__get_parent(curr_idx)

    def __has_left_child(self, i: int) -> bool:
        return True if self.__get_left_child(i) < self.size else False

    def __has_right_child(self, i: int) -> bool:
        return True if self.__get_right_child(i) < self.size else False

    def __get_smallest_child(self, i: int) -> int:
        smallest_child_idx = None

        # get children if they exist
        left_child_idx = self.__get_left_child(i) if self.__has_left_child(i) else None
        right_child_idx = self.__get_right_child(i) if self.__has_right_child(i) else None

        # choose which child is smaller
        if left_child_idx and right_child_idx:  # both exist, choose the smallest
            if self.arr[left_child_idx] < self.arr[right_child_idx]:
                smallest_child_idx = left_child_idx
            else:
                smallest_child_idx = right_child_idx
        else:
            if left_child_idx:  # only left side exists
                smallest_child_idx = left_child_idx
            elif right_child_idx:  # only right side exists
                smallest_child_idx = right_child_idx
            else:  # no children
                smallest_child_idx = None

        return smallest_child_idx

    def __bubble_down(self) -> None:
        curr_idx = 0
        smallest_child_idx = self.__get_smallest_child(curr_idx)

        # traverse heap while node has children and is bigger than them
        while smallest_child_idx and (self.arr[curr_idx] > self.arr[smallest_child_idx]):
            self.__swap(curr_idx, smallest_child_idx)
            curr_idx = smallest_child_idx
            smallest_child_idx = self.__get_smallest_child(curr_idx)

    def __len__(self) -> int:
        return self.size