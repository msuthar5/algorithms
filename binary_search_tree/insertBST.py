"""
Hackerrank Challenge: Binary Search Tree : Insertion

worst-case runtime: O(n) if BST is a linked list

if it is a balanced BST:
    worst-case runtime: O(log(n))

author: Manish Suthar
"""

def insert(self, val):
    parent = self.root
    current = self.root
    while parent:
        current = parent
        if val < current.info:
            parent = parent.left
        else:
            parent = parent.right
    node = Node(info=val)
    if not current:
        self.root = node
        node.level = 0
    else:
        if val <= current.info:
            current.left = node
        else:
            current.right = node
    return self.root
