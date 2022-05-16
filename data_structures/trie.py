class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.end = False

class Trie:
    def __init__(self) -> None:
        self.head = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.head
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]

        curr.end = True

    def startswith(self, substring: str) -> bool:
            curr = self.head
            for c in substring:
                if c in curr.children:
                    curr = curr.children[c]
                else:
                    return False

            return True

    def __contains__(self, word):
        curr = self.head
        for c in word:
            if c in curr.children:
                curr = curr.children[c]
            else:
                return False

        return True if curr.end else False