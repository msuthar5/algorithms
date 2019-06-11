"""
Hackerrank Challenge: Binary Search Tree : Lowest Common Ancestor

Given the root of a BST along with the satellite data for nodes
corresponding to v1 & v2, this function will return the lowest common
ancestor of the 2 nodes holding v1 & v2.

Run-time: O(log(n))
worst case: O(n) if the tree is a linked list

We walk a simple path from the root to v1/v2 and terminate
when the paths diverge. The point of divergence is the lowest
common ancestor

author: Manish Suthar
"""
def lca(root, v1, v2):
    LCA = n1 = n2 = root
    while n1 == n2:
        if n1 == n2:
            LCA = n1
        if n1.info == v1 or n2.info == v2:
            break
        if v1 <= n1.info:
            n1 = n1.left
        else:
            n1 = n1.right
        if v2 <= n2.info:
            n2 = n2.left
        else:
            n2 = n2.right
    return LCA
