class Node:
    def __init__(self, key: object) -> None:
        self.key = key
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.size = 0

    def append(self, key) -> None:
        node = Node(key)
        if not self.head:
            self.head = node

        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = node

    def pop(self, key) -> None:
        if self.head:
            curr = self.head
            prev = None
            while curr.key != key and curr.next is not None:
                prev = curr
                curr = curr.next

            if curr.key == key:
                prev.next = curr.next
                del curr
