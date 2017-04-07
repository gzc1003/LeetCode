class Node(object):
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.children = {}


class Trie(object):
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        current_node = self.root
        for char in word:
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                current_node.children[char] = Node(char)
                current_node = current_node.children[char]

        current_node.value = word


    def search(self, word):
        if not word: return False
        current_node = self.root
        for char in word:
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                return False
        if not current_node.value:
            return False
        else:
            return True

    def has_word_starts_with(self, prefix):
        current_node = self.root
        for char in prefix:
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                return False
        return True
