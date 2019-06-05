"""
Assume Node() is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None

    using a list to simulate a Queue object:
    ----------------------------------------
     ** yes I know it is more efficient to use an actual Queue() object
     so we do not deal with the overhead of rearranging the list after
     calls to list.pop(0) but I wanted to use simple data structures **

    Worst Case Run Time: O(n^2):
        every node is placed in the queue once, and for each node,
        we perfrom a BFS on the sub-tree rooted at the node

    Amortized Runtime: O(n):
        n: every node is placed in the Queue once
          for every node, we must find the min/max, but the height of the tree
          is reduced by 1 (# nodes in subtree  = # nodes in parent subtree / 2)

          if we count #nodes compared for the min/max for an entire subtree, we would
          have ~ O(2*n) comparisions == O(n)

     author: Manish Suthar
"""

def min_max(root,m=True):
    max = root.data
    min = root.data
    Q = []
    Q.append(root)
    while len(Q) > 0:
        node = Q.pop(0)
        if node.data > max:
            max = node.data
        if node.data < min:
            min = node.data
        if node.left:
            Q.append(node.left)
        if node.right:
            Q.append(node.right)
    if m:
        return max
    else:
        return min

def check_binary_search_tree_(root):
    if not root:
        return True
    if root.left and root.data <= min_max(root.left,True):
        return False
    if root.right and root.data >= min_max(root.right,False):
        return False

    return check_binary_search_tree_(root.left) and check_binary_search_tree_(root.right)
