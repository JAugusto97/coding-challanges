class HashTable:
    def __init__(self, capacity: int = 1000) -> None:
        self.size = 0
        self.capacity = capacity
        self.table = [None for _ in range(capacity)]

    def insert(self, key: object, value: object) -> None:
        if self.size == self.capacity:
            print(f"MAX SIZE {self.size} {self.capacity}")
            self.__increase_capacity()

        idx = hash(key) % self.capacity
        if not self.table[idx]:  #  entry is available
            self.table[idx] = (key, value)
        else:  # entry not available, linearly search for next available entry
            i = idx + 1 if idx + 1 < self.capacity else 0
            while i < self.capacity:
                if not self.table[i]:  # found available entry
                    self.table[i] = (key, value)
                    print(f"inserted at {i}")
                    break

                if i == self.capacity-1:  # reached the end of the table, go back to start
                    i = -1

                i += 1
        
        self.size += 1

    def remove(self, key: object) -> None:
        pass

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

h = HashTable(10)
for i in range(100):
    print(f"trying to insert {i}", h.table, h.capacity, h.size)
    h.insert("a", i)
print(len(h.table))