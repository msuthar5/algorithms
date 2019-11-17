"""
Leetcode #623 Add One Row to Tree
https://leetcode.com/problems/add-one-row-to-tree/
"""

# Definition for a binary tree node.
 class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

def addNodeHelper(root,v,d):
    if root:
        if d==2:
            lnode=TreeNode(v)
            rnode=TreeNode(v)
            lnode.left=root.left
            rnode.right=root.right
            root.left=lnode
            root.right=rnode
        else:
            addNodeHelper(root.left,v,d-1)
            addNodeHelper(root.right,v,d-1)

def addOneRow(root: TreeNode, v: int, d: int) -> TreeNode:
    if d == 1:
        node=TreeNode(v)
        node.left=root
        return node
    addNodeHelper(root,v,d)
    return root
