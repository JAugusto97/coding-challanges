class HashTable:
    def __init__(self, capacity: int = 1000) -> None:
        self.size = 0
        self.capacity = capacity
        self.table = [None for _ in range(capacity)]

    def insert(self, key: object, value: object) -> None:
        if self.size == self.capacity:
            self.__increase_capacity()

        idx = hash(key) % self.capacity
        if not self.table[idx]:  # entry is available
            self.table[idx] = (key, value)
            self.size += 1

        else:  # entry not available, linearly search for next available entry
            if key == self.table[idx][0]:  # key already exists, replace value
                self.table[idx] = (key, value)
            else:  # different key, search for new entry
                idx = self.__linear_probe(idx, find_empty=True)
                self.table[idx] = (key, value)
                self.size += 1

    def remove(self, key: object) -> None:
        pass

    def __linear_probe(self, conflict_idx, find_empty=True):
        i = conflict_idx + 1 if conflict_idx + 1 < self.capacity else 0
        while i < self.capacity:
            if (not self.table[i] and find_empty) or (
                self.table[i] and not find_empty
            ):  # found available entry
                return i

            if i == self.capacity - 1:  # reached the end of the table, go back to start
                i = -1

            if i == conflict_idx:  # reached back to conflict_idx, no available entries
                return -1

            i += 1

    def __increase_capacity(self) -> None:
        tmp_table = self.table
        tmp_capacity = self.capacity

        self.capacity *= 2
        self.table = [None for _ in range(self.capacity)]
        for i in range(tmp_capacity):
            k, v = tmp_table[i]
            self.insert(k, v)

        self.size = tmp_capacity

    def __contains__(self, key: object) -> bool:
        pass

    def __call__(self, key: object) -> object:
        idx = hash(key) % self.capacity
        if self.table[idx] is None:
            raise KeyError
        else:
            k, v = self.table[idx]
            if k == key:
                return v
            else:
                idx_probe = idx
                while True:
                    idx_probe = self.__linear_probe(idx_probe, find_empty=False)
                    if idx_probe == -1 or idx == idx_probe:
                        raise KeyError

                    k, v = self.table[idx_probe]
                    if k == key:
                        return v


h = HashTable(10)
for i in range(15):
    h.insert(str(i), i)
    print(
        f"trying to insert {i}, current capacity: {h.capacity}, current size: {h.size}"
    )
print(h.table)
print(h("1"))
