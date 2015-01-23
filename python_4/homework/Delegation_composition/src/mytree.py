"""
Demonstrates using a subtree model to store data attributes.
"""
class Tree:
    def __init__(self, key, data=None):
        "Create a new Tree object with empty L & R subtrees."
        self.key = key
        self.left = self.right = None
        self.data = data
    def insert(self, key, data=None):
        "Insert a new element into the tree in the correct position."
        if key < self.key:
            if self.left:
                self.left.insert(key, data)
            else:
                self.left = Tree(key, data)
        elif key > self.key:
            if self.right:
                self.right.insert(key, data)
            else:
                self.right = Tree(key, data)
        else:
            raise ValueError("Attempt to insert duplicate value")
    def walk(self):
        "Generate the keys from the tree in sorted order."
        if self.left:
            for n in self.left.walk():
                yield n
        yield self.key
        if self.right:
            for n in self.right.walk():
                yield n
    def find(self, key):
        "Find key from the tree"
        if key == self.key:
            return self.data
        elif key < self.key:
            if self.left is None:
                raise KeyError
            return self.left.find(key)
        elif key > self.key:
            if self.right is None:
                raise KeyError
            return self.right.find(key)
